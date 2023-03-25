

import os
import shutil
from datetime import datetime, timedelta

# Get the path for the downloads folder
downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')

# Get the path for the Documents folder
documents_dir = os.path.join(os.path.expanduser('~'), 'Documents')

# Get the current time
now = datetime.now()

# Iterate over all the files in the downloads directory
for filename in os.listdir(downloads_dir):
    # Get the full path of the file
    file_path = os.path.join(downloads_dir, filename)

    # Get the modification time of the file
    modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))

    # Calculate the time difference
    time_difference = now - modified_time

    # Check if the time difference is greater than 30 days
    if time_difference.days > 30:
        # Move the file to the Documents folder
        shutil.move(file_path, documents_dir)