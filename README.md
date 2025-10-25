<div align="center">

# 📁 Downloads Folder Organizer

**Automatically organize your Downloads folder by sorting files into subfolders based on their file type**

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

![Downloads Organizer](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20MacOS-lightgrey)

</div>

---

Python script that automatically organizes files in your Downloads folder by sorting them into subfolders based on their file type. Uses only Python's standard library and handles duplicate files intelligently with auto-renaming. Provides detailed statistics and progress reports throughout the organization process.

<div align="center">

## ✨ Features

</div>

- 🚀 **Automatic Organization** - Sorts files into appropriate category folders based on file type
- 🔄 **Duplicate Handling** - Automatically renames duplicate files instead of overwriting them
- 📊 **Statistics Report** - Shows summary of organized files and duplicates
- 🛠️ **No Dependencies** - Uses only Python's standard library
- 💡 **Well Commented** - Easy to understand and modify
- ⚡ **Fast Processing** - Efficient file handling with progress tracking
- 🔒 **Safe Operations** - Only moves files within the Downloads folder

<div align="center">

## 📂 File Categories

</div>

The script organizes files into the following folders:

| Category | Supported Extensions |
|----------|---------------------|
| 🖼️ **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`, `.ico`, `.tiff`, `.heic` |
| 🎥 **Videos** | `.mp4`, `.avi`, `.mov`, `.mkv`, `.flv`, `.wmv`, `.webm`, `.m4v`, `.3gp` |
| 🎵 **Music** | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.wma`, `.m4a` |
| 📄 **Documents** | `.pdf`, `.doc`, `.docx`, `.txt`, `.rtf`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.csv` |
| 📦 **Archives** | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`, `.xz`, `.iso` |
| ⚙️ **Executables** | `.exe`, `.msi`, `.dmg`, `.pkg`, `.deb`, `.rpm`, `.appimage` |
| 💻 **Code** | `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`, `.c`, `.php`, `.rb`, `.go`, `.ts` |
| 🔤 **Fonts** | `.ttf`, `.otf`, `.woff`, `.woff2`, `.eot` |
| 📊 **Spreadsheets** | `.csv`, `.xlsx`, `.xls`, `.ods` |
| 📽️ **Presentations** | `.pptx`, `.ppt`, `.odp` |
| ❓ **Others** | Any file types not in the above categories |

<div align="center">

## 📋 Requirements

- **Python 3.6 or higher**
- No additional packages required (uses only standard library)

---

## 🚀 Installation

</div>

```bash
git clone https://github.com/azizbek-web-dev/Python---Organize-downloads-folder-automatically.git
cd Python---Organize-downloads-folder-automatically
```

## 📖 Usage

```bash
python organize_downloads.py
```

### Custom Path

To organize a different folder, modify the script and pass a custom path:

```python
organizer = DownloadsOrganizer(downloads_path="C:/Users/YourName/Desktop/MyFolder")
organizer.organize_files()
```

---

<div align="center">

## 📊 Example Output

</div>



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

---

<div align="center">

## 🔧 How It Works

</div>

The script scans your Downloads folder, identifies file types by extension, sorts files into category folders, and handles duplicates by adding number suffixes. A summary report is displayed at the end showing total files organized, duplicates renamed, and any errors encountered.

<div align="center">

## 🔒 Safety Features

</div>

- **Safe Operations** - Only moves files within the Downloads folder
- **No Data Loss** - Duplicate files are renamed instead of overwriting
- **Error Handling** - Graceful handling of files that cannot be moved
- **Structure Preserved** - Maintains Downloads folder structure

<div align="center">

## ⚙️ Customization

</div>

To customize the script, modify the `FILE_CATEGORIES` dictionary in `organize_downloads.py`:

```python
FILE_CATEGORIES = {
    'images': ['.jpg', '.jpeg', '.png', '.your-extension'],
    'your-category': ['.ext1', '.ext2'],
}
```

---

<div align="center">

## 📝 Notes

</div>

- The script only organizes files in the Downloads folder root directory, not subdirectories
- Existing files in category folders are not overwritten - duplicates are automatically renamed
- You can run the script as often as you want to keep your Downloads folder organized

---

<div align="center">

## 🎯 Tech Stack

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=306998)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Made with ❤️ for organized Downloads folders**

</div>
