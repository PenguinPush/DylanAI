import cohere
co = cohere.Client('KOhEHVjWjfwcwObuwb0KuGhbfSlUEAf6oYYJqlJN')
inpt = input()
response = co.chat(
    query=inpt,
    temperature=0.8
)
print(response.text)
convo_id = response.conversation_id

while True:
    inpt = input()
    response = co.chat(
        query=inpt,
        temperature=1,
        conversation_id=convo_id
    )
    print(response.text)
