import os

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain


if __name__ == "__main__":
    print("hello langchain!")

    summary_template = """
    given the {information} about a person, I want you to create:
    1. a short summary
    2. two interesting facts about them"""

    summary_prompt_template = PromptTemplate(
        input_variables["information"], template=summary_template
    )
