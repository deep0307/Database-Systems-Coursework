import os
import subprocess

filenames = []
path_to_files = ""
#   Function to store all filenames in a list
def extract_filename(path_to_files):    # "/Users/****/Desktop/Old_epubs"
    os.chdir(path_to_files)
    books = os.getcwd()
    for f in os.listdir(books):
        f_name, f_ext = os.path.splitext(f)
        if f_ext == ".epub":
            filenames.append(f_name)

    filenames.sort()

#   Function to generate new epub files
def create_epub(path_to_new_files): # "/Users/****/Desktop/new_epubs/"
    total_files = len(filenames)
    for i in range(total_files):
        epub_path = "cd " + path_to_files
        filename = filenames[i] + ".epub"
        zipping = " zip -X -r " + path_to_new_files + filename + " mimetype *"
        plist = "rm iTunesMetadata.plist"
        comm = epub_path + filename + "; " + plist + "; " + zipping
        p1 = subprocess.run(comm, capture_output = True, text = True, shell = True)
        success = p1.returncode
        if success == 0:
            rem_files = total_files - i + 1
            print("File #", i+1, " has been processed successfully. Remaining files: ", rem_files)

#   Enter the paths
extract_filename(r"C:\Users\deepd\OneDrive\Desktop\Book")   # Path to directory containing epub packages
create_epub(r"C:\Users\deepd\OneDrive\Desktop\LeetCode")   # Path to store new epub files in