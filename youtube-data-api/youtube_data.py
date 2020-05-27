import requests, json, os

class YoutubeDataAPI:

    def __init__(self):
        super().__init__()

    def getVideos(self):
        key = os.getenv('youtube_data_api_key')
        endpoint = 'https://www.googleapis.com/youtube/v3/videos'
        params = {'key' : key, 'part' : 'snippet', 'chart' : 'mostPopular', 'regionCode' : 'KR', 'maxResults' : '10'}
        res = requests.get(endpoint, params).json()
        print(json.dumps(res, indent=2, ensure_ascii=False))

        
if __name__ == "__main__":
    a = YoutubeDataAPI()
    a.getVideos()
    pass
