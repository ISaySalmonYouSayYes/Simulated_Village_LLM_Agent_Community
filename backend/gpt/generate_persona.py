"""
This script defines a persona generator using the LangChain framework.

Key Components:
- A `gpt4_generate_persona` function that generates persona details using the GPT-4 model.

Example Usage:
Kai_Json=gpt4_generate_persona("Kai")
Input: "Alice"
Output: JSON object with persona details for Alice.
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser






class PersonaGenerator(BaseModel):
    name: str = Field(description="Persona name")
    age: int = Field(description="Persona age")
    gender: str = Field(description="Persona gender")
    occupation: str = Field(description="Persona occupation")
    hobbies: list = Field(description="Persona hobbies")
    wealth: int = Field(description="Persona wealth(0 to 1000)")
    health: int = Field(description="Persona health(0 to 100)")
    belongings: Optional[list] = Field(default=None, description="Persona belongings")
    religion: str = Field(description="Persona religion")
    ethnicity: str = Field(description="Persona ethnicity")


def gpt4_generate_persona(name: str):
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=1.2,
        n=1,
        max_tokens=256)

    parser = JsonOutputParser(pydantic_object=PersonaGenerator)
    input_text = name
    SYSTEMMESSAGE = f"""
  Please creating personal information for following person.

  Example:
        {{
            "name": "Koichiro",
            "age": "29",
            "gender": "Male",
            "status": "Student",
            "hobbies": ["painting", "cycling", "reading sci-fi"],
            "wealth": "550",
            "belongings": ["book"],
            "religious": "Buddhism",
            "ethnicity": "Japanese"
        }}

        {{
            "name": "Jill",
            "age": "27",
            "gender": "Female",
            "status": "Software Developer",
            "hobbies": ["hiking", "playing video games", "cooking"],
            "wealth": "900",
            "belongings": ["water bottle", "pencil", "knife"],
            "religious": "Catholic",
            "ethnicity": "German"
        }}

        {{
            "name": "Midori",
            "age": "25",
            "gender": "Female",
            "status": "Graphic Designer",
            "hobbies": ["drawing", "photography", "traveling"],
            "wealth": "700",
            "belongings": ["laptop", "camera", "sketchbook"],
            "religious": "Shinto",
            "ethnicity": "Japanese"
        }}
  """

    prompt = PromptTemplate(
        template="{system_message}\n{input}\n{format_instructions}\n",
        input_variables=[input],
        partial_variables={"format_instructions": parser.get_format_instructions(), "system_message": SYSTEMMESSAGE},
    )

    chain = prompt | llm | parser
    return chain.invoke({"input": input_text})


#
# def gpt4_generate_persona(name: str):
#     MODEL = 'gpt-4o-mini'
#     prompt = f"""
#   Please creating information for {name} following the persona template. Don't add extra words.
#
#   ----------------------------------------
#   Template:
#       name (str): The name of the persona.
#       age (int): Age of the persona.
#       gender (str): Gender of the persona.(Only Female, and Male)
#       status (str): Occupation or current status.
#       hobbies (list): List of hobbies the persona enjoys.
#       wealth (int): Wealth level (0 to 1000).
#       health (int): Health level (0 to 100).
#       belongings (list): Persona's belongings.
#       religious (str): Persona's religious
#       ethnicity (str): Persona's ethnicity.
#   ----------------------------------------
#   Example:
#         {{
#     "name": "Koichiro",
#             "age": "29",
#             "gender": "Male",
#             "status": "Student",
#             "hobbies": ["painting", "cycling", "reading sci-fi"],
#             "wealth": "550",
#             "belongings": ["book"],
#             "religious": "Buddhism",
#             "ethnicity": "Japanese"
#         }}
#
#
#         {{
#     "name": "Jill",
#             "age": "27",
#             "gender": "Female",
#             "status": "Software Developer",
#             "hobbies": ["hiking", "playing video games", "cooking"],
#             "wealth": "900",
#             "belongings": ["water bottle", "pencil", "knife"],
#             "religious": "Catholic",
#             "ethnicity": "German"
#         }}
#
#         {{
#     "name": "Midori",
#             "age": "25",
#             "gender": "Female",
#             "status": "Graphic Designer",
#             "hobbies": ["drawing", "photography", "traveling"],
#             "wealth": "700",
#             "belongings": ["laptop", "camera", "sketchbook"],
#             "religious": "Shinto",
#             "ethnicity": "Japanese"
#         }}
#
#
#   """
#
#     messages = [
#         SystemMessage(content="You're a system creating a simulated person"),
#         HumanMessage(content=prompt),
#     ]
#
#     llm = ChatOpenAI(
#         model=MODEL,
#         temperature=1.2,
#         n=1,
#         max_tokens=256)
#
#     return llm.invoke(messages).content
