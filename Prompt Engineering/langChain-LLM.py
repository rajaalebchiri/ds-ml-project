"""Building LLM application using LangChain """
from langchain_openai import OpenAI
import langchain_core

OPENAI_KEY = "KEY_GOES_HERE"

USER_INPUT = "Paris"

template = """ I am travelling to {location}. What are the top 3 things I can do while I am there. Be very specific and respond as three bullet points """


llm = OpenAI(model_name="gpt-3.5-turbo-instruct", openai_api_key=OPENAI_KEY)


print("Response from OpenAI")
print(llm.invoke("Tell me a joke about data scientist"))



prompt = langchain_core.prompts.PromptTemplate(

input_variables=["location"],

template=template,

)

final_prompt = prompt.format(location=USER_INPUT )

print(f"LLM Output: {llm.invoke(final_prompt)}")