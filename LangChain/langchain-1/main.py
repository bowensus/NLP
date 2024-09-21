from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import argparse

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()

# note: this is your openai api_key
# it is not free, you need to add a debit card for payment method
# at least you need pay for 5 dollers

llm = OpenAI()

code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}",
    input_variables=["language", "task"]
)

test_prompt = PromptTemplate(
  template="Write a test for the following {language} code:\n{code}",
  input_variables=["language", "code"]
)

code_chain = code_prompt | llm
test_chain = test_prompt | llm

code_result = code_chain.invoke({
    "language": args.language,
    "task": args.task
})

chain = code_chain | (lambda code_result: {"language": args.language, "code": code_result}) | test_chain

result = chain.invoke({
    "language": args.language,
    "task": args.task
})

print(result)
