def main():
    try:
        ReadFile = open("textfile.txt","r")
        for line in ReadFile:
            print(line)
        ReadFile.close()
    except IOError:
        print("file not found")
    print("App is Done")


if __name__ == '__main__':main()
