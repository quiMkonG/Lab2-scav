import os
import sys

source = sys.argv[1]
codec = sys.argv[2]

command = "ffmpeg -i {} -c:v {} {}_{}{}".format(source, codec, source[:-4], codec, source[-4:])

os.system(command)
