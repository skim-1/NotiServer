from flask import Flask, request, jsonify
from flask_cors import cross_origin
import json
from pred_spam import get_score as get_spam
from pred_news import get_score as get_news
import tensorflow as tf
import tensorflow_hub as tf_hub
import tensorflow_text as tf_text
import openai

app = Flask(__name__)
spmodel = tf.keras.models.load_model('./spamModel.h5', custom_objects={'KerasLayer': tf_hub.KerasLayer})
nmodel = tf.keras.models.load_model('./newModel.h5', custom_objects={'KerasLayer': tf_hub.KerasLayer})

openai.api_key = "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"


def display_score(raw_score):
    return round(raw_score, 3)


@app.route('/news', methods=['POST'])
@cross_origin()
def news():
    if request.method == 'POST':
        f = request.json
        score = get_news(str(f['text']), nmodel)
        print(float(score[0]))
        out = jsonify(msg=display_score(float(score[0])))
        return out
    else:
        out = jsonify(msg='dont work')
        return out


@app.route('/spam', methods=['POST'])
@cross_origin()
def spam():
    if request.method == 'POST':
        f = request.json
        score = get_spam(str(f['text']))
        print(float(score[0]), spmodel)
        out = jsonify(msg=display_score(float(score[0])))
        return out
    else:
        out = jsonify(msg='dont work')
        return out


@app.route('/summary', methods=['POST'])
@cross_origin()
def summary():
    if request.method == 'POST':
        f = request.json

        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f['text'],
            temperature=0.7,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        summ = response.choices[0].text.strip()

        out = jsonify(msg=summ)
        return out


if __name__ == '__main__':
    app.run(debug=True)