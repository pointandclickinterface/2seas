from flask import Flask

app= Flask(__name__)

@app.route("/")
def conn():
    return "Connected Properly"

if __name__ == "__main__":
    app.run()