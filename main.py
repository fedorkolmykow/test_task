from server import init_app
from config import Config


def main():
    app = init_app(Config)
    app.run(host='0.0.0.0')


if __name__ == "__main__":
    main()
