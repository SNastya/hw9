import subprocess
import os
import soundfile as sf
from pydub import AudioSegment



def speed_up(path_audio:str, value:int):
    subprocess.call(['ffmpeg', '-i' , path_audio, '-filter:a', 'atempo='+ str(value), 'out.wav'])
    data, fs = sf.read('out.wav')
    sound = AudioSegment.from_file(path_audio)
    sound.export('outwav.wav', format="wav")
    sf.write('outwav.wav', data, fs)
    sound = AudioSegment.from_file('outwav.wav')
    sound.export(path_audio, format="mp3")
    os.remove("out.wav")
    os.remove("outwav.wav")

def speed_down(path_audio:str, value:int):
    subprocess.call(['ffmpeg', '-i' , path_audio, '-filter:a', 'atempo='+ str(value**(-1)), 'out.wav'])
    data, fs = sf.read('out.wav')
    sound = AudioSegment.from_file(path_audio)
    sound.export('outwav.wav', format="wav")
    sf.write('outwav.wav', data, fs)
    sound = AudioSegment.from_file('outwav.wav')
    sound.export(path_audio, format="mp3")
    os.remove("out.wav")
    os.remove("outwav.wav")

def booster(path_audio:str, value:int):
    out_path = 'out1.mp3'
    subprocess.call(['ffmpeg', '-i',  path_audio, '-filter:a',  'asetrate=44100*' + str(value), '-ar', '44100', out_path])
    speed_down(out_path, value)
    sound1 = AudioSegment.from_file(out_path)
    sound1.export('outwav.wav', format="wav")
    sound2 = AudioSegment.from_file(path_audio)
    sound2.export('pathwav.wav', format="wav")
    data, fs = sf.read('outwav.wav')
    sf.write('pathwav.wav', data, fs)
    sound = AudioSegment.from_file('pathwav.wav')
    sound.export(path_audio, format="mp3")
    os.remove(out_path)
    os.remove("outwav.wav")
    os.remove("pathwav.wav")



def lower(path_audio:str, value:int):
    out_path = 'out1.mp3'
    subprocess.call(['ffmpeg', '-i',  path_audio, '-filter:a',  'asetrate=44100*' + str(value**(-1)),'-ar', '44100', out_path])
    speed_up(out_path, value)
    sound1 = AudioSegment.from_file(out_path)
    sound1.export('outwav.wav', format="wav")
    sound2 = AudioSegment.from_file(path_audio)
    sound2.export('pathwav.wav', format="wav")
    data, fs = sf.read('outwav.wav')
    sf.write('pathwav.wav', data, fs)
    sound = AudioSegment.from_file('pathwav.wav')
    sound.export(path_audio, format="mp3")
    os.remove(out_path)
    os.remove("outwav.wav")
    os.remove("pathwav.wav")


