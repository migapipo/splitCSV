# splitCSV

see the original URL: 
https://gist.github.com/traviswaelbro/fefc37b1ad36196e6b92cbb8cba8baa6

## split_file_in_folder:

Split all CSV files in a source path into multiple CSVs of equal numbers of records, except the last file.


Split files follow a sequential naming convention like so: `{file_number}_0.csv`
        
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
