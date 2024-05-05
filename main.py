import os

# Path to the folder containing video files
folder_path = "E:\STUDY\React\code with harry"

# Get a list of all video files in the folder
video_files = [file for file in os.listdir(folder_path) if file.endswith(".mp4")]

# Sort the video files based on the number in their names
sorted_video_files = sorted(video_files, key=lambda x: int(x.split("#")[-1].split(".")[0]))

# Rename the video files sequentially
for i, file_name in enumerate(sorted_video_files, start=1):
    # Construct the new file name
    new_file_name = f"video_{i}.mp4"
    
    # Rename the file
    os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
    
    print(f"Renamed {file_name} to {new_file_name}")

print("All video files have been renamed.")
