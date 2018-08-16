import subprocess
import sys

def main():
	url = sys.argv[1]
	print("downloading %s..." % url)
	if url:
		cmd = [
			"youtube-dl", 
			"-o",
			"./songs/%(title)s.%(ext)s",
			"--extract-audio", 
			"--audio-format",
			"mp3",
			url			
		]
		subprocess.Popen(cmd).wait()
			# (, shell=True)

if __name__ == "__main__":
  main()