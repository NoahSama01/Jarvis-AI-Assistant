from openai import OpenAI

api_key = "v1-a334ff7b44c44a3b4fffd58429a7681d21f9d9efcf15e7dce719d7fc57102b11"


# pip install openai
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
    api_key="v1-a334ff7b44c44a3b4fffd58429a7681d21f9d9efcf15e7dce719d7fc57102b11"
)

completion = client.chat.completions.create(
    model="google/gemini-2.5-pro-exp-03-25:free",
    messages=[
        {"role": "Assistant", "content": "You are a virtual assistant named Jarvis who answers questions like Alexa and Google."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message.content)
