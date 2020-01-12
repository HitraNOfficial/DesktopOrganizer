import os
import time

def move_files():
    for file in os.listdir(folder_to_track):
        filename, file_extension = os.path.splitext(file)
        src = folder_to_track + "\\" + file

        print("Started work on file {} with extension {}", filename, file_extension)
        if file_extension.lower() in [".mp4", ".webm", ".mkv", ".flv", ".avi", ".wmv"]:
            new_destination = folder_destination + "\\Videos\\" + file
        elif file_extension.lower() in [".mp3", ".wav", ".ogg", ".m4a"]:
            new_destination = folder_destination + "\\Music\\" + file
        elif file_extension.lower() in [".docx", ".txt", ".pub", ".pptx", ".xls", ".doc"]:
            new_destination = folder_destination + "\\Documents\\" + file
        elif file_extension.lower() in [".jpg", ".jpeg", ".gif", ".png"]:
            new_destination = folder_destination + "\\Pictures\\" + file
        else:
            new_destination = folder_destination + "\\Others\\" + file
        
        os.rename(src, new_destination)

folder_to_track = "C:\\Users\\HitraN\\Desktop"
folder_destination = "C:\\General\\ORGANIZER"
move_files()