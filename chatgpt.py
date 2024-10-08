# CLicking brute force
# Upsides:
#    Its really simple for code.
# Downsides:
# Theres a lot of variability of what your screen looks like.

import openai
from key import OPENAI_KEY
client = openai.OpenAI(api_key=OPENAI_KEY)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "you are the mafia"},
        {
            "role": "user",
            "content": "you need to collect debts"
        }
    ]
)

print(completion.choices[0].message.content)