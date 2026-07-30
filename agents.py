from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# llm = ChatOpenAI(model="gpt-4", temperature=0)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

#1st agent
def build_search_agent():
    return create_agent(
        model = llm,
        tools = [web_search]
    )


#2nd agent
def build_reader_agent():
    return create_agent(
        model = llm,
        tools = [scrape_url]
    )


#writer chain
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert reserch writer. Write clear,structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.
    Topic: {topic}

    Research Gathered: {research}
    
    Structure the report as:
    - Introduction
    - Key Findings(minimum 3 well-researched points)
    - Analysis
    - Conclusion
    - Sources(list all URLs found in the research)
    
    
    Be detailed, factual and professional.""")
])

writer_chain = writer_prompt | llm | StrOutputParser()

#critic_chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research critic. Evaluate the research report for accuracy, completeness, and clarity.Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.
    Report: {report}

    Respond in this exact format:
    Score: x/10

    Strengths:
    - ....
    - ....

    Areas for Improvement:
    - ....
    - ....

    One line verdict:
    ....
    """)
])

critic_chain = critic_prompt | llm | StrOutputParser()
