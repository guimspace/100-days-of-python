import sys

from app import App


def main(argv):
    if len(argv) <= 1 or argv[1] == "verify":
        App.verify(argv[2])
    elif argv[1] == "setup":
        App.setup()
    else:
        print(f"{argv[0]}: [setup | verify]")


if __name__ == "__main__":
    main(sys.argv)
