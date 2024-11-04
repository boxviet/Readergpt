# CLicking brute force
# Upsides:
#    Its really simple for code.
# Downsides:
# Theres a lot of variability of what your screen looks like.

# Web scraping ideas - 

# - Kahoot god
# - Automatic typer
# - GPT-4 Summarization of very long text

import openai
from key import OPENAI_KEY
client = openai.OpenAI(api_key=OPENAI_KEY)
def ChatGpt(Prompt, Content):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": Prompt},
            {
            "role": "user",
            "content": Content
            }
        ]
    )
    return completion.choices[0].message.content
    
def DALLE(Prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=Prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return response.data[0].url




# print(ChatGpt("you are a quiz answerer. ONLY ANSWER WITH QUESTION ANSWER, NO EXTRA CHARACTERS", "what is the capital of the USA?"))
