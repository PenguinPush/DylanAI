from categorization import default_list
from categorization import default_list_locations
from categorization import browser
import os
import keyboard
import mouse
import webbrowser

confidence_threshold = 0.8

class Variables:
    valid = False
    command = ""

def read_info(key, item):

    #print(f"{key}: {item[0]}")

    match key:
        case "validity":
            if item[1] > confidence_threshold:
               if item[0] == "valid command":
                   Variables.valid = True
               else:
                   Variables.valid = False

        case "command":
            if item[1] > confidence_threshold:
                Variables.command = item[0]
                print(Variables.command)

        case "subject":
            if item[1] > confidence_threshold:
                item_location = default_list_locations[default_list.index(item[0])]

                if item_location.startswith("http"):
                    subject_type = "url"
                else:
                    subject_type = "path"

                if Variables.valid and Variables.command == "open":
                    if subject_type == "path":
                        os.system(item_location)
                        Variables.valid = False
                        Variables.command = ""

                    if subject_type == "url":
                        webbrowser.open(item_location)
                        Variables.valid = False
                        Variables.command = ""


