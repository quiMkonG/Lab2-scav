# Lab2-scav
Lab 2 from SCAV subject. UPF.

# Quim Marcé - 205523

Previous steps)

Download the BigBuckBunny(refered to as BBB from now on) video from this link: https://peach.blender.org/download/ 

In this lab we can work on the BBB file in any video format supported by ffmpeg.

All exercises are implemented in "ex5.py", a deeper explanation on how it works can be found in the end of this file.

All python scripts are aimed to be run from terminal


EXERCISE 1)

Corresponding files: ex1.py

Corresponding command: python3 ex1.py x 

Where x is the name of the input video we want to parse.

To do this part of the lab I had to look for some methods on the internet and I found one which seems pretty useful (link can be found attached at Source 1 below). Basically it uses ffprobe and "show entries" to show the selected entries generated with "ffmpeg -i file". The metadata can be chosen from either "format", "stream" or other. For example, in my case it shows the video codec and the audio codec from "stream", and the duration in sexagesimal time units from "format". More information can be found in the show_entries section in the link below.

Source 1: https://ffmpeg.org/ffprobe.html


EXERCISE 2)

This part of the lab was already implemented in the final file "s2.py" from the previous seminar, so I just recylced that part of code and implemented it directly in "ex5.py".



EXERCISE 3) 

Corresponding files: ex3.py 

Corresponding command: python3 ex3.py i AAAxBBB

Where "i" refers to the input video, AAA refers to the width of the output resized image and BBB to its height. The x in the middle is mandatory.

Basically it consists on the same as in the previous seminars/labs except for the part of making it work for different video formats, so the input format of the video has to be copied in the output file.

EXERCISE 4)

Corresponding files: ex4.py

Corresponding command: python3 ex3.py i x

Where "i" is the input video and "x" is the name of the output video codec.

A change of codec can be applied pretty easily with -c:v x, where x is again the name of the output codec.

EXERCISE 5)

Corresponding files: ex3.py 

Corresponding command: python3 ex5.py source operation

Where source is the input video and operation can take several values depending on the operation we want to apply to the input video.

Here we can found implemented all the operations corresponding to Seminar 2 and also the ones in Lab 2 working for any kind of video format.

	
	1) Video cut.
	
	Operation = cutxxyy
	
	Where xx represents the starting time in seconds where we want to start cutting and yy is 		the duration also in seconds of our cut.
	
	Outputs the cut video with the same name adding "cut" in the end. Also with the same 	format.

	2) Histogram.
	
	Operation = histogram
	
	No secret here. Outputs the video with the overlayed yuv histogram. Output conserves same 		format and same name adding "_histogram" in the end.
	
	3) Converting audio to mono.
	
	Operation: mono
	
	Already explained in Seminar 2, converts audio to mono. Outputs the video with converted 		audio, conserving video format and video name adding "_mono" in the end.

	4) Converting audio codec to AAC.
	
	Operation: aac
	
	Already explained in Seminar 2, converts audio codec to aac. Outputs the video with 	converted audio codec, conserving video format and video name adding "_aac" in the end.

	5) Resizing.
	
	Operation: resizeAAAxBBB
	
	AAA: width of the resized output. BBB: height of the resized output. "x" is mandatory.
	
	Implementation of exercise 3. 
	
	6) Printing video and audio codecs used and duration of the video in sexagesimal units.
	
	Operation: parse
	
	Implementation of exercise 1.
	
	7) Changing video codec
	
	Operation: codecX
	
	Where X can be any video codec supported by ffmpeg.
	
	Implementation of exercise 4.
	





