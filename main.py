import os
import sys
import zipfile
import time
from jumpssh import SSHSession
from datetime import datetime

def zip_dir(files, file_name):
    print("\n Creating artifact .....\n")
    zip_file = zipfile.ZipFile(file_name, mode="w")
    root = os.getcwd()
    for file in files:
        zip_file.write(file)
    zip_file.close()
    print("\n Artifact has been created")

def list_directory(directory):
    print("+ Listing directory: " + directory)
    for item in os.listdir(directory):
        print(" - " + item)

def get_canged_files(filename):
    with open(filename) as file:
        files = [line.rstrip() for line in file]
    return files

def main():
    print("Runing phyton inside of Docker")
    print ('Argument List:', str(sys.argv))
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        bastion_host = sys.argv[3]
        remote_host = sys.argv[4]
        print ('User_name:', username)
        files = get_canged_files("list.txt")
        timestamp = datetime.now().time()
        zip_file = str(timestamp) + ".zip"
        zip_dir(files,zip_file)
        list_directory(".")
    #list_directory("/github/workspace")


if __name__ == "__main__":
    main()
