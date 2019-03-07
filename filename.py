import os
directory = "audioRefrence/"
for filename in os.listdir(directory):
    if filename.endswith(".wav"): 
        file = os.path.join(filename)
        userId = os.path.splitext(file)[0]
        print userId
        continue
    else:
        continue