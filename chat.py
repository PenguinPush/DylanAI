import cohere
co = cohere.Client('cohere apikey')

def chat(input):
    response = co.chat(query=input, temperature=0.8)
    print(response.text)
    convo_id = response.conversation_id
