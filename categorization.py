import cohere
from cohere.responses.classify import Example
co = cohere.Client('KOhEHVjWjfwcwObuwb0KuGhbfSlUEAf6oYYJqlJN')
commands = {"typing", "open app", ""}

data_validity = [
    Example("Dylan, fetch me a water bottle", "not computer related"),
    Example("Dylan, open me a new chrome tab", "valid command"),
    Example("open me a new chrome tab", "invalid command"),
    Example("Dylan, type good game in chat", "valid command"),
    Example("Dylan, pause the youtube video", "valid command"),
    Example("Dylan, skip this current song", "valid command"),
    Example("Dylan, open instagram", "valid command"),
    Example("Dylan, open the door for me", "not computer related"),
    Example("Dylan, have sex with my mom", "not computer related"),
    Example("Dylan, give me head", "not computer related"),
    Example("type good game in chat", "invalid command"),
    Example("pause the youtube video", "invalid command"),
    Example("skip this current song", "invalid command"),
    Example("have sex with my mom", "invalid command"),
    Example("Dylan, do something physical", "not computer related"),
    Example("Dylan, do something virtual", "valid command")
]

data_command = [
    Example("Dylan, open chrome in my web browser", "open"),
    Example("Dylan, open safari for me", "open"),
    Example("Dylan, open firefox", "open"),
    Example("Dylan, please open nhentai.net", "open"),
    Example("Dylan, open nhentai.net pleaseplaseplasea", "open"),
    Example("Dylan, can you please open https://www.instagram.com/vickychqu/", "open"),
    Example("Dylan, type /ac good game in chat", "type"),
    Example("Dylan, can you type fuycj you", "type"),
    Example("Dylan, type t", "type"),
    Example("Dylan, please type a response in chat", "type"),

]


inputs = [input()]
while inputs != ["stop"]:
    validity = co.classify(
        inputs=inputs,
        examples=data_validity,
        model="embed-english-light-v2.0"
    )
    command = co.classify(
        inputs=inputs,
        examples=data_command,
    )
    print(f"validity: {validity.classifications[0].prediction}")
    print(f"confidence: {validity.classifications[0].confidence}")

    print(f"command type: {command.classifications[0].prediction}")
    print(f"confidence: {command.classifications[0].confidence}")

    inputs = [input()]
