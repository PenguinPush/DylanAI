from googleapiclient.discovery import build
import pprint
import cohere

co = cohere.Client('a3q94Odywjq3jBIDEdFlvFDVXeDDhTTOJ9g56WY9')
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

    if results:
        for result in results:
            print(result['title'])
            print(result['formattedUrl'])
            if 'snippet' in result:
                print(result['snippet'] + '\n')
            else:
                print('')
        result_text = []

        for result in results:

            if 'snippet' in result:
                result_text.append(result['title'] + result['snippet'])
            else:
                result_text.append(result['title'])


        response = co.rerank(
            model='rerank-english-v2.0',
            query=search_term,
            documents=result_text,
        )

        ordered_results = [{}, {}, {}]

        for result in response:
            min_score = min([i.relevance_score for i in response])
            max_score = max([i.relevance_score for i in response])
            index = result.index
            score = result.relevance_score
            if score >= (max_score-0.001) and not ordered_results[0]:
                ordered_results[0] = results[index]
                ordered_results[0]['score'] = (score, index)
            elif score <= (min_score+0.001) and not ordered_results[2]:
                ordered_results[2] = results[index]
                ordered_results[2]['score'] = (score, index)
            else:
                if not ordered_results[1]:
                    ordered_results[1] = results[index]
                    ordered_results[1]['score'] = (score, index)

                else:
                    for i in range(len(ordered_results)):
                        if not ordered_results[i]:
                            ordered_results[i] = results[index]
                            ordered_results[i]['score'] = (score, index)
    else:
        print("no search results")
        ordered_results = None

    return ordered_results
