# automatic-video-editor
A simple Terminal based application that takes a image and audio file/spotify playlist link and outputs a video of desired length in mp4 format.

The output file is saved in mp3 form and the length of the video is equal to the length of mp3 file or the spotify playlist.

The output file is saved in mp3 form and the length of the video is equal to the length of mp3 file
or the spotify playlist.

IMPORTANT:
To use this tool for you need to have the following modules/library installed in your system.
- Moviepy - `pip install moviepy`
- SpotDL  - `pip install spotdl`

## How to use.
- To run the script use CMD or Windows Power shell
<br>`> python AutoEditor.py [path to local image] [link to music(spotify)/path to local mp3 file.] [OPTIONS]`</br>
- To clean the previously used files from *output_files* folder and *downloaded_music* folder.
<br>`> python cleaner.py`</br>

### Options
- `-spot`   [Spotify]           : Directly download the music and attach the image.
- `-custom` [Custom/local mp3]  : Use a local music file.
- `-s-short` [Spotify Short]     : A short or single music link that can be multiplied. **Note: Still in progress**
- `-c-short` [Custom Short]      : A Custom or short local music path that can be multiplied.

