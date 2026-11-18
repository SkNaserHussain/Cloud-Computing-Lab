
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Cloud Computing Lab 8</title>
    </head>
    <body>
        <h1>Welcome to Cloud Computing Lab 8</h1>
        <h2>Application Version 2</h2>
        <p>Successfully deployed using Render.</p>
        <p>This application demonstrates Platform as a Service (PaaS).</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
