import time
import os,sys,os.path

class dirCleaner:
    def __init__(self) -> None:
        self.crunt_dir = os.getcwd()
    def Cleaner(self):
        print("Cleaner: Moving to 'downloaded_music' folder")
        time.sleep(1)
        os.chdir("D:\Projects\AutoEdit\Music_stuff\downloaded_music")
        lis = os.listdir()
        # print(lis)
        print("Files Found:")
        time.sleep(1)
        for i in lis:
            print(i)
        print("Cleaner: Deleting above files")
        time.sleep(1)
        for i in lis:
            os.system(f"rmdir {i} /s /q")
        print("Cleaner: downloaded_music files deleted.")
        time.sleep(1)
        print("Moving to the /output_files")
        time.sleep(1)
        os.chdir("D:\Projects\AutoEdit\Music_stuff\output_files")
        lis = os.listdir()
        print("Cleaner: Files Found_")
        time.sleep(1)
        for i in lis:
            print(i)
        print("Cleaner: Deleting above files")
        time.sleep(1)
        for i in lis:
            os.system(f"del {i}")
        print("Cleaner: output_files files deleted.")
        time.sleep(1)
        print("FULL CLEAN SUCCESSFUL")



ob = dirCleaner()
ob.Cleaner()