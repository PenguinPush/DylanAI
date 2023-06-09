import cohere
from cohere.responses.classify import Example
co = cohere.Client('cohere apikey')
commands = {"typing", "open app", "other"}


default_list_dict = {
    "Youtube": "https://youtube.com",
    "Google Trasnlate": "https://translate.google.com/",
    "File explorer": "C:\Windows\explorer.exe",
    "Notepad": "C:\Windows\\notepad.exe"
}
browser = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

def categorize(input, subject_list=default_list_dict.keys()):
    co = cohere.Client('cohere apikey')
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
        Example("type good game in chat", "invalid command"),
        Example("pause the youtube video", "invalid command"),
        Example("skip this current song", "invalid command"),
        Example("Dylan, do something physical", "not computer related"),
        Example("Dylan, do something virtual", "valid command"),
        Example("Dylan, search for a recipe for chocolate chip cookies.", "valid command"),
        Example("Dylan, play the latest episode of 'Game of Thrones'.", "valid command"),
        Example("Dylan, send an email to John with the attachment.", "valid command"),
        Example("Dylan, schedule a meeting for tomorrow at 2 PM.", "valid command"),
        Example("Dylan, set a reminder for my dentist appointment on Friday.", "valid command"),
        Example("Search for a recipe for chocolate chip cookies.", "invalid command"),
        Example("Play the latest episode of 'Game of Thrones'.", "invalid command"),
        Example("Send an email to John with the attachment.", "invalid command"),
        Example("Schedule a meeting for tomorrow at 2 PM.", "invalid command"),
        Example("Set a reminder for my dentist appointment on Friday.", "invalid command"),
        Example("Dylan, pass the salt, please.", "not computer related"),
        Example("Dylan, turn on the lights in the living room.", "not computer related"),
        Example("Dylan, order a pizza for dinner tonight.", "not computer related"),
        Example("Dylan, feed the dog before leaving.", "not computer related"),
        Example("Dylan, water the plants in the garden.", "not computer related")
    ]

    data_command = []
    data_subject = []
    for subject in subject_list:
        data_subject += [
            Example(f"Dylan, please open {subject}", subject),
            Example(f"Dylan, type {subject} for me", subject),
            Example(f"Dylan, run {subject} quickly", subject),
            Example(f"Dylan, message {subject} please", subject),
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
            Example(f"Dylan, respond to {subject}", "type"),
            Example(f"Dylan, write {subject}", "type"),
            Example(f"Dylan, can you write {subject}", "type"),
            Example(f"Dylan, write {subject}", "type"),
            Example("Dylan, please write a response in chat", "type"),

            Example(f"Dylan, search for {subject}", "search"),
            Example(f"Dylan, find mcdonalds locations near me", "search"),
            Example(f"Dylan, locate {subject}", "search"),
            Example(f"Dylan, find me a {subject} online", "search"),
            Example(f"Dylan, look for a {subject}", "search"),
            Example(f"Dylan, browse for a {subject}", "search"),
            Example(f"Dylan, browse the web for {subject}", "search"),
            Example(f"Dylan, look up {subject}", "search"),
            Example(f"Dylan, Google {subject}", "search"),
            Example(f"Dylan, surf for {subject}", "search"),
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



def get_searchable_term(string):
    co = cohere.Client('cohere apikey')
    prompt = f'''
    When I specify it, there will be a prompt, a user command to DYLAN, an ai system designed to search terms. 
    You will need to output a concise, searchable term based on the prompt below, removing any mentions of DYLAN, and just making it into a searchable message:
    Here is the user inputted prompt:
    {string}'''
    response = co.generate(
        model='command-nightly',
        prompt=prompt,
        max_tokens=200,
        temperature=0)
    terms = response.generations[0].text
    return terms

def get_typeable_term(string):
    co = cohere.Client('cohere apikey')
    prompt = f'''
    When I specify it, there will be a prompt, a user command to DYLAN, an ai system designed to type terms to aid those with accessibility needs. 
    You will need to remove references to DYLAN and any other details around the typed phrase, and leave only the typed phrase. 
    For example, if the prompt was "Dylan, message my mom that to pick me up from school", the response would be "pick me up from school":
    However, if the user requires you to write a creative writing prompt, or something beyond a simple quote, do that to your fullest ability.
    Here is the user inputted prompt:
    {string}'''
    response = co.generate(
        model='command-nightly',
        prompt=prompt,
        max_tokens=200,
        temperature=0)
    terms = response.generations[0].text
    return terms

#while True:
    #inpt = input()
    #print(get_typeable_term(inpt))
    #print(get_searchable_term(inpt))
