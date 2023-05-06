from categorization import default_list_dict
from categorization import get_searchable_term
from searching import search_results
import os
import keyboard
import mouse
import webbrowser

confidence_threshold = 0.8

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
            if item[1] > confidence_threshold:
                item_location = default_list_dict[item[0]]

                if item_location.startswith("http"):
                    subject_type = "url"
                else:
                    subject_type = "path"

                if VariablesMacros.valid == 1 and VariablesMacros.command == "open":
                    if subject_type == "path":
                        os.system(item_location)
                        VariablesMacros.valid = False
                        VariablesMacros.command = ""

                    if subject_type == "url":
                        webbrowser.open(item_location)
                        VariablesMacros.valid = False
                        VariablesMacros.command = ""

                else:
                    if VariablesMacros.valid > 0:
                        print(get_searchable_term(text))
                        results = search_results(get_searchable_term(text), 3)
                        for result in results:
                            print(result['title'])
                            print(result['formattedUrl'] + '\n')

            else:
                if VariablesMacros.valid > 0:
                    print(get_searchable_term(text))
                    results = search_results(get_searchable_term(text), 3)
                    for result in results:
                        print(result['title'])
                        print(result['formattedUrl'] + '\n')



