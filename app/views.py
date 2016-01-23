from app import app
from flask import request
import os, sys, random, json
# doublevision helper dependencies
import video_dl, extract_frames, recognise, context

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
        ytid = video_dl.by_url(url) # download by url, ytid returned and stored
    else:
        return "No Download Parameters." # crash and burn if no id/url supplied

    cachefile = "cache/{}.cache".format(ytid)

    if os.path.isfile(cachefile):
        top_tag_dump = ""
        with open(cachefile) as f:
            top_tag_dump = f.read()
        top_tag = json.loads(top_tag_dump)
    else:
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

        print top_tag

        top_tag_serialize = json.dumps(top_tag)

        with open(cachefile, "w") as f:
            f.write(top_tag_serialize)

    result = {}
    for tag in top_tag:
        tag = tag.strip()
        result[tag] = context.tag_info(tag)

    result_serialize = json.dumps(result)


    return result_serialize
