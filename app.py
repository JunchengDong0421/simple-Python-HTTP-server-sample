from flask import Flask, render_template, request, redirect, send_file, json

app = Flask(__name__, static_url_path='/')
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/patch')
def send_patch():
    return send_file("patches/universal_c_runtime_2008_R2_x86_64.msu", as_attachment=True)


@app.route('/upload', methods=['POST'])
def receive_file():
    files = request.files.getlist('f')
    for f in files:
        if file_name := f.filename:
            f.save(f"files/{file_name}")
    return redirect('/')


@app.route('/upload-ajax', methods=["POST"])
def receive_file_ajax():
    files = request.files.getlist('f')
    for f in files:
        if file_name := f.filename:
            f.save(f"files/{file_name}")
    return json.dumps({"num": len(files)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
