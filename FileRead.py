def main():
    readFile = open("myfile.txt","r")
    for line in readFile:
        print(line)
    readFile.close()
    print("App is Done")

if __name__ == '__main__':main()
