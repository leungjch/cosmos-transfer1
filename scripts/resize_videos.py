import os
from moviepy.editor import VideoFileClip

input_dir = '/home/data/datasets/cosmos-posttrain-av/videos_large'
output_dir = '/home/data/datasets/cosmos-posttrain-av/videos'
target_resolution = (1280, 704)

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate over all files in the input directory
for filename in os.listdir(input_dir):
    input_path = os.path.join(input_dir, filename)
    
    # Check if the file is a video by simple extension check
    if filename.endswith(('.mp4', '.avi', '.mov', '.mkv')):
        output_path = os.path.join(output_dir, filename)
        
        # Load the video file
        clip = VideoFileClip(input_path)
        
        # Resize the video
        resized_clip = clip.resize(newsize=target_resolution)
        
        # Write the resized video to the output directory
        resized_clip.write_videofile(output_path)

print("All videos have been resized and saved to the 'videos' directory.")