# voice_authentication_python
Simple voice authentication using matplotlib, dtw, pyaudio and google firebase(work in progress).
This uses matplotlib.pyplot to plot the two audio files spectrum the using dtw libary which 
stands for Dynamic Time Warping. This then caculates the distance between the two plots of the audio files.


## Setup

```shell
$ git clone https://github.com/greallye/voice_authentication_python.git
$ cd voice_authentication_python
```

Now we need to creat the folder to store audio files for users
```shell
$ mkdir audioRefrence
```
createv virtualenv to install all the libaries if you do not have virtualenv (pip install virtualenv)
```shell
$ virtualenv voiceauth
```
Then activate it
```shell
$ source voiceauth/bin/activate
```

Lets install all the libaries(will create a setup later when this project is further developed)
```shell
$ pip install pyaudio
$ pip install wave
$ pip install librosa
$ pip install matplotlib 
$ pip install dtw
```
Open the enrol.py 
update the config with firebase credntials
Open the okVoice.py
update the config with firebase credntials

In enrol.py change "Test Name" to the name you want to enrol.

First run the enrol.py 

```shell
$ enrol.py
```

Once the console says Recording say a phrase you want to test again. 
You have 5 seconds.

Once recorded

```shell
$ okVoice.py
```

This will say recording again Say the same phrase that you enrolled with. 
It should return the name you enrolled with if it is a match. 
Record multiple people and test it out.

# Enjoy

