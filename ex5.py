import os
import sys

source = sys.argv[1]
operation = sys.argv[2]
command = ""


if operation[:3] == "cut":
    command = "ffmpeg -i {} -ss 00:00:{} -t 00:00:{} {}cut{}".format(source, operation[3:5], operation[5:], source[:-4],source[-4:])
    os.system(command)

elif operation == "histogram":
    command = 'ffmpeg -i {} -vf "split=2[a][b],[b]histogram[hh],[a][hh]overlay" {}_histogram{}'.format(source,source[:-4], source[-4:])
    os.system(command)

elif operation == "mono":
    command = "ffmpeg -i {} -ac 1 {}_mono{}".format(source, source[:-4], source[-4:])
    os.system(command)

elif operation == "aac":
    command = "ffmpeg -i {} -c:v copy -c:a libfdk_aac -vbr 3 {}_aac{}".format(source, source[:-4], source[-4:])
    os.system(command)

elif operation[:6] == "resize":
    command = "ffmpeg -i {} -vf scale={} {}_{}{}".format(source, operation[-7:], source[:-4], operation[-7:], source[-4:])
    os.system(command)

elif operation == "parse":
    command = "ffprobe -v error -show_entries format=duration:stream=codec_name -of default=noprint_wrappers=1:nokey=1 {}".format(source);
    os.system(command)

elif operation[:5] == "codec":
    command = "ffmpeg -i {} -c:v {} {}_{}{}".format(source, operation[5:], source[:-4], operation[5:], source[-4:])
    os.system(command)

else:
    print("Invalid operation requested")
