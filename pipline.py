from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

def run_research_pipeline(topic: str) -> dict:
    state = {}

    #search agent working
    print("\n"+" ="*50)
    print("step1 - search agent is working...")
    print("="*50+"\n")

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"Search for recent and reliable information on the topic: {topic}")]
    })
    state['search_results'] = search_result['messages'][-1].content

    print("\n search result ",state['search_results'])

    #reader agent working
    print("\n"+" ="*50)
    print("step2 - reader agent is working...")
    print("="*50+"\n")

    reader_agent = build_reader_agent()
    # Extract URLs from search results
    reader_result = reader_agent.invoke({
        "messages": [("user", 
                      f"Based on the following search results about '{topic}',"
                      f"pick the most relevant URLs and scrape their content for deeper analysis and content.\n\n"
                      f"Search Results:\n{state['search_results'][:800]}"
                      )]
    })

    state['scraped_content'] = reader_result['messages'][-1].content
    print("\n Scraped Content: ", state['scraped_content'])

    #step3 - writer chain working
    print("\n"+" ="*50)
    print("step3 - writer chain is working...")
    print("="*50+"\n")

    research_combined =(
        f"SEARCH RESULTS:\n{state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\n Final Research Report: ", state['report'])

    #step4 - critic chain working
    print("\n"+" ="*50)
    print("step4 - critic chain is working...")
    print("="*50+"\n")

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    print("\n Critic Feedback: ", state['feedback'])

    return state

if __name__ == "__main__":
    topic = input("Enter the research topic: ")
    run_research_pipeline(topic)
    
