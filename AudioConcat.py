from moviepy.editor import AudioFileClip,concatenate_audioclips
import sys,os

class AudioConcat:
    def __init__(self,args) -> None:
        self.aud_folder = args[1]
    def Concatenator(self):
        folder_name = (self.aud_folder).split("\\")
        # print(folder_name)
        os.chdir(f"D:\Projects\AutoEdit\Music_stuff\downloaded_music\{folder_name[-1]}")
        aud_lis = os.listdir(self.aud_folder)
        aud_obj_list = [AudioFileClip(x) for x in aud_lis]
        # print(aud_lis,os.getcwd())
        os.chdir("D:\Projects\AutoEdit\Music_stuff")
        aud = concatenate_audioclips(aud_obj_list)
        aud.write_audiofile('Concatanated.mp3')


ob = AudioConcat(sys.argv)
ob.Concatenator()
# print(os.listdir("D:\Projects\AutoEdit\Music_stuff\output_files"))