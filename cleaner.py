import time
import os,sys

class dirCleaner:
    def __init__(self) -> None:
        self.crunt_dir = os.getcwd()
    def Cleaner(self):
        os.chdir("D:\Projects\AutoEdit\Music_stuff")
        print("Cleaner: Moving to 'downloaded_music' folder")
        time.sleep(1.0)
        os.chdir("D:\Projects\AutoEdit\Music_stuff\downloaded_music")
        lis = os.listdir()
        print(lis)
        print("Files Found:")
        for i in lis:
            print(i)
        print("Cleaner: Deleting above files")
        for i in lis:
            os.system(f"del {i}")
        print("Cleaner: downloaded_music files deleted.")

        os.chdir("D:\Projects\AutoEdit\Music_stuff\output_files")
        lis = os.listdir()
        print("Cleaner: Files Found_")
        for i in lis:
            print(i)
        print("Cleaner: Deleting above files")
        for i in lis:
            os.system(f"del {i}")
        print("Cleaner: output_files files deleted.")



ob = dirCleaner()
ob.Cleaner()