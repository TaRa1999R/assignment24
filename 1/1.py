
import time
from  moviepy import editor

video = editor.VideoFileClip("1\Metele_zumba.mp4")
video.audio.write_audiofile ("1\Metele_zumba.mp3")