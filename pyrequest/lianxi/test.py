#coding=utf-8
import os
def batch_rename(work_dir, old_ext, new_ext):
    """
    This will batch rename a group of files in a given directory,
    once you pass the current and new extensions
    """
    # files = os.listdir(work_dir)
    for filename in os.listdir(work_dir):
        print filename
        # Get the file extension
        split_file = os.path.splitext(filename)
        print split_file
        file_ext = split_file[1]
        # Start of the logic to check the file extensions, if old_ext = file_ext
        if old_ext == file_ext:
            # Returns changed name of the file with new extention
            newfile = split_file[0] + new_ext
            print 'fff', os.path.join(work_dir, filename), os.path.join(work_dir, newfile)
            # Write the files
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
batch_rename('F:\\fff','.doc','.docx')

