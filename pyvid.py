import json as simplejson
import requests
from pytube import YouTube
from pydub import AudioSegment
AudioSegment.ffmpeg = "/path/to/ffmpeg"
import os
import glob
import lxml
import urllib
import urllib.request
from urllib.request import Request, urlopen
import pytube

class YoutubeObject:
    def __init__(self, url, youtube_url):
        self.url = url
        self.youtube_url = youtube_url

    def title(self):
        json = requests.get(self.url).json()
        title = json['items'][0]['snippet']['title']
        print(title)

    def videoToMp3(self):
        youtube = pytube.YouTube(self.youtube_url)
        video = youtube.streams.first()
        video.download('/Users/aneud/Documents/Python projects/yt_mp3downloader/youtube-downloader')

        video_dir = r'C:\Users\aneud\Documents\Python projects\yt_mp3downloader\youtube-downloader'
        extension_list = ('*.mp4', '*.flv')

        os.chdir(video_dir)
        for extension in extension_list:
            for video in glob.glob(extension):
                mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
                AudioSegment.from_file(video).export(mp3_filename, format='mp3')
                os.remove(video)











if __name__ =='__main__':
    youtube_url = input('enter video url:')
    id = youtube_url.rsplit('/', 1)[1]
    api_key = 'AIzaSyC7MRHUqlvGMYEDWZyRxR5mmkjsr1GusXk'
    url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={id}&key={api_key}'
    header = {'USER-AGENT': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
    request = Request(youtube_url, headers=header)
    youtube = YoutubeObject(url, youtube_url)
    youtube.videoToMp3()
    youtube.title()
