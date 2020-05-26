import os
from google.cloud import translate_v2 as translate
import json
from flask import Flask, Response, request, jsonify, json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    print("hihi")
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)


@app.route("/translator", methods=['POST'])
def translator_func():
    if request.method == 'POST':
        print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
        client = translate.Client()
        origin = request.form.get('origin_word')
        dest = request.form.get('trans_language')
        result = client.translate(origin, target_language=dest)
        print(result)
        data = {
            "trans_language": result['detectedSourceLanguage'],  # dest = 타겟 언어
            "origin_word": result['input'],  # origin = 번역할 글자
            "trans_word": result['translatedText'],  # text = 번역된 글자
        }
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
