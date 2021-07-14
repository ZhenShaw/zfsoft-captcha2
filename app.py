from flask import Flask, url_for, request, redirect
from predictor import split_pic, analyse
from tensorflow import keras

app = Flask(__name__)  # __main__
model = keras.models.load_model('./model/model_10000')


@app.route("/")
def hello(name=None):
    return """home page
    upload: /upload
    api: /api
    """


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return 'No selected file'
        else:
            result = analyse(file.read(), model)
            return "".join(result)
    elif request.method == 'GET':
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
        </form>
        '''


@app.route('/api', methods=['POST'])
def api():
    if request.method == 'POST':
        stream = request.data
        result = analyse(stream, model)
        return "".join(result)


if __name__ == "__main__":
    from gevent.pywsgi import WSGIServer

    # app.run()
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()


# 云函数入口
def handler(environ, start_response):
    return app(environ, start_response)