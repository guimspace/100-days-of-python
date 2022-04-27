from prettytable import PrettyTable


def main():
    table = PrettyTable()

    table.add_column("^", ["True", "False"])
    table.add_column("True", ["True", "False"])
    table.add_column("False", ["False", "False"])

    table.align = "c"

    print(table)


if __name__ == "__main__":
    main()
