import tensorflow as tf
import numpy as np
from PIL import Image

class ObjectIdentifier:
    def __init__(self):
        self.model = tf.keras.applications.ResNet50(weights='imagenet')

    def preprocess_image(self, image_path):
        image = Image.open(image_path)
        image = image.resize((224, 224))
        image = np.array(image)
        image = np.expand_dims(image, axis=0)
        image = tf.keras.applications.resnet50.preprocess_input(image)
        return image

    def identify_objects(self, image_path):
        predictions = self.model.predict(self.preprocess_image(image_path))
        top_predictions = tf.keras.applications.resnet50.decode_predictions(predictions, top=5)[0]
        return [label for (_, label, _) in top_predictions]

    def run_object_detection(self, image_path):
        objects_found = self.identify_objects(image_path)
        return "Objects found: " + ", ".join(objects_found)
