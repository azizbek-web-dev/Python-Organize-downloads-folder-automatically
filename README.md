# Downloads Folder Organizer

Python script that automatically organizes files in your Downloads folder by sorting them into subfolders based on their file type. Uses only Python's standard library and handles duplicate files intelligently.

## Features

- Automatic organization into categories
- Duplicate file handling with auto-renaming
- Statistics summary after organization
- No external dependencies required
- Well-commented code for easy modification

## File Categories

Files are organized into the following folders:

- Images: jpg, jpeg, png, gif, bmp, svg, webp, ico, tiff, heic
- Videos: mp4, avi, mov, mkv, flv, wmv, webm, m4v, 3gp
- Music: mp3, wav, flac, aac, ogg, wma, m4a
- Documents: pdf, doc, docx, txt, rtf, xls, xlsx, ppt, pptx, csv
- Archives: zip, rar, 7z, tar, gz, bz2, xz, iso
- Executables: exe, msi, dmg, pkg, deb, rpm, appimage
- Code: py, js, html, css, java, cpp, c, php, rb, go, ts
- Fonts: ttf, otf, woff, woff2, eot
- Spreadsheets: csv, xlsx, xls, ods
- Presentations: pptx, ppt, odp
- Others: Any file types not in the above categories

## Requirements

- Python 3.6 or higher
- No additional packages required (uses only standard library)

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/azizbek-web-dev/Python---Organize-downloads-folder-automatically.git
cd Python---Organize-downloads-folder-automatically
```

No additional installation required. Just run the script with Python.

## Usage

Run the script to organize your Downloads folder:

```bash
python organize_downloads.py
```

To organize a different folder, modify the script and pass a custom path:

```python
organizer = DownloadsOrganizer(downloads_path="C:/Users/YourName/Desktop/MyFolder")
organizer.organize_files()
```

## Example Output

```
============================================================
Downloads Folder Organizer
============================================================

Organizing files in: C:\Users\YourName\Downloads
------------------------------------------------------------
document.pdf -> documents/document.pdf
image.jpg -> images/image.jpg
video.mp4 -> videos/video.mp4
Renamed duplicate: document.pdf -> document_1.pdf
------------------------------------------------------------
Organization Summary:
  Total files found: 25
  Files organized: 25
  Duplicates renamed: 3
  Errors: 0

Your Downloads folder is now organized.
```

## How It Works

The script scans your Downloads folder, identifies file types by extension, sorts files into category folders, and handles duplicates by adding number suffixes. A summary report is displayed at the end.

## Safety Features

- Only moves files within the Downloads folder
- Handles duplicates by adding number suffixes
- Error handling for files that cannot be moved
- Preserves the Downloads folder structure

## Customization

To customize the script:

1. Add more file categories by modifying the FILE_CATEGORIES dictionary
2. Change folder names by updating the dictionary keys
3. Add more file types to the appropriate category list

Example:
```python
FILE_CATEGORIES = {
    'images': ['.jpg', '.jpeg', '.png', '.your-extension'],
    'your-category': ['.ext1', '.ext2'],
}
```

## Notes

The script only organizes files in the Downloads folder root directory, not subdirectories. Existing files in category folders are not overwritten - duplicates are automatically renamed. You can run the script as often as you want to keep your Downloads folder organized.
