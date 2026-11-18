
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
        <h1>Cloud Computing Lab 8</h1>
        <p>Application successfully implemented using Flask.</p>
        <p>This application demonstrates Platform as a Service (PaaS).</p>
        <h3>Hosted using Render</h3>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
