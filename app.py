from flask import Flask, render_template, send_file, request

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Level 1
@app.route("/level1", methods=["GET", "POST"])
def level1():
    if request.method == "POST":
        submitted_flag = request.form.get("flag")
        if submitted_flag == "ctf{you_found_the_flag}":
            return "<h2>Correct! <a href='/level2'>Proceed to Level 2 </a></h2>"
        else:
            return "<h2>Incorrect flag. Try again!</h2><a href='/level1'>Back</a>"
    return render_template("level1.html")

@app.route("/download1")
def download1():
    return send_file("static/challenge_with_flag.jpg", as_attachment=True)

# Level 2
@app.route("/level2", methods=["GET", "POST"])
def level2():
    if request.method == "POST":
        submitted_flag = request.form.get("flag")
        if submitted_flag == "ctf{layered_secret_found}":
            return "<h2>Correct! <a href='/level3'>Proceed to Level 3 </a></h2>"
        else:
            return "<h2>Incorrect flag. Try again!</h2><a href='/level2'>Back</a>"
    return render_template("level2.html")

@app.route("/download2")
def download2():
    return send_file("static/level2_image.png", as_attachment=True)

# Level 3
@app.route("/level3", methods=["GET", "POST"])
def level3():
    if request.method == "POST":
        submitted_flag = request.form.get("flag")
        if submitted_flag == "ctf{audio_secret_revealed}":
            return "<h2>Congratulations! You've completed the CTF!</h2>"
        else:
            return "<h2>Incorrect flag. Try again!</h2><a href='/level3'>Back</a>"
    return render_template("level3.html")

@app.route("/download3")
def download3():
    return send_file("static/level3_audio.mp3", as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
