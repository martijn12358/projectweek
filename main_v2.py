import matplotlib.pyplot as plt
from name_identifier import best_match, number_match
import keras_ocr

# keras-ocr will automatically download pretrained
# weights for the detector and recognizer.
pipeline = keras_ocr.pipeline.Pipeline()

# Get a set of three example images
# Read images from folder path to image object
images = [
    keras_ocr.tools.read(img) for img in ['test_ball_2.jpg']
]

# Each list of predictions in prediction_groups is a list of
# (word, box) tuples.
prediction_groups = pipeline.recognize(images)

# Plot the predictions
if len(images) > 1:
    fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
    for ax, image, predictions in zip(axs, images, prediction_groups):
        keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)
else:
    keras_ocr.tools.drawAnnotations(image=images[0], predictions=prediction_groups[0])


#predicted_image = prediction_groups[0]
for predicted_image in prediction_groups:
    for text, box in predicted_image:
        if len(text) > 1:
            print(f"{text = }, {best_match(text) = }")
        else:
            print(f"{text = }, {number_match(text) = }")



plt.show()
