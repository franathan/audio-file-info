# audio-file-info

Quickly get the sample rate and bit-depth from numerous audio file types. This is built off of the python package
[SoundFile](https://github.com/bastibe/python-soundfile).


## Installation

1) Download the file `audio_info.py`.
2) Open Terminal. Run `which python`. Your output should be something similar to `/usr/bin/python3`.
3) Paste this result into audio_file.py after the hashbang, so it looks like this: `#!/usr/bin/python3`.
4) Add the path to `audio_info.py` to your `$path` environmental variable. Simply add the line
   `export PATH="$PATH:<PATH_TO_FOLDER_WITH_AUDIO_INFO.py>"` to your `.zshrc` file.

## Usage

Since the file location has been added to your `$path` variable, usage is quite easy. Open terminal and run `audio_info.py`.
This command can be run from any location, so you do not need to be in the directory the file is saved in. Paste
the absolute path of the audio file, or a folder that contains multiple audio files.
```angular2html
➜  ~ audio_info.py
Please paste path to file or directory, or [q]uit: ~/Music/Hi Res Audio/Random Access Memories (2013)/Give Live Back To Music.flac
samplerate: 96000 Hz
channels: 2
duration: 04:33.451 min
format: FLAC (Free Lossless Audio Codec) [FLAC]
subtype: Signed 24 bit PCM [PCM_24]
Please paste path to file or directory, or [q]uit:
```
Currently, this cannot handle `.mp3` extensions as the file format was once patented. This does not search folders within folders (recursive folders). 
