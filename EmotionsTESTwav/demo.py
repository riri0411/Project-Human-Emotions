#import ffmpeg
# import ffmpy
"""
print("Am importat un pachet care trateaza conversii de fisiere video")
clip=ffmpeg.input("clip.mp4")
print("Am citit fisierul .mp4")
audio=ffmpeg.output(clip,"clip.wav")
print("L-am convertit in .wav")
ffmpeg.run(audio)
print("Am salvat fisierul convertit")
"""


import os

def main():
    files = os.listdir(".")
    print (files)
    for f in files:
        #if f.lower()[-3:] == "mp4":
        if f.lower()[-3:] == "wav":
            print("Am importat un pachet care trateaza conversii de fisiere video")
            print ("processing", f)
            process(f)

def process(f):
    inFile = f
    #outFile = f[:-3] + "wav"
    outFile = f[:-3] + "png"
    #cmd = "ffmpeg -i {} -vn  -ac 2 -ar 44100 -ab 320k -f mp3 {}".format(inFile, outFile)
    #cmd = "ffmpeg -i {} -vn  -ac 2 -ar 44100 -ab 160k -f wav {}".format(inFile, outFile)
    #cmd  = 'ffmpeg.exe -i "clip.wav" -lavfi showwavespic=split_channels=1:s=1024x800 waveform.png'
    #cmd = "sox clip.wav -n spectrogram"
    #cmd = "sox clip.wav -n spectrogram -y 130 -l -r -o ${clip.wav}.png"
    cmd="sox "+inFile+" "+inFile+"_mono.wav remix − && sox "+inFile+"_mono.wav -n spectrogram -r -o "+outFile+" && del "+inFile+"_mono.wav";
    #command = "ffmpeg -i C:/test.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav"
    os.popen(cmd)

main()
