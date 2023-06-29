import numpy as np
import os
from tensorflow.keras.models import load_model
import gradio

model = load_model('model.h5')

labels_raw = os.listdir('data_raw')
labels = []

for label in labels_raw :
    labels.append(label.split('-')[1])

def classify_image(image_):
    
    mat = np.array(image_)
    mat = np.expand_dims(mat, axis = 0)
    prediction = model.predict(mat)[0]

    return {labels[i]: bool(prediction[i]) for i in range(10)}

image = gradio.inputs.Image(shape=(224,224))
label = gradio.outputs.Label(num_top_classes=3)

gradio.Interface(fn=classify_image, inputs=image, outputs=label,
                 title="Image classification - limited to 10 dog breeds").launch(debug=False)

def main() :
    return classify_image()

if __name__ == '__main__' :
    main()