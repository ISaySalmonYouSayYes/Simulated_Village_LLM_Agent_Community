from Persona import Persona
from config import OPENAI_API_KEY, LANGSMITH_API_KEY
import os

from gpt.startFirstSentence import gpt4_StartFirstSentence

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
os.environ['LANGSMITH_API_KEY'] = LANGSMITH_API_KEY

if __name__ == "__main__":
    #001
    # persona_Yuki = Persona.generate_persona_from_gpt("Yuki")
    # persona_Yuki.display_info()

    #002
    temp = gpt4_StartFirstSentence("Lea", "Amy")
    print(temp)
