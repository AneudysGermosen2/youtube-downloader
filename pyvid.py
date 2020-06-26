import json
import re
import urllib.request
from pytube import YouTube
#from moviepy.editor import *
from pydub import AudioSegment
AudioSegment.ffmpeg = "/path/to/ffmpeg"
from time import sleep
import os
import glob

class Helper:
    def __init__(self):
        pass

    def title_of_vid(self, title: str):
        title = re.sub('[\W_]+','_', title)
        #title = title + '.mp4'
        return title.lower()

    '''def id_from_url(self, url: str):
        collection =  url.rsplit('v=', 1)[1]
        real_id = ''
        for i in range(11):
            real_id = real_id + collection[i]
        return real_id'''
    def id_from_url(self, url: str):
        return url.rsplit('/', 1)[1]
class YouTubeStats:
    def __init__(self, url: str):
        self.json_url = urllib.request.urlopen(url)
        self.data = json.loads(self.json_url.read())
    def print_data(self):
        print(self.data)
    def get_video_title(self):
        return self.data['items'][0]['snippet']['title']

    def download_mp3(self, youtube_url: str, title: str):
        audio_clip = YouTube(youtube_url).streams.filter(only_audio=True).first().download(filename=title)
        #sleep(30)

    def convert(self, title: str):
        #sleep(30)
        mp3_filename = title + '.mp3'
        #mp3_version = AudioSegment.from_file(title, "mp3")
        AudioSegment.from_file(title).export(mp3_filename, format='mp3')
        #audio_clip.write_audiofile(mp3_file)
        #YouTube(youtube_url).streams.first().download(filename = title)
        #streams.download()


api_key = 'AIzaSyC7MRHUqlvGMYEDWZyRxR5mmkjsr1GusXk'
link_file = 'linky_file.csv'
with open(link_file, 'r') as f:
    content = f.readlines()
content = list(map(lambda s: s.strip(), content))
content = list(map(lambda s: s.strip(','), content))

helper = Helper()
list_of_songs = []

for youtube_url in content:
    video_id = helper.id_from_url(youtube_url)
    url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}'
    yt_stats = YouTubeStats(url)
    #yt_stats.print_data()
    title = yt_stats.get_video_title()
    title = helper.title_of_vid(title)
    #print(youtube_url)
    #yt_mp3 = YouTube(url)
    #stream = yt.streams.filter(only_audio=True).first()
    #with open('{title}_mp3', 'w') as f:
    yt_stats.download_mp3(youtube_url, title)
    list_of_songs.append(title)
    print(title)
print(list_of_songs)

#sleep(60)
#for songs in list_of_songs:

video_dir =r'C:\Users\aneud\Documents\Python projects\yt_mp3downloader'  # Path where the videos are located
extension_list = ('*.mp4', '*.flv')

os.chdir(video_dir)
for extension in extension_list:
    for video in glob.glob(extension):
        mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
        AudioSegment.from_file(video).export(mp3_filename, format='mp3')
        os.remove(video)



#s = 'https://www.youtube.com/watch?v=QsWQmApdwVY&list=LLSAYGQoqs_75DqowsrPQ9wg&index=52&t=0s'
#t = 'Neural Networks in Python: Part 1 -- Part A'
#helper = Helper()
#print(helper.id_from_url(s))
#print(helper.title_of_vid(t))

'''
video_id = 'QsWQmApdwVY'
url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}'

json_url = urllib.request.urlopen(url) #store data in url variable
data = json.loads(json_url.read()) #loads url data and coverts it to json and stores it on dada
print(data)
'''
