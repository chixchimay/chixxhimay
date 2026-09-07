
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>ChiXchimay Photography</title></head>
    <body style="margin:0; font-family:sans-serif; background:#0a0a0a; color:white; text-align:center;">
        <div style="padding:60px 20px;">
            <h1 style="font-size:50px; letter-spacing:2px;">ChiXchimay Photography 📸</h1>
            <p style="color:#aaa; font-size:18px;">REGGIO EMILIA, Italy | Capturing Moments</p>
            <div style="margin-top:40px; background:white; color:black; display:inline-block; padding:12px 25px; border-radius:30px; font-weight:bold;">
                Gallery Coming Soon
            </div>
            <p style="margin-top:50px; color:#555;">Site is Ready!</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
