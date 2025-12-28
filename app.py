from flask import Flask, render_template, request
import base64, cv2, numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("camera.html")

@app.route("/upload", methods=["POST"])
def upload():
    data = request.form["image"]
    img_data = base64.b64decode(data.split(",")[1])

    img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
    cv2.imwrite("capture.jpg", img)

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
