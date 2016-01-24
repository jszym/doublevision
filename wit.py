#!/usr/bin/env python3

def recognizeText(audioFile):
	import speech_recognition as sr

	WAV_FILE = audioFile

	r = sr.Recognizer()
	with sr.WavFile(WAV_FILE) as source:
    		audio = r.record(source) # read the entire WAV file

	# recognize speech using Wit.ai
	WIT_AI_KEY = "AUIRKP74ZOKPLLHQDE4VKMGT25BN54U5" # Wit.ai keys are 32-character uppercase alphanumeric strings
	try:
    		transText = r.recognize_wit(audio, key=WIT_AI_KEY)
    		print("Wit.ai thinks you said " + transText)
	except sr.UnknownValueError:
    		print("Wit.ai could not understand audio")
	except sr.RequestError as e:
    		print("Could not request results from Wit.ai service; {0}".format(e))
	return

#Test call. Remove when ready to use recognizeText
recognizeText("test.wav")
