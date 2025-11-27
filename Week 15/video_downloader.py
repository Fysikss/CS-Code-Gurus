"""
    Name: video_downloader.py
    Author: Noel Onate
    Created: 11/27/25
    Purpose: Download YouTube videos from input
"""

# Import pytube library
from pytubefix import YouTube

# Ask user to input a link
url = input("Enter YouTube URL: ")

# Create object using pytube and inputted url
yt = YouTube(url)

# Make the video the highest resolution possible
video = yt.streams.get_highest_resolution()

# Download the video for user
print(f"Downloading: {yt.title}...")
video.download()
print("Download complete!")