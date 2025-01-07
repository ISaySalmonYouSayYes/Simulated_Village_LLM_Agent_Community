from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import JsonOutputParser

from langchain.tools import tool, StructuredTool
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field



class FirstSentenceGenerator(BaseModel):
    reason: str = Field(description="The reason why this sentence was generated")
    output: Optional[str] = Field(default=None, description="The first sentence to start the conversation")


class personNameInput(BaseModel):
    name: str = Field(description="The name of the person that you want to get info.")


class StartFirstSentence_Tool:
    def __init__(self):
        self.get_personalInfo_tool = StructuredTool(
            name="get_personalInfo",
            description="""Put in a person's name, and you'll get the info of this person.
    """,
            func=self.get_personalInfo,
            args_schema=personNameInput  # Define the expected input schema
        )

        self.get_diary_tool = StructuredTool(
            name="get_diary",
            description="""Put in a person's name, and you'll get the diary of this person.
    A diary contains what happend in the past, and would indicate the relationship between people.
    """,
            func=self.get_diary,
            args_schema=personNameInput  # Define the expected input schema
        )

        self.get_todolist_tool = StructuredTool(
            name="get_todolist",
            description="""Put in a person's name, and you'll get the to-do list of this person.
    A to-do list contains a person's schedule, what the person planned to do.
    """,
            func=self.get_todolist,
            args_schema=personNameInput  # Define the expected input schema
        )

    @staticmethod
    def get_personalInfo(name: str):
        if name == "Lea":
            personalInfo = "Name: Lea\
                Age: 23\
                Gender: Female\
                Status: Graphic Designer\
                Hobbies: drawing, yoga, traveling\
                Wealth: 410\
                Favorite Food: Sushi\
                Religious: Agnostic\
                Ethnicity: Brazilian"
            return personalInfo
        elif name == "Amy":
            personalInfo = "Name: Amy\
                Age: 29\
                Gender: Male\
                Status: Teacher\
                Hobbies: painting, cycling, reading sci-fi\
                Wealth: 510\
                Favorite Food: Sushi\
                Religious: Agnostic\
                Ethnicity: American"
            return personalInfo

    @staticmethod
    def get_diary(name: str):
        if name == "Lea":
            diary = """"Lea": { "events": [ { "title": "invitation from Amy", "time": "2025-02-12T10:00:00", "description": "Amy invited Lea to have dinner together, but I have to check when do I have time before replying." }, { "title": "Hiking Adventure", "time": "2025-03-05T07:30:00", "description": "Lea joined a group of outdoor enthusiasts for a hiking trip to the Alps, exploring breathtaking mountain views." } ] },"""
            return diary
        elif name == "Amy":
            diary = """"Amy": { "events": [ { "title": "Tech Conference Keynote", "time": "2025-01-20T09:00:00", "description": "Amy delivered a keynote speech on the future of AI in healthcare at a major tech conference in San Francisco." }, { "title": "Community Volunteering", "time": "2025-02-28T14:00:00", "description": "Amy volunteered at a local shelter, helping organize resources for families in need." } ] }"""
            return diary

    @staticmethod
    def get_todolist(name: str):
        if name == "Lea":
            todolist = """“Lea": { "to_do_list": [ { "title": "Complete Project Proposal", "deadline": "2025-01-15T23:59:00", "description": "Prepare and submit the project proposal for the upcoming research grant." }, { "title": "Team Meeting", "deadline": "2025-01-18T10:00:00", "description": "Attend the team meeting to discuss project milestones and deliverables." } ] }"""
            return todolist
        elif name == "Amy":
            todolist = """“Amy": { "to_do_list": [ { "title": "Submit Expense Report", "deadline": "2025-01-12T17:00:00", "description": "Compile and submit the monthly expense report to the finance department." }, { "title": "Client Presentation", "deadline": "2025-01-20T14:30:00", "description": "Prepare and deliver a presentation to the client outlining project progress." } ] }"""
            return todolist

def gpt4_StartFirstSentence(name_1: str, name_2: str):
    llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.2,
        n=1,
        max_tokens=10000)

    prompt = hub.pull("hwchase17/openai-functions-agent")
    prompt = prompt + " Return a JSON object formatted as follows: {{'firstSentence': <response sentence, which could be null>, 'reason': <justification for the response>}}."
    startFirstSentence_Tool = StartFirstSentence_Tool()
    tools = [startFirstSentence_Tool.get_personalInfo_tool, startFirstSentence_Tool.get_diary_tool, startFirstSentence_Tool.get_todolist_tool]
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


    SYSTEMMESSAGE = f'Decide whether {name_1} would like to start a conversation with {name_2}. Filter out three possible first sentence, and then decide which to use.\
    If no conversation is initiated, return None.'


    return agent_executor.invoke({"input": SYSTEMMESSAGE})


