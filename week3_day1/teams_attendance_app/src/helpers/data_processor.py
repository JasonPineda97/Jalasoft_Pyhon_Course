"""
    Filters in-memory meetings data and uses meeting_name, star_date, end_date, etc...
"""
import os
def get_file_path(args):
    files_with_name = []
    for base, dirs, files in os.walk("../attendace_reports"):
        for file in files:
            if args.get("name") in file:
                files_with_name.append(base.replace("\\", "/")+"/"+file)
    return files_with_name