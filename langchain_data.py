from seckey import genapi_key
import os
os.environ['GOOGLE_API_KEY']=genapi_key
from langchain.chat_models import init_chat_model
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
message=init_chat_model("gemini-2.0-flash",model_provider='google_genai')


def generate_name(cuisine):
    #chain no.1
    prompt_template_name=PromptTemplate(
        input_variables=['cuisine'],
        template='I want to open a resturant for {cuisine} food. Suggest a fancy name for this and just suggest one name'
    )
    name_chain=LLMChain(llm=message,prompt=prompt_template_name,output_key="resturant_name")

    #chain no.2
    prompt_template_items=PromptTemplate(
        input_variables=['resturant_name'],
        template='Suggest some menu items for {resturant_name}. Return it as a comma seprated list'
    )
    food_items_chain=LLMChain(llm=message,prompt=prompt_template_items,output_key="food_items")

    #output
    chains2=SequentialChain(
        chains=[name_chain,food_items_chain],
        input_variables=['cuisine'],
        output_variables=['resturant_name','food_items']
    )
    response =chains2({'cuisine':cuisine})
    
    return  response

if __name__ =="__main__":
    print(generate_name("Indian"))