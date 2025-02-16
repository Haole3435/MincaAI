from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain_community.chat_models import ChatOpenAI
from tools.research_tools import get_current_date, perplexity_research
from config import OPENAI_API_KEY

def create_agent_executor():
    tools = [get_current_date, perplexity_research]
    llm = ChatOpenAI(
        # model="gpt-3.5-turbo",
        model="gpt-4-turbo",
        temperature=0,
        openai_api_key=OPENAI_API_KEY
    )
    
    prompt_template = """Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin!

    Question: {input}
    Thought:{agent_scratchpad}"""
    
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)