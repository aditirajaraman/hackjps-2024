# This is a sample Python script.
from openai import OpenAI
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # setup ChatGPT secret key
    secret_key  = os.environ['OPENAPI_KEY']
    client = OpenAI(api_key=secret_key)

    # input from ChatBot
    userprompt = "What career paths for Genetics and Computer Science?"

    # execute API call
    print("Send ChatGPT API Request...")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
           {"role": "system",
             "content": userprompt}
        ]
    )

    # get API Response
    apiresponse = completion.choices[0].message

    print("ChatGPT API Response received...")

    print(apiresponse)
