from openai import OpenAI
key = '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'
client = OpenAI(api_key=key)
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)
