from playsound import*
path="sound\\"
def play(n,blocking=False):
    file=(path+n+'.mp3')
    playsound(file,block=blocking)
