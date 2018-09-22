def main():
    try:
        x = int(input("Enter a number"))
        print(x+6)
    except ValueError:
        print("value have to be integer")

if __name__ == '__main__':main()
