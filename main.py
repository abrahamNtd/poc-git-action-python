import os

def main():
    print("Runing phyton inside of Docker")
    for name, value in os.environ.items():
        print("{0}: {1}".format(name, value))


if __name__ == "__main__":
    main()
