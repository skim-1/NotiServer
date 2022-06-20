import tensorflow as tf
import tensorflow_hub as tf_hub
import tensorflow_text as tf_text


def get_score(text, model):
    predictions = model.predict([text])
    return predictions[0]