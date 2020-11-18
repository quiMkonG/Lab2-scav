import sys
import os

source = sys.argv[1];
resize = sys.argv[2];

command = "ffmpeg -i {} -vf scale={} {}_{}{}".format(source, resize, source[:-4], resize, source[-4:])

os.system(command)
