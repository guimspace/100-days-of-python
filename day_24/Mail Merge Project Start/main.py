def main():
    with open("Input/Letters/starting_letter.txt") as letter:
        template = letter.readlines()

    with open("Input/Names/invited_names.txt") as guests:
        names = guests.readlines()

    for name in names:
        name = name.strip()

        copy = []
        for line in template:
            copy.append(line.replace("[name]", name))

        file_name = f"Output/ReadyToSend/{name}.txt"
        with open(file_name, "w") as letter:
            letter.write("".join(copy))


if __name__ == "__main__":
    main()
