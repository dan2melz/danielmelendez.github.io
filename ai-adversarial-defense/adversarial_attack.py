import tensorflow as tf
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions

def generate_adversarial_example(img_path, epsilon=0.02):
    """Generates an adversarial example by adding small perturbations to the input image."""
    model = MobileNetV2(weights='imagenet')
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    img_tensor = tf.convert_to_tensor(img_array)
    with tf.GradientTape() as tape:
        tape.watch(img_tensor)
        predictions = model(img_tensor)
        loss = tf.keras.losses.sparse_categorical_crossentropy([np.argmax(predictions)], predictions)
    
    gradient = tape.gradient(loss, img_tensor)
    adversarial_img = img_tensor + epsilon * tf.sign(gradient)
    adversarial_img = tf.clip_by_value(adversarial_img, -1, 1)
    
    return adversarial_img.numpy()

if __name__ == "__main__":
    adversarial_example = generate_adversarial_example("sample.jpg")
    print("Adversarial example generated successfully.")
