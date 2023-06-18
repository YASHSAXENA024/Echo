import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Write an essay about lions"}])
print(completion.choices[0].message.content)