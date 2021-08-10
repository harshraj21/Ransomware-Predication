from keras.models import load_model
import numpy as np
import cv2
import pickle
import imutils
import os

RAW_IMAGE_TO_CLASSIFY = 'test.png'

MODEL_FILENAME = "ransom_model.hdf5"
MODEL_LABELS_FILENAME = "ransom_label.dat"
DATASET = "dataset"

with open(MODEL_LABELS_FILENAME, "rb") as f:
    lb = pickle.load(f)

raw_image_arr = []
raw_image_arr.append((RAW_IMAGE_TO_CLASSIFY))

def resize_image(image, width, height):
    (h, w) = image.shape[:2]
    if w > h:
        image = imutils.resize(image, width=width)
    else:
        image = imutils.resize(image, height=height)
    padW = int((width - image.shape[1]) / 2.0)
    padH = int((height - image.shape[0]) / 2.0)
    image = cv2.copyMakeBorder(image, padH, padH, padW, padW, cv2.BORDER_REPLICATE)
    image = cv2.resize(image, (width, height))
    return image

model = load_model(MODEL_FILENAME)
for image_file in raw_image_arr:
    image = cv2.imread(image_file,0)
    proc_image = resize_image(image, 64, 64)
    proc_image = np.expand_dims(proc_image, axis=2)
    proc_image = np.expand_dims(proc_image, axis=0)
    prediction = model.predict(proc_image)
    op = lb.inverse_transform(prediction)[0]
    acc = model.predict_proba(proc_image)
    print('Predicted File Name: '+op)
    #print(acc)
    # os.rename(image_file,"["+op+"].png")
print("All Operations Finished Sucessfully!!")
