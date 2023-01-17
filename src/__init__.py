from src.getAnimes import get_animes
from src.searchAnime import search_anime
from src.getCapList import get_cap_list
from src.downloadCap import download_cap

ROOT = [
    {
        'path': '/getAnimes/<string:page>',
        'method': 'GET',
        'function': get_animes,
        'endpoint': 'get_animes'
    },
    {
        'path': '/searchAnime/<string:query>',
        'method': 'GET',
        'function': search_anime,
        'endpoint': 'search_anime'
    },
    {
        'path': '/getCapList/<string:anime_name>',
        'method': 'GET',
        'function': get_cap_list,
        'endpoint': 'get_cap_list'
    },
    {
        'path': '/downloadCap/<string:cap_name>',
        'method': 'GET',
        'function': download_cap,
        'endpoint': 'download_cap'
    }
]