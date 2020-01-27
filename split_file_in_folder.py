# Xiaoyu 
# 2020/01/26

import csv
import os
import sys

if len(sys.argv) != 4:
    raise Exception('Wrong number of arguments!')

"""
    Split all CSV files in a source path into multiple CSVs of equal numbers of records,
    except the last file.
    
    Split files follow a sequential naming convention like so:
        `{file_number}_0.csv`
    :param 
        SOURCE_PATH{str}: 
        Source path including files which need to be split.
    :param 
        DEST_PATH {str}:
        Full path to the directory where the split files should be saved.
    :param 
        ROW_LIMIT {int}:
        Number of rows per file (header row is excluded from the row count).
    :return {NoneType}:
"""

SOURCE_PATH = sys.argv[1]   
DEST_PATH = sys.argv[2]
ROW_LIMIT = int(sys.argv[3])


def split_csv(source_filepath, dest_path, result_filename_prefix, row_limit):
    """
    Split a source CSV into multiple CSVs of equal numbers of records,
    except the last file.
    The initial file's header row will be included as a header row in each split
    file.
    Split files follow a zero-index sequential naming convention like so:
        `{result_filename_prefix}_0.csv`
    :param source_filepath {str}:
        File name (including full path) for the file to be split.
    :param dest_path {str}:
        Full path to the directory where the split files should be saved.
    :param result_filename_prefix {str}:
        File name to be used for the generated files.
        Example: If `my_split_file` is provided as the prefix, then a resulting
                 file might be named: `my_split_file_0.csv'
    :param row_limit {int}:
        Number of rows per file (header row is excluded from the row count).
    :return {NoneType}:
    """
    if row_limit <= 0:
        raise Exception('row_limit must be > 0')

    with open(source_filepath, 'r') as source:
        reader = csv.reader(source)
        headers = next(reader)

        file_number = 0
        records_exist = True

        while records_exist:

            i = 0
            
            target_filename = f'{result_filename_prefix}_{file_number}.csv'
            target_filepath = os.path.join(dest_path, target_filename)

            with open(target_filepath, 'w') as target:
                writer = csv.writer(target)

                while i < row_limit:
                    
                    if i == 0:
                        writer.writerow(headers)

                    try:
                        writer.writerow(next(reader))
                        i += 1
                    except:
                        records_exist = False
                        break

            if i == 0:
                # we only wrote the header, so delete that file
                os.remove(target_filepath)

            file_number += 1


file_number = 0

with os.scandir(SOURCE_PATH) as it:
    
    for entry in it:
        
        if entry.name.endswith(".csv") and entry.is_file():
            file_number += 1
            split_csv(entry.path, DEST_PATH, file_number, ROW_LIMIT)
           
            
