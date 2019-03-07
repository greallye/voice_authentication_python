import librosa

import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import librosa.display
from dtw import dtw
from numpy.linalg import norm

import pyrebase
import os

directory = "audioRefrence/"

from soundrecording import *
# from enrol import *
startRecording()


config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

all_users = db.child("users").get()

for filename in os.listdir(directory):
    i = 0
    if filename.endswith(".wav"): 
        file = os.path.join(filename)
        stringFile = str(file);
        y1, sr1 = librosa.load('1.wav') 
        y2, sr2 = librosa.load("audioRefrence/"+stringFile) 

        #Showing multiple plots using subplot
        plt.subplot(1, 2, 1) 
        mfcc1 = librosa.feature.mfcc(y1,sr1)   #Computing MFCC values
        librosa.display.specshow(mfcc1)

        plt.subplot(1, 2, 2)
        mfcc2 = librosa.feature.mfcc(y2, sr2)
        librosa.display.specshow(mfcc2)

        dist = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
        
        print("The normalized distance between the two : ",dist[i])
        
        if(dist[i] < 158):
            userId = os.path.splitext(file)[i]
            print userId
            print("suceess")
            for user in all_users.each():
                if(userId == user.key()):
                    print (user.key())
                    print(user.val()[u'name'])
            break
    i += 1
    
