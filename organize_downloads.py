#!/usr/bin/env python3
"""
Downloads Folder Organizer
Automatically organizes files in the Downloads folder into subfolders by file type.
Handles duplicate files by renaming them with a number suffix.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime


class DownloadsOrganizer:
    """Organizes files in the Downloads folder by their type."""
    
    # File type mappings to folder names
    FILE_CATEGORIES = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico', '.tiff', '.heic'],
        'videos': ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm', '.m4v', '.3gp'],
        'music': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
        'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.xls', '.xlsx', '.ppt', '.pptx', '.csv'],
        'archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.iso'],
        'executables': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm', '.appimage'],
        'code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go', '.ts'],
        'fonts': ['.ttf', '.otf', '.woff', '.woff2', '.eot'],
        'spreadsheets': ['.csv', '.xlsx', '.xls', '.ods'],
        'presentations': ['.pptx', '.ppt', '.odp'],
    }
    
    def __init__(self, downloads_path=None):
        """
        Initialize the organizer.
        
        Args:
            downloads_path (str, optional): Path to Downloads folder.
                                           Defaults to user's Downloads folder.
        """
        if downloads_path is None:
            # Get the user's Downloads folder
            self.downloads_path = Path.home() / 'Downloads'
        else:
            self.downloads_path = Path(downloads_path)
        
        self.stats = {
            'total_files': 0,
            'organized': 0,
            'duplicates_renamed': 0,
            'errors': 0
        }
    
    def get_file_category(self, file_extension):
        """
        Determine which category a file belongs to based on its extension.
        
        Args:
            file_extension (str): File extension including the dot (e.g., '.pdf')
        
        Returns:
            str: Category name or 'others' if no match found
        """
        file_extension = file_extension.lower()
        
        for category, extensions in self.FILE_CATEGORIES.items():
            if file_extension in extensions:
                return category
        
        return 'others'
    
    def find_available_filename(self, destination_path):
        """
        Find an available filename if the target already exists.
        
        Args:
            destination_path (Path): Desired file path
        
        Returns:
            Path: Available file path (possibly with number suffix)
        """
        if not destination_path.exists():
            return destination_path
        
        # If file exists, add a number suffix
        base_name = destination_path.stem
        extension = destination_path.suffix
        parent_dir = destination_path.parent
        counter = 1
        
        while destination_path.exists():
            new_name = f"{base_name}_{counter}{extension}"
            destination_path = parent_dir / new_name
            counter += 1
        
        return destination_path
    
    def organize_files(self):
        """Organize all files in the Downloads folder."""
        if not self.downloads_path.exists():
            print(f"Error: Downloads folder not found at {self.downloads_path}")
            return False
        
        if not self.downloads_path.is_dir():
            print(f"Error: {self.downloads_path} is not a directory")
            return False
        
        print(f"Organizing files in: {self.downloads_path}")
        print("-" * 60)
        
        # Get all files in Downloads folder (not directories)
        files_to_organize = [f for f in self.downloads_path.iterdir() if f.is_file()]
        self.stats['total_files'] = len(files_to_organize)
        
        if not files_to_organize:
            print("No files to organize.")
            return True
        
        for file_path in files_to_organize:
            try:
                self._organize_file(file_path)
            except Exception as e:
                print(f"Error processing {file_path.name}: {str(e)}")
                self.stats['errors'] += 1
        
        self._print_summary()
        return True
    
    def _organize_file(self, file_path):
        """
        Organize a single file into its appropriate category folder.
        
        Args:
            file_path (Path): Path to the file to organize
        """
        # Get file extension and determine category
        file_extension = file_path.suffix
        category = self.get_file_category(file_extension)
        
        # Create category folder if it doesn't exist
        category_folder = self.downloads_path / category
        category_folder.mkdir(exist_ok=True)
        
        # Determine destination path
        destination = category_folder / file_path.name
        
        # If file exists in destination, find available name
        if destination.exists() and destination != file_path:
            destination = self.find_available_filename(destination)
            self.stats['duplicates_renamed'] += 1
            print(f"Renamed duplicate: {file_path.name} -> {destination.name}")
        
        # Move the file
        shutil.move(str(file_path), str(destination))
        self.stats['organized'] += 1
        print(f"✓ {file_path.name} -> {category}/{destination.name}")
    
    def _print_summary(self):
        """Print summary statistics of the organization process."""
        print("-" * 60)
        print("Organization Summary:")
        print(f"  Total files found: {self.stats['total_files']}")
        print(f"  Files organized: {self.stats['organized']}")
        print(f"  Duplicates renamed: {self.stats['duplicates_renamed']}")
        print(f"  Errors: {self.stats['errors']}")
        print(f"\nYour Downloads folder is now organized! 🎉")


def main():
    """Main entry point for the script."""
    print("=" * 60)
    print("Downloads Folder Organizer")
    print("=" * 60)
    print()
    
    organizer = DownloadsOrganizer()
    organizer.organize_files()


if __name__ == "__main__":
    main()
