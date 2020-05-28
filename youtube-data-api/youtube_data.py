import requests, json, os

class YoutubeDataAPI:

    def __init__(self):
        super().__init__()

    def getVideos(self):
        key = os.getenv('youtube_data_api_key')
        endpoint = 'https://www.googleapis.com/youtube/v3/videos'
        params = {'key' : key, 'part' : 'statistics,contentDetails', 'chart' : 'mostPopular', 'regionCode' : 'KR', 'maxResults' : '10'}
        res = requests.get(endpoint, params).json()
        print(json.dumps(res, indent=2, ensure_ascii=False))

    def getComments(self):
        key = os.getenv('youtube_data_api_key')
        endpoint = 'https://www.googleapis.com/youtube/v3/comments'
        params = {'key' : key, 'part' : 'snippet', 'parentId' : 'UgzDE2tasfmrYLyNkGt4AaABAg'}
        res = requests.get(endpoint, params).json()
        print(json.dumps(res, indent=2, ensure_ascii=False))

    def getCommentThreads(self):
        key = os.getenv('youtube_data_api_key')
        endpoint = 'https://www.googleapis.com/youtube/v3/commentThreads'
        params = {'key' : key, 'part' : 'snippet', 'videoId' : 'ax2mwUxv0bU', 'maxResults' : 5}
        res = requests.get(endpoint, params).json()
        print(json.dumps(res, indent=2, ensure_ascii=False))

        
if __name__ == "__main__":
    a = YoutubeDataAPI()
    a.getCommentThreads()
    pass
