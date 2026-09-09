
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Chixx Photography</title>
<style>
body{margin:0;font-family:Arial;background:#0a0a0a;color:white;text-align:center}
.header{padding:60px 20px;background:linear-gradient(rgba(0,0,0,0.6),rgba(0,0,0,0.6)),url('https://images.unsplash.com/photo-1452587925148-ce544e77e70d');background-size:cover}
.header h1{font-size:50px;margin:0;letter-spacing:3px}
.header p{font-size:18px;color:#ccc}
.btn{display:inline-block;padding:12px 25px;margin:10px;border-radius:30px;text-decoration:none;font-weight:bold}
.btn-whatsapp{background:#25D366;color:white}
.btn-call{background:white;color:black}
.btn-insta{background:linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888);color:white}
.btn-fb{background:#1877F2;color:white}
.gallery{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;padding:20px}
.gallery img{width:100%;height:250px;object-fit:cover;border-radius:15px}
.section{padding:40px 20px}
.contact-box{background:#1a1a1a;padding:30px;border-radius:20px;margin:20px}
</style>
</head>
<body>

<div class="header">
    <h1>CHIXX PHOTOGRAPHY</h1>
    <p>Capturing Moments, Creating Memories</p>
    <br>
    <a href="https://wa.me/91XXXXXXXXXX" class="btn btn-whatsapp">WhatsApp Me</a>
    <a href="tel:+39340456306" class="btn btn-call">📞 Call Now</a>
</div>

<div class="section">
    <h2>📸my Work</h2>
    <p></p>
    <div class="gallery">
        <img src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4">
        <img src="https://images.unsplash.com/photo-1469474968028-56623f02e42e">
        <img src="https://images.unsplash.com/photo-1501785888041-af3ef285b470">
        <img src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05">
        <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e">
        <img src="https://images.unsplash.com/photo-1426604966848-d7adac402bff">
    </div>
</div>

<div class="section">
    <h2>🔗 Follow Me</h2>
    <a href="https://instagram.com/saki_fakir" class="btn btn-insta">Instagram</a>
    <a href="https://facebook.com/farhan ahamed sakib" class="btn btn-fb">Facebook</a>
</div>

<div class="contact-box">
    <h2>📞 Contact Me</h2>
    <p>Booking to captur any beautiful moment</p>
    <h3>+393420456306</h3>
    <p>Reggio Emilia, Italy</p>
</div>

<p style="padding:20px;color:#555">© 2026 Chixx Photography</p>
</body>
</html>
    """

if __name__ == '__main__':
    app.run()
