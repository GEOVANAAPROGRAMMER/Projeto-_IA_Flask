from flask import Flask, render_template, request, jsonify
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io
import tensorflow as tf

app = Flask(__name__)

# Carregar o modelo Keras e as classes
model = tf.keras.models.load_model('keras_model.h5')
with open('labels.txt', 'r') as file:
    classes = [line.strip() for line in file]

@app.route('/')
def index():
    return render_template('lista.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    uploaded_file = request.files['file']

    if uploaded_file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Processar a imagem
    img = Image.open(io.BytesIO(uploaded_file.read()))
    img = img.resize((224, 224))  # Redimensionar para o tamanho desejado
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    # Fazer a previsão
    predictions = model.predict(img_array)
    predicted_class = classes[np.argmax(predictions)]

    return jsonify({'Previsão': predicted_class})

if __name__ == '__main__':
    app.run(debug=True)
