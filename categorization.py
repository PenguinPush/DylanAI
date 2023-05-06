import cohere
from cohere.responses.classify import Example
co = cohere.Client('KOhEHVjWjfwcwObuwb0KuGhbfSlUEAf6oYYJqlJN')
commands = {"typing", "open app", ""}
default_list = ["Chrome", "Safari", "Spotify", "lunar client", "youtube", "task manager", "mother", "discord", "instagram", "@vickyqchu"]

def categorize(input, subject_list=default_list):

    if subject_list is None:
        subject_list = ["Chrome", "Safari", "Spotify", "lunar client", "youtube", "task manager", "mother", "discord",
                        "instagram", "@vickyqchu"]
    inputs = [input]
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
    for subject in subject_list:
        data_subject += [
            Example(f"Dylan, please open {subject}", subject),
            Example(f"Dylan, type {subject} for me", subject),
            Example(f"Dylan, run {subject} quickly", subject),
            Example(f"Dylan, message {subject} pleaeplease", subject),
            Example(f"Dylan, please run {subject}", subject),
            Example(f"Dylan, fuck {subject} around", subject),
            Example(f"Dylan, get {subject}'s address", subject),
            Example(f"Dylan, close {subject}'s windows", subject),
            Example(f"Dylan, skip {subject} in the playlist", subject),

        ]
        data_command += [
            Example(f"Dylan, open {subject} in my web browser", "open"),
            Example(f"Dylan, open {subject} for me", "open"),
            Example(f"Dylan, open {subject}", "open"),
            Example(f"Dylan, please open {subject}", "open"),
            Example(f"Dylan, open {subject} pleaseplaseplasea", "open"),
            Example(f"Dylan, run {subject}", "open"),
            Example(f"Dylan, run {subject}", "open"),
            Example(f"Dylan, create a new {subject} tab something", "open"),

            Example(f"Dylan, can you please open {subject}", "open"),
            Example(f"Dylan, type {subject}", "type"),
            Example(f"Dylan, can you type {subject}", "type"),
            Example(f"Dylan, type {subject}", "type"),
            Example("Dylan, please type a response in chat", "type"),
            Example(f"Dylan, message {subject}", "type"),
            Example(f"Dylan, reply to {subject}", "type"),
            Example(f"Dylan, send {subject} a text message", "type"),
            Example(f"dylsn, respond to {subject}", "type"),

        ]
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
    return(
        {
            "validity": (validity.classifications[0].prediction, validity.classifications[0].confidence),
            "command": (command.classifications[0].prediction, command.classifications[0].confidence),
            "subject": (subject.classifications[0].prediction, subject.classifications[0].confidence),

        }
    )

