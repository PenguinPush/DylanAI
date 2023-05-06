import cohere
from cohere.responses.classify import Example
co = cohere.Client('KOhEHVjWjfwcwObuwb0KuGhbfSlUEAf6oYYJqlJN')
commands = {"typing", "open app", "other"}
default_list = ["Chrome", "Youtube", "Google Translate", "File Explorer", "Notepad"]
default_list_locations = ["C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s", "https://youtube.com", "https://translate.google.com/", "C:\Windows\explorer.exe", "C:\Windows\\notepad.exe"]
browser = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

def categorize(input, subject_list=default_list):

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
            Example(f"Dylan, open {subject} please", "open"),
            Example(f"Dylan, run {subject}", "open"),
            Example(f"Dylan, launch {subject}", "open"),
            Example(f"Dylan, create a new {subject} tab something", "open"),
            Example(f"Dylan, start {subject}", "open"),
            Example(f"Dylan, use {subject}", "open"),

            Example(f"Dylan, type {subject}", "type"),
            Example(f"Dylan, can you type {subject}", "type"),
            Example(f"Dylan, type {subject}", "type"),
            Example(f"Dylan, please type a response in chat", "type"),
            Example(f"Dylan, message {subject}", "type"),
            Example(f"Dylan, reply to {subject}", "type"),
            Example(f"Dylan, send {subject} a text message", "type"),
            Example(f"Dylan, respond to {subject}", "type"),

            Example(f"Dylan, update {subject}", "other"),
            Example(f"Dylan, configure {subject}", "other"),
            Example(f"Dylan, troubleshoot {subject}", "other"),
            Example(f"Dylan, customize {subject}", "other"),
            Example(f"Dylan, analyze {subject}", "other"),
            Example(f"Dylan, organize {subject}", "other"),
            Example(f"Dylan, schedule {subject}", "other"),
            Example(f"Dylan, backup {subject}", "other"),
            Example(f"Dylan, restore {subject}", "other"),
            Example(f"Dylan, export {subject}", "other"),
            Example(f"Dylan, import {subject}", "other"),
            Example(f"Dylan, record {subject}", "other"),
            Example(f"Dylan, stream {subject}", "other"),
            Example(f"Dylan, broadcast {subject}", "other"),
            Example(f"Dylan, stop {subject}", "other"),
            Example(f"Dylan, shuffle {subject}", "other"),
            Example(f"Dylan, repeat {subject}", "other"),
            Example(f"Dylan, skip {subject}", "other"),
            Example(f"Dylan, rewind {subject}", "other"),
            Example(f"Dylan, fast forward {subject}", "other"),
            Example(f"Dylan, delete {subject}", "other"),
            Example(f"Dylan, clear {subject}", "other"),
            Example(f"Dylan, undo {subject}", "other"),
            Example(f"Dylan, redo {subject}", "other"),
            Example(f"Dylan, resize {subject}", "other"),
            Example(f"Dylan, rotate {subject}", "other"),
            Example(f"Dylan, crop {subject}", "other"),

            Example(f"Dylan, lift {subject}", "other"),
            Example(f"Dylan, throw {subject}", "other"),
            Example(f"Dylan, run with {subject}", "other"),
            Example(f"Dylan, kick {subject}", "other"),
            Example(f"Dylan, catch {subject}", "other"),
            Example(f"Dylan, climb {subject}", "other"),
            Example(f"Dylan, balance {subject}", "other"),
            Example(f"Dylan, jump over {subject}", "other"),
            Example(f"Dylan, swim across {subject}", "other"),
            Example(f"Dylan, ride {subject}", "other"),
            Example(f"Dylan, drive {subject}", "other"),
            Example(f"Dylan, fly {subject}", "other"),
            Example(f"Dylan, walk on {subject}", "other"),
            Example(f"Dylan, punch {subject}", "other"),
            Example(f"Dylan, dance with {subject}", "other"),
            Example(f"Dylan, exercise with {subject}", "other"),
            Example(f"Dylan, hug {subject}", "other"),
            Example(f"Dylan, kiss {subject}", "other"),
            Example(f"Dylan, high-five {subject}", "other"),
            Example(f"Dylan, shake hands with {subject}", "other"),
            Example(f"Dylan, massage {subject}", "other"),
            Example(f"Dylan, feed {subject}", "other"),
            Example(f"Dylan, pet {subject}", "other"),
            Example(f"Dylan, water {subject}", "other"),
            Example(f"Dylan, paint {subject}", "other"),
            Example(f"Dylan, carve {subject}", "other")
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

