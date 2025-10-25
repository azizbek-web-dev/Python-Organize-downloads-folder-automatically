#!/usr/bin/env python3
"""
Scheduler Module for Downloads Folder Organizer
Automatically runs the organizer at specified intervals.
"""

import schedule
import time
from datetime import datetime
from organize_downloads import DownloadsOrganizer


class OrganizerScheduler:
    """Manages automatic scheduling of the organizer."""
    
    def __init__(self, downloads_path=None):
        """
        Initialize the scheduler.
        
        Args:
            downloads_path (str, optional): Path to Downloads folder.
        """
        self.organizer = DownloadsOrganizer(downloads_path)
        self.is_running = False
    
    def run_daily(self, time_str="09:00"):
        """
        Schedule the organizer to run daily at a specific time.
        
        Args:
            time_str (str): Time in HH:MM format (24-hour).
        """
        schedule.every().day.at(time_str).do(self._run_organizer)
        print(f"Scheduled to run daily at {time_str}")
    
    def run_hourly(self):
        """Schedule the organizer to run every hour."""
        schedule.every().hour.do(self._run_organizer)
        print("Scheduled to run every hour")
    
    def run_at_interval(self, interval_hours=12):
        """
        Schedule the organizer to run at specific intervals.
        
        Args:
            interval_hours (int): Interval in hours.
        """
        schedule.every(interval_hours).hours.do(self._run_organizer)
        print(f"Scheduled to run every {interval_hours} hours")
    
    def run_weekly(self, day_of_week="monday", time_str="09:00"):
        """
        Schedule the organizer to run weekly.
        
        Args:
            day_of_week (str): Day of week (monday, tuesday, etc.).
            time_str (str): Time in HH:MM format.
        """
        schedule.every().week.at(time_str).do(self._run_organizer)
        print(f"Scheduled to run every {day_of_week} at {time_str}")
    
    def _run_organizer(self):
        """Internal method to run the organizer."""
        print(f"\n{'='*60}")
        print(f"Automatic organization started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}\n")
        
        try:
            self.organizer.organize_files()
            print(f"\n{'='*60}")
            print(f"Automatic organization completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"{'='*60}\n")
        except Exception as e:
            print(f"Error during automatic organization: {str(e)}")
    
    def start_scheduler(self):
        """Start the scheduler loop."""
        self.is_running = True
        print("Scheduler started. Press Ctrl+C to stop.")
        print("Waiting for scheduled time...\n")
        
        try:
            while self.is_running:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("\n\nScheduler stopped by user.")
            self.is_running = False
    
    def stop_scheduler(self):
        """Stop the scheduler."""
        self.is_running = False
        print("Scheduler stopped.")


def main():
    """Main entry point for the scheduler."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Schedule Downloads folder organizer')
    parser.add_argument('--mode', choices=['daily', 'hourly', 'interval', 'weekly'], 
                       default='daily', help='Scheduling mode')
    parser.add_argument('--time', default='09:00', 
                       help='Time for daily/weekly runs (HH:MM format)')
    parser.add_argument('--interval', type=int, default=12, 
                       help='Interval in hours for interval mode')
    parser.add_argument('--path', 
                       help='Path to Downloads folder (optional)')
    
    args = parser.parse_args()
    
    scheduler = OrganizerScheduler(downloads_path=args.path)
    
    if args.mode == 'daily':
        scheduler.run_daily(args.time)
    elif args.mode == 'hourly':
        scheduler.run_hourly()
    elif args.mode == 'interval':
        scheduler.run_at_interval(args.interval)
    elif args.mode == 'weekly':
        scheduler.run_weekly(time_str=args.time)
    
    scheduler.start_scheduler()


if __name__ == "__main__":
    main()
