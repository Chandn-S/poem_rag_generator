# Description: This file contains the function that generates an 8-line poem by invoking a GROQ-based language model.
import prompt
from model import create_chat_groq
def poem(topic_str):
    """
    This function generates an 8-line poem by invoking a GROQ-based language model.
    
    Steps:
    1. Creates a ChatGroq instance using the `create_chat_groq` function.
    2. Sends a prompt to the model to generate an 8-line poem.
    3. Returns the model's response content.
    
    Returns:
        str: The content of the generated poem returned by the model.
    """
    prompt_temp=prompt.poem_generator_prompt_from_hub()

    llm= create_chat_groq()

    chain = prompt_temp| llm
    response = chain.invoke({"question":topic_str})
    return response.content