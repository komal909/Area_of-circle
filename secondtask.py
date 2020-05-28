Input:
file=str(input("enter the filename: "))
file_extension=file.split(".") 
print("the extension of the file is " + repr(file_extension[1] + 'thon'))

Output:
Enter the filename: abc.py
the extension of the file is 'python'
