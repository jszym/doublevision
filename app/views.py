from app import app
from flask import request
import os, sys, random
# doublevision helper dependencies
import video_dl, extract_frames, recognise

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

    frames = extract_frames.extract("{}.mp4".format(ytid), 1000)

    # Recognise objects in images

    total_tags = {}

    for frame_path in frames:
        tags = recognise.get_tensor_tags(frame_path)
        total_tags.update(tags)

    # Return top recognised keys

    sorted_tag_keys = sorted(total_tags, reverse = True)

    top_tag = total_tags[sorted_tag_keys[0]]

    runid = random.randint(0,100) #just to show that page updated
    return "1. {} runid:{}".format(top_tag,runid)
