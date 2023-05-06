from categorization import categorize
import keyboard
import mouse

confidence_threshold = 0.9

def read_info(key, item):

    #print(f"{key}: {item[0]}")

    match key:
        case "validity":
            if item[1] > confidence_threshold:
                print(item[0])

        case "command":
            if item[1] > confidence_threshold:
                print(item[0])

        case "subject":
            if item[1] > confidence_threshold:
                print(item[0])
