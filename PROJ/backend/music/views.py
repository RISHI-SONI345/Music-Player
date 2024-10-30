import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def search_music(request):
    search_term = request.query_params.get('term', '')
    url = f'https://itunes.apple.com/search?term={search_term}&media=music&entity=album'
    response = requests.get(url)
    data = response.json()
    return Response(data)
