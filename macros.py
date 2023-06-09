from categorization import default_list_dict, get_typeable_term, get_searchable_term
from searching import search_results
import os
import keyboard
import mouse
import webbrowser
import subprocess
confidence_threshold = 0.8


import cohere

co = cohere.Client('cohere apikey')


class VariablesMacros:
    valid = 0
    command = ""


def read_info(key, item, text):
    match key:
        case "validity":
            if item[1] > confidence_threshold / 4:
                match item[0]:
                    case "valid command":
                        VariablesMacros.valid = 1
                    case "not computer related":
                        VariablesMacros.valid = 2
                    case "invalid command":
                        VariablesMacros.valid = 0

        case "command":
            if item[1] > confidence_threshold:
                VariablesMacros.command = item[0]

        case "subject":
            item_location = default_list_dict.get(item[0])
            print(item_location)

            if item_location.startswith("http"):
                subject_type = "url"
            else:
                subject_type = "path"

            if VariablesMacros.valid == 1 and VariablesMacros.command == "open":
                if subject_type == "path":
                    subprocess.Popen(item_location)
                    VariablesMacros.valid = False
                    VariablesMacros.command = ""
                    return f"Opening file at {item_location}..."

                if subject_type == "url":
                    webbrowser.open(item_location)
                    VariablesMacros.valid = False
                    VariablesMacros.command = ""
                    return f"Opening url {item_location}..."

            elif VariablesMacros.valid == 1 and VariablesMacros.command == "search":
                search_term = get_searchable_term(text)
                print(f"the searched term is: {search_term}")
                results = search_results(search_term, 3)
                if results:
                    for result in results:
                        if not result:
                            break
                        else:
                            print(result['title'])
                            print(result['formattedUrl'] + '\n')
                    webbrowser.open(results[0]['link'])
                    VariablesMacros.valid = False
                    VariablesMacros.command = ""
                return f"Searching for {search_term}..."

            elif VariablesMacros.valid == 1 and VariablesMacros.command == "type":
                if VariablesMacros.valid != 0:
                    type_term = get_typeable_term(text)
                    print(f"the typed term is: {type_term}")
                    keyboard.write(type_term)
            elif VariablesMacros.valid != 0:
                response = co.chat(
                    query=text,
                    temperature=0.7,
                )
                print(response.text)
                return response.text

