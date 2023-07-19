# Auto File Organizer

Auto File Organizer is a Python script designed to automate the organization of downloaded files. It efficiently categorizes downloaded files based on their extensions into designated folders, such as videos, audios, executables, and unknown files, making it easier to manage and declutter the "Downloads" folder.

## Features

- Automatic File Organization: The script continuously monitors the "Downloads" folder and automatically moves completed downloads to their respective folders based on their file extensions.

- Real-time Notifications: Users receive desktop notifications as soon as a download is completed, providing instant updates on the status of downloaded files and their destinations.

- Intelligent File Classification: Leveraging advanced file extension handling and threading techniques, the script intelligently categorizes files, ensuring smooth and interruption-free file movements.

- User-friendly Solution: The Auto File Organizer provides a simple and intuitive solution that reduces manual file management efforts, offering an organized and clutter-free workspace.

## Requirements

- Python 3.x
- plyer library (for desktop notifications)
- watchdog library (for monitoring the "Downloads" folder)

Install the required libraries using pip:
pip install plyer watchdog

## Usage
1.Clone the repository to your local machine.
2.Navigate to the project directory:
cd Auto-File-Organizer

## Run the script:
python auto_file_organizer.py

1. The script will automatically start monitoring the "Downloads" folder for new downloads. Once a download is completed, it will be moved to its respective folder based on the file extension.
2. Desktop notifications will provide real-time updates on completed downloads and their respective destinations.

## Customization
You can modify the folder paths (VIDEO_PATH, AUDIO_PATH, EXECUTABLE_PATH, UNKNOWN_PATH) in the auto_file_organizer.py script to suit your preferred folder structure.

Adjust the time delay in the wait_for_download_completion function of the DownloadHandler class if needed to fine-tune the download completion check.

Note
The script is designed to run on Windows operating systems due to the usage of the win32file module for folder monitoring.
