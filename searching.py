from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyDgdskhbihKlynk5kGoWd23yyifrRrrgU0"
my_cse_id = "b1e865d1c0a764b9a"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']


results = google_search('"god is a woman" "thank you next" "7 rings"', my_api_key, my_cse_id, num=10)
for result in results:
    pprint.pprint(result)
