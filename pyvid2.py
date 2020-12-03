import json as simplejson
import requests
#import re
from pytube import YouTube
from pydub import AudioSegment
AudioSegment.ffmpeg = "/path/to/ffmpeg"
#from time import sleep
import os
import glob
import lxml
#from lxml import etree
import urllib
import urllib.request
from urllib.request import Request, urlopen
import pytube

#import simplejson
youtube_url = input('enter video url:')
#if(youtube_url == NULL):
    #print('invalid input')
    #return False

id = youtube_url.rsplit('/', 1)[1]
api_key = 'AIzaSyC7MRHUqlvGMYEDWZyRxR5mmkjsr1GusXk'
url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={id}&key={api_key}'

#id = youtube_url.rsplit('/', 1)[1]
#url = 'http://gdata.youtube.com/feeds/api/videos/%s?alt=json&v=2' % id
header = {'USER-AGENT': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
request = Request(youtube_url, headers=header)
#json = simplejson.load(urllib.request.urlopen(request))
json = requests.get(url).json()
#print(json)

#title = json['entry']['title']['$t']
title = json['items'][0]['snippet']['title']

youtube = pytube.YouTube(youtube_url)
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
print(title)

#author = json['entry']['author'][0]['name']

#print("id:%s\nauthor:%s\ntitle:%s" % (id, author, title))
