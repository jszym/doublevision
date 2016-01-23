'''
extract_frames.py
---
Extract the frames of a video using the OpenCV library
'''
import cv2
import os

'''
Extract frames from a given video using the OpenCv library.
Adapted from http://stackoverflow.com/a/17109400

:param: vid_path    the path to the video file
:param: f_interval  the interval at which to save frames (1=all frames,
                                                          2=every other frame,etc..)
:returns: saves files in the frames folder as the vid_path+"-"+frame_num+".mp4"
'''
def extract(vid_path, f_interval):
    print f_interval
    cv = cv2.VideoCapture(vid_path)
    frame_num=1
    file_name = os.path.basename(vid_path)
    print file_name

    if cv.isOpened():
    	rval, frame = cv.read()
    else:
    	rval = False

    while rval:

    	rval, frame = cv.read()
    	if frame_num % f_interval == 0:
            file = 'frames/{}-{}.jpg'.format(file_name, frame_num)
            print file
            cv2.imwrite(file, frame)
            cv2.waitKey(1)
    	frame_num += 1
    cv.release()
