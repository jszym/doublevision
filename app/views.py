from app import app
from flask import request
import os, sys
# doublevision helper dependencies
import video_dl, extract_frames

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

'''
Take an identifier argument (either url or ytid) and download
a video based on that identifier.
'''
@app.route('/analyse.vid')
def analyse_vid():

    # Download the video...
    ytid = request.args.get('ytid') # youtube id (as in the 123 in ?v=123)
    url = request.args.get('url') # youtube url (as in https://youtube...)

    if ytid:
        video_dl.by_ytid(ytid) # download the video by id, will save as "ytid".mp4
    elif url:
        ytid = video_dl.by_url(url) # download by url
    else:
        return "No Download Parameters." # crash and burn if no id/url supplied

    # Extract frames

    extract_frames.extract("{}.mp4".format(ytid), 500)

    return "Success"
