from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyDgdskhbihKlynk5kGoWd23yyifrRrrgU0"
my_cse_id = "b1e865d1c0a764b9a"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def search_results(search_term):
    try:
        results = google_search(search_term, my_api_key, my_cse_id, num=3)
    except KeyError:
        results = None

#for result in results:
    #print(result['title'])
    #print(result['formattedUrl'] + '\n')

    return results
