import sys
import os
import shutil
import traceback

def list_directory(directory):
    print("+ Listing directory: " + directory)
    for item in os.listdir(directory):
        print(" - " + item)

def main():
    print("Runing phyton inside of Docker")
    for name, value in os.environ.items():
        print("{0}: {1}".format(name, value))
    print ('Argument List:', str(sys.argv))
    #list_directory("/github/workspace")
    list_directory(".")


if __name__ == "__main__":
    main()
