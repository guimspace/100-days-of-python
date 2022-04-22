from app import App


def main():
    try:
        app = App()
    except Exception:
        app = None
        return

    app.launch()


if __name__ == "__main__":
    main()
