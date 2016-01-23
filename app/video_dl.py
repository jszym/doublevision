from __future__ import unicode_literals
import youtube_dl

'''
Downloads a video by it's url.
The file is saved as it's id with the mp4 extension

:param: url     the url of the video to be dowloaded
:output: None
'''
def by_url(url):

    ydl_opts = {

        "outtmpl": "%(id)s.%(ext)s"

    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return None

'''
Downloads a video by it's ytid.
The file is saved as it's id with the mp4 extension.

:param: ytid     the youtube id of the video to be dowloaded
:output: None
'''
def by_ytid(ytid):

    ydl_opts = {

        "outtmpl": "%(id)s.%(ext)s"

    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(["https://youtube.com/watch?v={}".format(ytid)])

    return None
