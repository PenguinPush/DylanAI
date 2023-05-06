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



temp_subject_list = ["Chrome", "Safari", "Spotify", "lunar client", "youtube", "task manager", "mother", "discord", "instagram", "@vickyqchu"]
data_command = []
data_subject = []
for temp_subject in temp_subject_list:
    data_subject += [
        Example(f"Dylan, please open {temp_subject}", temp_subject),
        Example(f"Dylan, type {temp_subject} for me", temp_subject),
        Example(f"Dylan, run {temp_subject} quickly", temp_subject),
        Example(f"Dylan, message {temp_subject} pleaeplease", temp_subject),
        Example(f"Dylan, please run {temp_subject}", temp_subject),
        Example(f"Dylan, fuck {temp_subject} around", temp_subject),
        Example(f"Dylan, get {temp_subject}'s address", temp_subject),
        Example(f"Dylan, close {temp_subject}'s windows", temp_subject),
        Example(f"Dylan, skip {temp_subject} in the playlist", temp_subject),

    ]
    data_command += [
        Example(f"Dylan, open {temp_subject} in my web browser", "open"),
        Example(f"Dylan, open {temp_subject} for me", "open"),
        Example(f"Dylan, open {temp_subject}", "open"),
        Example(f"Dylan, please open {temp_subject}", "open"),
        Example(f"Dylan, open {temp_subject} pleaseplaseplasea", "open"),
        Example(f"Dylan, run {temp_subject}", "open"),
        Example(f"Dylan, run {temp_subject}", "open"),
        Example(f"Dylan, create a new {temp_subject} tab something", "open"),

        Example(f"Dylan, can you please open {temp_subject}", "open"),
        Example(f"Dylan, type {temp_subject}", "type"),
        Example(f"Dylan, can you type {temp_subject}", "type"),
        Example(f"Dylan, type {temp_subject}", "type"),
        Example("Dylan, please type a response in chat", "type"),
        Example(f"Dylan, message {temp_subject}", "type"),
        Example(f"Dylan, reply to {temp_subject}", "type"),
        Example(f"Dylan, send {temp_subject} a text message", "type"),
        Example(f"dylsn, respond to {temp_subject}", "type"),

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
        model="embed-english-light-v2.0"
    )
    subject = co.classify(
        inputs=inputs,
        examples=data_subject,
        model="embed-english-light-v2.0"

    )
    print(f"validity: {validity.classifications[0].prediction}")
    print(f"confidence: {validity.classifications[0].confidence}")

    print(f"command type: {command.classifications[0].prediction}")
    print(f"confidence: {command.classifications[0].confidence}")

    print(f"subject: {subject.classifications[0].prediction}")
    print(f"confidence: {subject.classifications[0].confidence}")

    inputs = [input()]

