import os,sys
import datetime
from moviepy.editor import ImageClip,AudioFileClip,concatenate_audioclips,vfx
from moviepy.editor import concatenate_videoclips,VideoFileClip,CompositeVideoClip

'''
Still in progress, working on adding a overlay such as snow or rain or leaves.
Effects performance in a bad way, not recommended.
'''
class VideoGenerator:
    def __init__(self,args) -> None:
        if args[1] == '-h':
            self.ManualPage()
        self.img = args[1]
        self.music_link = args[2]
        self.aud_mode = args[3]
        print("AUD_MODE:",self.aud_mode)
        self.curnt_dir = os.getcwd()

        self.overlay = VideoFileClip(r"C:\Users\saisr\Downloads\leaves_diagonal_right_fast.mp4").subclip()

        try:
            self.fxParameters = [float(args[4]),float(args[5]),float(args[6])]
        except(IndexError):
            self.fxParameters = [2.0,8.0,0.20]
        
        s = str(datetime.datetime.now()).replace(' ','__')
        s = s.replace(':','-')
        self.prsnt_date = s.replace(".","-")

    def MusicDownloader(self):
        os.chdir("downloaded_music")
        os.system(f"mkdir {self.prsnt_date}")
        os.chdir(f"{self.prsnt_date}")
        os.system(f"spotdl {self.music_link}")
        
        music_list = os.listdir(os.getcwd())
        
        music_obj_list = []
        for i in music_list:
            temp = AudioFileClip(i)
            music_obj_list.append(temp)
        audio = concatenate_audioclips(music_obj_list)
        os.chdir(self.curnt_dir)

        return audio
    
    def VideoCreator(self):

        if self.aud_mode == '-s':
            audio = self.MusicDownloader()
        elif(self.aud_mode == '-c'):
            audio = AudioFileClip(self.music_link)
        elif(self.aud_mode == '-c-short'):
            audio = AudioFileClip(self.music_link)
            multiplier = int(input("Enter the no. of times lenhth is to be increased:"))
            audio = concatenate_audioclips([audio]*multiplier)
        elif(self.aud_mode == '-s-short'):
            os.chdir("downloaded_music")
            os.system(f"mkdir {self.prsnt_date}")
            os.chdir(f"{self.prsnt_date}")
            os.system(f"spotdl {self.music_link}")
            file_name = os.listdir(os.getcwd())[0]
            print(f"THE AUDIO NAME:{file_name}")
            aud_obj = AudioFileClip(file_name)
            # aud_obj.write_audiofile("output.mp3")
            n = int(input("Enter no. time to multiply the audio:"))
            audio = concatenate_audioclips([aud_obj]*n)
            os.chdir(self.curnt_dir)
        elif(self.aud_mode == '-sample'):
            self.SampleCreator()
            
        thumbnail = ImageClip(self.img)
        thumbnail = thumbnail.resize((1920,1080))
        thumbnail = thumbnail.set_duration(10) 
        # thumbnail = thumbnail.set_audio(audio)
        thumbnail = thumbnail.fx(vfx.colorx, self.fxParameters[0])

        Outro = VideoFileClip("D:\Projects\AutoEdit\Music_stuff\Thumbnails\Ooutro.mp4").resize(thumbnail.size)
        # Outro = Outro.resize((1536,864))
        self.overlay = self.overlay.set_opacity(self.fxParameters[2])
        self.overlay = self.overlay.fx(vfx.colorx, self.fxParameters[1])
        self.overlay = self.overlay.resize(thumbnail.size)
        self.overlay = self.overlay.set_duration(10)

        thumbnail = CompositeVideoClip([thumbnail,self.overlay])

        audDuration = audio.duration

        extraSeconds = audDuration%60

        totalMinuts = int((audDuration-extraSeconds)/60)

        
        tempExtraSecondsClip = thumbnail.set_duration(extraSeconds)
        thumbnail = concatenate_videoclips([thumbnail]*(int(totalMinuts)*6))
        thumbnail = concatenate_videoclips([thumbnail,tempExtraSecondsClip])
        thumbnail = thumbnail.set_audio(audio)
        # print("-------------------------",thumbnail.duration)
        # print("---------------------------",audio.duration)
        combined = concatenate_videoclips([thumbnail,Outro])
        
        final = combined.set_fps(24)
        # final = final.resize((1920,1080))
        os.chdir(f"{self.curnt_dir}\output_files")
        final.write_videofile(f"{self.prsnt_date}.mp4",codec='h264_nvenc')
    


    
    def SampleCreator(self):
        
        thumbnail = ImageClip(self.img)
        thumbnail = thumbnail.resize((1920,1080))
        thumbnail = thumbnail.set_duration(5) 
        thumbnail = thumbnail.fx(vfx.colorx, self.fxParameters[0])
        
        self.overlay = self.overlay.set_opacity(self.fxParameters[2])
        self.overlay = self.overlay.set_duration(thumbnail.duration)
        self.overlay = self.overlay.resize(thumbnail.size)
        self.overlay = self.overlay.fx(vfx.colorx, self.fxParameters[1])

        sample = CompositeVideoClip([thumbnail,self.overlay])
        sample = sample.set_fps(24)
        # sample = sample.resize((1920,1080))
        
        os.chdir(f"{self.curnt_dir}\samples")
        sample.write_videofile("sample.mp4",codec='h264_nvenc')
        print("Sample Generated...!!!")
        t = input("Continue creation?(Y/N):")
        if(t == 'Y' or t == 'y'):
            self.aud_mode = input("Enter audio mode:")
            self.VideoCreator()
        else:
            print("Enter new parameters:")
            self.fxParameters = [float(x) for x in input().split()]
            self.SampleCreator()
            
    def ManualPage():
        pass

gen = VideoGenerator(sys.argv)
gen.VideoCreator()