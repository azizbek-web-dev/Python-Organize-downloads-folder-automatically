#!/usr/bin/env python3
"""
Real-time Downloads Folder Watcher
Automatically organizes files as soon as they appear in the Downloads folder.
"""

import time
import hashlib
from pathlib import Path
from organize_downloads import DownloadsOrganizer


class DownloadsWatcher:
    """Monitors the Downloads folder and automatically organizes new files."""
    
    def __init__(self, downloads_path=None):
        """
        Initialize the watcher.
        
        Args:
            downloads_path (str, optional): Path to Downloads folder.
        """
        self.organizer = DownloadsOrganizer(downloads_path)
        self.downloads_path = self.organizer.downloads_path
        self.known_files = set()
        self.is_running = False
        
        # Initialize with current files
        self._update_known_files()
        print(f"Watching: {self.downloads_path}")
        print(f"Initial scan: Found {len(self.known_files)} existing files")
    
    def _get_file_hash(self, file_path):
        """
        Get a simple hash of file metadata for identification.
        
        Args:
            file_path (Path): Path to the file
        
        Returns:
            str: Hash of file name, size, and modification time
        """
        try:
            stat = file_path.stat()
            # Create a hash from filename, size, and mtime
            data = f"{file_path.name}{stat.st_size}{stat.st_mtime}"
            return hashlib.md5(data.encode()).hexdigest()
        except Exception:
            return None
    
    def _update_known_files(self):
        """Update the set of known files in Downloads folder."""
        try:
            files = [f for f in self.downloads_path.iterdir() if f.is_file()]
            self.known_files = {self._get_file_hash(f) for f in files if self._get_file_hash(f)}
        except Exception as e:
            print(f"Error updating known files: {e}")
    
    def _check_for_new_files(self):
        """
        Check if any new files have been added.
        
        Returns:
            list: List of new file paths
        """
        try:
            current_files = [f for f in self.downloads_path.iterdir() if f.is_file()]
            new_files = []
            
            for file_path in current_files:
                file_hash = self._get_file_hash(file_path)
                if file_hash and file_hash not in self.known_files:
                    new_files.append(file_path)
                    self.known_files.add(file_hash)
            
            return new_files
        except Exception as e:
            print(f"Error checking for new files: {e}")
            return []
    
    def start_watching(self, check_interval=2):
        """
        Start watching the Downloads folder.
        
        Args:
            check_interval (int): How often to check for new files (in seconds)
        """
        self.is_running = True
        print(f"\n{'='*60}")
        print("Downloads Folder Watcher Started")
        print(f"Checking every {check_interval} seconds...")
        print("Press Ctrl+C to stop")
        print(f"{'='*60}\n")
        
        try:
            while self.is_running:
                new_files = self._check_for_new_files()
                
                if new_files:
                    print(f"\n[{time.strftime('%Y-%m-%d %H:%M:%S')}] Found {len(new_files)} new file(s)")
                    self._organize_new_files()
                
                time.sleep(check_interval)
        
        except KeyboardInterrupt:
            print("\n\nWatcher stopped by user.")
            self.is_running = False
    
    def _organize_new_files(self):
        """Organize any new files that appeared in Downloads."""
        try:
            # Get files that are not in category folders
            files_to_organize = []
            for file_path in self.downloads_path.iterdir():
                if file_path.is_file() and file_path.parent == self.downloads_path:
                    files_to_organize.append(file_path)
            
            if files_to_organize:
                print(f"Organizing {len(files_to_organize)} file(s)...")
                self.organizer.organize_files()
                self._update_known_files()
        
        except Exception as e:
            print(f"Error organizing files: {e}")
    
    def stop_watching(self):
        """Stop watching the Downloads folder."""
        self.is_running = False
        print("Watcher stopped.")


def main():
    """Main entry point for the watcher."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Watch Downloads folder and auto-organize new files')
    parser.add_argument('--interval', type=int, default=2, 
                       help='Check interval in seconds (default: 2)')
    parser.add_argument('--path', 
                       help='Path to Downloads folder (optional)')
    
    args = parser.parse_args()
    
    watcher = DownloadsWatcher(downloads_path=args.path)
    watcher.start_watching(check_interval=args.interval)


if __name__ == "__main__":
    main()
