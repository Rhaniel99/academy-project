from src.app import app

HOST = 'localhost'
PORT = 4000
DEBUG = True


if __name__ == "__main__":
    app.secret_key = '012#!APaAjaBoleh)(*^%'
    app.run(HOST, PORT, DEBUG)
