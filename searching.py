from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyCcljAuCPGhz7jdA8u_KPQYNnPUeiYZ3sU"
my_cse_id = "b1e865d1c0a764b9a"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def search_results(search_term, results_number=3):
    try:
        results = google_search(search_term, my_api_key, my_cse_id, num=results_number)
    except KeyError:
        results = None

#for result in results:
    #print(result['title'])
    #print(result['formattedUrl'] + '\n')

    return results
