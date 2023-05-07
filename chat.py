import cohere
co = cohere.Client('a3q94Odywjq3jBIDEdFlvFDVXeDDhTTOJ9g56WY9')

def chat(input):
    response = co.chat(query=input, temperature=0.8)
    print(response.text)
    convo_id = response.conversation_id
