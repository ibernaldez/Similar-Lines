# Similar Lines

READ ME

ABOUT

Since May 1st 2021, I've programmed for at least one hour every single day. I hope to become a great programmer, and know constant practice is the only way to do it. 

Massive thank you to my great friend Henri Schmidt. This project was his idea, and he has provided extremely helpful feedback and guidance throughout this whole process!

SIMILAR LINES

Takes two .txt files in the command line and returns which lines are similar. 

In the context of this program, "similar" means that regardless of non character items in the line, or the order of the words, the words themselves are the same. Similar does not mean the same. 

For example:

File 1, line 1: foo soson bar bash
File 2, line 3: !!!!foo soson bar bash . - ??

would fall under the "similar" characterization. Although File 2, line 3 has non-character items in the line, the programs filters them out before comparing them.

Another example:

File 1, line 2: hello ignacio i hope
File 2, line 5: ignacio i hope hello

would fall under the "similar" characterization. Although the order of the words is different the words themselves are the same. 

Another example: 

File 1, line 7: abc def
File 2, line 7: abcd ef 

although the letters are the same, the words themselves arent. "abc" != "abcd."

FUNCTIONS 

def open_commandline_arg(data, file_num):

This function takes the command line argument file, reads the lines, and appends them to a list. 


def clean(filedata):

This function cleans the lines of each file, removing any non character elements. The cleaned lines are then again appended to a list. 

def main():


This function passed the two files through the above functions. The functions are then indexed through and compared. I choose to use sorted() when comparing, but setting the list to a set would've also worked. 
There are certaintly more efficent ways to compare the lines of the two files. Because of the nested for loop, the run time is O(n^2). However, this program demonstrates my current understanding, so searching for a more efficent algorithim would've felt dishonest.

Sources: 

https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
https://stackoverflow.com/questions/50589997/open-a-python-file-with-command-line-arguments/50590039
https://stackoverflow.com/questions/43438303/how-to-read-print-the-io-textiowrapper-data
https://www.geeksforgeeks.org/reading-writing-text-files-python/
https://www.guru99.com/python-counter-collections-example.html
https://stackoverflow.com/questions/3984539/python-use-regular-expression-to-remove-the-white-space-from-all-lines
https://docs.python.org/3/library/re.html
