#Writeup by Korvex (aka Bitraven, Bitravens)


#importing the necessary libraries
from PIL import Image
import numpy as np

#Since the images seem to interact with one another, I've tried multiple merging methods, and xor seemed to work best
#We'll be xoring all possible combination of the gif's frames
def xor_frames(gif_path):
    with Image.open(gif_path) as img:
        frames = []
        
        #storint the frames in an array
        for i in range(img.n_frames):
            img.seek(i)
            frame = np.array(img.convert("RGB"))  
            frames.append(frame)
        #XORing the frames two by two and saving them in a folder
        for i in range(0,len(frames)-1):
            for j in range(i+1,len(frames)):
                xor_result = np.bitwise_xor(frames[i], frames[j])
                xor_image = Image.fromarray(np.uint8(xor_result))
                xor_image.save(f"output/frame_{i}_{j}.png")

xor_frames('tv.gif')

#upon inspecting the hundreds of pictures in the output folder, one will contain a face and the flag
