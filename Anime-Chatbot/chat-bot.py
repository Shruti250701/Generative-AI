import openai
import os

openai.api_key  = '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'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

def get_summary(text) :
    prompt = f"""Summarize this ```{text}``` """
    response = get_completion(prompt)
    return response

temperature = 0
messages =  [  
{'role':'system', 'content':"You are an assistant that speaks about anime and anime characters and everything about anime"},    
{'role':'user', 'content':'what is an anime'},   
{'role':'assistant', 'content':'a style of Japanese film and television animation, typically aimed at adults as well as children.'},   
{'role':'user', 'content':'what is best thing about it'} ,
{'role':'assistant', 'content':'Expressive art form. Anime expresses its story through animation, which has its unique way of delivering stories or ideas in a creative expression which is another crucial reason why you should watch anime.'} ]

while True : 
    user_input = input("You : ")
    messages.append({'role' : 'user', 'content' : user_input})
    response = get_completion_from_messages(messages, temperature=0)
    print("Anime-BOT : ", response)
    summary = get_summary(response)
    messages.append({'role':'assistant', 'content': summary})
    if (user_input == "exit") :
        break
    print()