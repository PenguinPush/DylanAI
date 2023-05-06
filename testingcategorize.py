from categorization import categorize

subjects = ["Chrome", "Safari", "Spotify", "lunar client", "youtube", "task manager", "mother", "discord", "instagram", "@vickyqchu"]

inpt = input()

while inpt != "stop":
    categories = categorize(inpt, subjects)

    for key, item in categories.items():
        print(f"{key}: {item}")
    inpt = input()
