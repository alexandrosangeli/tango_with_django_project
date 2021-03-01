import requests
import json
from pprint import pprint
import time

def read_bing_key():
    """reads the BING API key from a file called 'bing.key'
    returns: a string which is either None, i.e. no key found, or with a key
    remember to put bing.key in your .gitignore file to avoid committing it.
    
    See Python Anti-Patterns - it is an awesome resource to improve your python code
    Here we using "with" when opening documents
    http://bit.ly/twd-antipattern-open-files
    """

    bing_api_key = None

    try:
        with open('bing.key', 'r') as f:
            bing_api_key = f.readline().strip()
    except Exception:
        try:
            with open('../bing.key','r') as f:
                bing_api_key = f.readline().strip()
        except Exception:
            raise IOError('bing.key file not found')

    if not bing_api_key:
        raise KeyError('Bing key not found')

    return bing_api_key

def run_query(search_terms):
    """See the Microsoft's documentation on other parameters that you can set.
    http://bit.ly/twd-bing-api"""

    bing_key = read_bing_key()
    search_url = 'https://api.bing.microsoft.com/v7.0/search'
    headers = {'Ocp-Apim-Subscription-Key': bing_key}
    params = {'q': search_terms,'textDecorations':True,'textFormat':'HTML'}

    # Try to retrieve data every 3 seconds 10 times
    for i in range(11):
        if i == 10:
            raise ConnectionError('Unable to retrieve data after 10 tries 3 seconds apart')
        try:
            response = requests.get(search_url, headers=headers, params=params)
            break
        except ConnectionError:
            time.sleep(3)
            continue

        
    print(response)
    response.raise_for_status()
    search_results = response.json()

    results = []
    for result in search_results['webPages']['value']:
        results.append({
            'title':result['name'],
            'link':result['url'],
            'summary':result['snippet']
        })
    return results

def main():
    search_terms = input('Search:\n')
    pprint(run_query(search_terms))

if __name__ == '__main__':
    main()