import sys
import os

source = sys.argv[1]

command = "ffprobe -v error -show_entries format=duration:stream=codec_name -of default=noprint_wrappers=1:nokey=1 {}".format(source);

os.system(command)
