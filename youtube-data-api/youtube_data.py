import requests, json, os, random, urllib, webbrowser
import pytagcloud
from konlpy.tag import Kkma, Hannanum1
from konlpy.utils import pprint
from collections import Counter

class YoutubeDataAPI:

    def __init__(self):
        super().__init__()

    def getVideos(self):
        key = os.getenv('youtube_data_api_key')
        endpoint = 'https://www.googleapis.com/youtube/v3/videos'
        params = {'key' : key, 'part' : 'statistics,contentDetails', 'chart' : 'mostPopular', 'regionCode' : 'KR', 'maxResults' : '10'}
        res = requests.get(endpoint, params).json()
        return res
        # print(json.dumps(res, indent=2, ensure_ascii=False))

    def getComments(self):
        key = os.getenv('youtube_data_api_key')
        endpoint = 'https://www.googleapis.com/youtube/v3/comments'
        params = {'key' : key, 'part' : 'snippet', 'parentId' : 'UgzDE2tasfmrYLyNkGt4AaABAg'}
        res = requests.get(endpoint, params).json()
        return res
        # print(json.dumps(res, indent=2, ensure_ascii=False))

    def getCommentThreads(self):
        key = os.getenv('youtube_data_api_key')
        endpoint = 'https://www.googleapis.com/youtube/v3/commentThreads'
        comments = []
        nextPageToken = ''
        while True:
            params = {'key' : key, 'part' : 'snippet', 'videoId' : '9VzZ1G8X_I0', 'maxResults' : 100, 'pageToken' : nextPageToken}
            res = requests.get(endpoint, params).json()
            print(res)
            for comment in res['items']:
                comments.append(comment['snippet']['topLevelComment']['snippet']['textOriginal'])

            nextPageToken = res.get('nextPageToken', None)
            if nextPageToken is None:
                break

        return comments

    def get_tags(self, text, ntags=50, multiplier=10):
        r = lambda: random.randint(0,255)
        color = lambda: (r(), r(), r())
        h = Hannanum()
        nouns = h.nouns(text)
        count = Counter(nouns)
        return [{ 'color': color(), 'tag': n, 'size': c*multiplier }\
                    for n, c in count.most_common(ntags)]

    def draw_cloud(self, tags, filename, fontname='D2 Coding', size=(1000, 400)):
        pytagcloud.create_tag_image(tags, filename, fontname=fontname, size=size)
        webbrowser.open(filename)
        

if __name__ == "__main__":
    a = YoutubeDataAPI()
    text = ''.join(a.getCommentThreads()[:100])
    tags = a.get_tags(text)
    a.draw_cloud(tags, 'wordcloud.png')
    pass
