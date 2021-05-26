"""
Similar Lines
"""
import sys
import re

# Opens the user input files
def open_commandline_arg(data, file_num):
    with open(data[file_num], 'r') as firstfile_read:
        firstfile_data = firstfile_read.readlines()
    print(type(firstfile_data))
    return firstfile_data

# Cleans the input files, removing numbers and punctuation
def clean(filedata):
    file_lines_cleaned = []
    for lines in range(len(filedata)):
        edit_line = re.sub(r'[^a-zA-Z ]+', '', filedata[lines])
        file_lines_cleaned.append(edit_line)
    return file_lines_cleaned

# Compares lines of each cleaned file
    # line 0 == line 1, line 1 == line 2, etc
def main():
    similarity_counter = 0
    files_num = [0, 1]
    files_num[0] = open_commandline_arg(sys.argv, 1)
    files_num[1] = open_commandline_arg(sys.argv, 2)
    file1_data, file2_data = files_num[0], files_num[1]
    file1_cleaned = clean(file1_data)
    file2_cleaned = clean(file2_data)
    for file1_lines in range(len(file1_cleaned)):
        for file2_lines in range(len(file2_cleaned)):
            if sorted(file1_cleaned[file1_lines].split()) == sorted(file2_cleaned[file2_lines].split()):
                similarity_counter += 1
                print("Similarity #" + str(similarity_counter))
                print("\tFile1.txt:")
                print("\t\tLine " + str(file1_lines + 1) + ": " + file1_data[file1_lines])
                print("\tFile2.txt:")
                print("\t\tLine " + str(file2_lines + 1) + ": " + file2_data[file2_lines])
main()
