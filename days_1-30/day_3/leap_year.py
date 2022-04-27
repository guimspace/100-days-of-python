def main():
    year = int(input(""))

    if year % 4 != 0:
        print("common year")
    elif year % 100 != 0:
        print("leap year")
    elif year % 400 == 0:
        print("leap year")
    else:
        print("common year")


if __name__ == "__main__":
    main()
