# Python - Organize Downloads Folder Automatically

Automatically organize your Downloads folder by sorting files into subfolders based on their file type. This script uses only Python's standard library and handles duplicate files intelligently.

## Features

- 📁 **Automatic Organization**: Sorts files into categories (images, videos, music, documents, etc.)
- 🔄 **Duplicate Handling**: Automatically renames duplicate files instead of overwriting them
- 📊 **Statistics**: Shows a summary of organized files and duplicates
- 🛠️ **No Dependencies**: Uses only Python's standard library
- 🎯 **Well Commented**: Easy to understand and modify

## File Categories

The script organizes files into the following categories:

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`, `.ico`, `.tiff`, `.heic`
- **Videos**: `.mp4`, `.avi`, `.mov`, `.mkv`, `.flv`, `.wmv`, `.webm`, `.m4v`, `.3gp`
- **Music**: `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.wma`, `.m4a`
- **Documents**: `.pdf`, `.doc`, `.docx`, `.txt`, `.rtf`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.csv`
- **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`, `.xz`, `.iso`
- **Executables**: `.exe`, `.msi`, `.dmg`, `.pkg`, `.deb`, `.rpm`, `.appimage`
- **Code**: `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`, `.c`, `.php`, `.rb`, `.go`, `.ts`
- **Fonts**: `.ttf`, `.otf`, `.woff`, `.woff2`, `.eot`
- **Spreadsheets**: `.csv`, `.xlsx`, `.xls`, `.ods`
- **Presentations**: `.pptx`, `.ppt`, `.odp`
- **Others**: Any file types not in the above categories

## Requirements

- Python 3.6 or higher
- No additional packages required (uses only standard library)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/azizbek-web-dev/Python---Organize-downloads-folder-automatically.git
cd Python---Organize-downloads-folder-automatically
```

2. No additional installation needed! Just run the script.

## Usage

### Basic Usage

Simply run the script to organize your Downloads folder:

```bash
python organize_downloads.py
```

### Custom Path

You can also modify the script to organize a different folder by passing a custom path:

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
✓ document.pdf -> documents/document.pdf
✓ image.jpg -> images/image.jpg
✓ video.mp4 -> videos/video.mp4
Renamed duplicate: document.pdf -> document_1.pdf
------------------------------------------------------------
Organization Summary:
  Total files found: 25
  Files organized: 25
  Duplicates renamed: 3
  Errors: 0

Your Downloads folder is now organized! 🎉
```

## How It Works

1. The script scans your Downloads folder for all files
2. It identifies each file's type based on its extension
3. Files are sorted into appropriate category folders
4. If a file with the same name already exists in the destination folder, it's renamed with a number suffix (e.g., `file_1.pdf`)
5. A summary report is displayed at the end

## Safety Features

- Only moves files within the Downloads folder (doesn't delete anything)
- Handles duplicates intelligently by adding number suffixes
- Error handling for files that cannot be moved
- Preserves the original Downloads folder structure

## Customization

You can easily customize the script by:

1. **Adding more file categories**: Modify the `FILE_CATEGORIES` dictionary
2. **Changing folder names**: Update the category names in the dictionary keys
3. **Adding more file types**: Add extensions to the appropriate category list

Example:
```python
FILE_CATEGORIES = {
    'images': ['.jpg', '.jpeg', '.png', '.your-extension'],
    'your-category': ['.ext1', '.ext2'],
}
```

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available for personal use.

## Author

Created for organizing downloads folders efficiently and automatically.

## Notes

- The script only organizes files in the Downloads folder, not subdirectories
- Existing files in category folders are not overwritten (duplicates are renamed)
- Run the script as often as you want to keep your Downloads folder organized
