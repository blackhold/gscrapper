from django.shortcuts import render

import requests, json
from bs4 import BeautifulSoup

def index(request):
    nav = {'menu': 'dashboard'}

    if request.method == 'POST':
        nav = {'menu': 'result'}

        post = request.POST

        _references = post['key2'].split(", ")
        _search_results = []
        _i = 0

        for _r in _references:
            if _i < 50:
                _search_term = str(post['key1'] + " " + str(_r))
                _search_results.append(search_results(_search_term))
            _i = _i + 1

        _search_results = order_results(_search_results, "result")

        _data = {'key1': post['key1'], 'key2': post['key2'], 'results': _search_results}
    else:
        _data = {}

    return render(request, 'index.html', {'nav': nav, 'data': _data})


def search(request):
    nav = {'menu': 'result'}
    _search_term = request.GET.getlist('term')

    URL = "http://suggestqueries.google.com/complete/search?client=firefox&q=" + str(_search_term)
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(URL, headers=headers)
    result = json.loads(response.content.decode('utf-8'))

    _search_results = []

    for _r in result[1]:
        _search_results.append(search_results(_r))

    _search_results = order_results(_search_results, "result")

    _data = {'key1': _search_term, 'key2': result[1], 'results': _search_results}

    return render(request, 'index.html', {'nav': nav, 'data': _data})


def search_results(search_term):
    # desktop user-agent
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

    query = search_term.replace(' ', '+')
    # https://developers.google.com/custom-search/docs/xml_results_appendices#countryCodes
    URL = f"https://google.com/search?q={query}&cr=countryES&lr=lang_es&gl=es"

    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)

    _search_results = {'search_term': None, 'result': None}

    try:
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "html.parser")

            for g in soup.find(id='result-stats'):
                try:
                    _result = g.split(" ")
                    _result = _result[1]
                    _result = int(_result.replace(".", ""))
                    _search_results = {'search_term': search_term, 'result': _result}
                except Exception:
                    pass
        elif resp.status_code == 429:
            _search_results = {'search_term': search_term, 'result': "too many requests, try again later"}

    except Exception:
        pass

    return _search_results

def order_results(var, key):
    try:
        _ordered = sorted(var, key=lambda i: i[key], reverse=True)
    except Exception:
        _ordered = var
    return _ordered