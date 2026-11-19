
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Cloud Computing Lab testing</title>
    </head>
    <body>
        <h1>Welcome to Cloud Computing Lab testing</h1>
        <h2>Application Version 3</h2>
        <p>Successfully deployed using Render.</p>
        <p>This application demonstrates Platform as a Service (PaaS).</p>
        <p>Automatic deployment verified successfully.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
