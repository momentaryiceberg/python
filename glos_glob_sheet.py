import glob

# Basic patterns
files = glob.glob('path/to/files/*.txt')
print("Files in the directory:", files)

# Recursive search
all_files = glob.glob('path/to/files/**/*.txt', recursive=True)
print("All files (including subdirectories):", all_files)

# Wildcard characters
txt_files = glob.glob('path/to/files/*.txt')
print("Text files:", txt_files)

# Character ranges
jpg_files = glob.glob('path/to/files/*.[jJ][pP][gG]')
print("JPG files:", jpg_files)

# Single character wildcard
txt_or_log_files = glob.glob('path/to/files/*.{txt,log}')
print("Text or log files:", txt_or_log_files)

# Braces for multiple patterns
image_files = glob.glob('path/to/files/*.{jpg,jpeg,png}')
print("Image files:", image_files)

# Get files starting with a specific prefix
prefix_files = glob.glob('path/to/files/prefix*')
print("Files with a specific prefix:", prefix_files)

# Get files with a specific extension
extension_files = glob.glob('path/to/files/*.extension')
print("Files with a specific extension:", extension_files)

# Get all files in the current directory
all_files_current_dir = glob.glob('*')
print("All files in the current directory:", all_files_current_dir)

# Get all files with a specific extension in any subdirectory
all_python_files = glob.glob('**/*.py', recursive=True)
print("All Python files in any subdirectory:", all_python_files)

# Find files using a complex pattern
complex_pattern_files = glob.glob('path/to/files/[0-9][0-9][0-9]/*.txt')
print("Files matching a complex pattern:", complex_pattern_files)

# Exclude files with a specific pattern
exclude_pattern_files = glob.glob('path/to/files/*.txt', exclude='path/to/files/exclude*.txt')
print("Files excluding a specific pattern:", exclude_pattern_files)

# Retrieve directories only
directories_only = glob.glob('path/to/files/*/', recursive=True)
print("Directories only:", directories_only)

# Use case-insensitive matching
case_insensitive_files = glob.glob('path/to/files/*.TXT', flags=glob.IGNORECASE)
print("Case-insensitive matching:", case_insensitive_files)

# Get files modified within a specific time range
import os
import time
now = time.time()
one_day_ago = now - (24 * 3600)
recently_modified_files = [f for f in glob.glob('path/to/files/*') if os.path.getmtime(f) > one_day_ago]
print("Recently modified files:", recently_modified_files)
