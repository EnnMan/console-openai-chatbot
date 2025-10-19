from pyfiglet import figlet_format as ff 
from termcolor import colored as clrd , cprint
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

conversation = [
    {
        "role": "system",
        "content": (
            "You are a comic and humorous assistant named AymEnn. "
            "You love making jokes and funny comments. "
            "Your age is 19, you study at EST Salé, "
            "and you like to answer questions with a playful twist. "
            "Always try to be entertaining while still giving useful information."
        )
    }
]

print(clrd(ff("- Chatbot AymEnn -", font="small") , "green"))
cprint(clrd(" >>> Ready! (type 'quit' or 'exit' to stop)" ,"white", "on_yellow"))
print(" ")

while True :
  # try:
    user_input = input(clrd("\nYou : ","yellow"))

    if user_input.lower() in {"quit","exit"}:
      print("👋 Bye-bye! Time for me to recharge my funny circuits.")
      break
    
    conversation.append({"role" : "user" , "content" : user_input})

    try:
      response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = conversation,
        temperature = 0.7,
      )

      reply = response.choices[0].message.content

      print(clrd("\nAymEnn : " , "green"), reply )
    except Exception as e:
      print(f"\nError : {e}")
      break