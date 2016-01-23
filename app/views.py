from app import app
import video_dl
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

'''
Take an identifier argument (either url or ytid) and download
a video based on that identifier.
'''
@app.route('/download.vid')
def download_vid():
    ytid = request.args.get('ytid')
    url = request.args.get('url')
    if ytid:
        video_dl.by_ytid(ytid)
        return "Success"
    elif url:
        video_dl.by_url(url)
        return "Success"
    else:
        return "No Download Parameters."
