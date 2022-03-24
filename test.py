import glob
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import imageio as im
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint
import csv
from PIL import Image

# Read train.csv
imageData = []
with open('./train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        imageData.append(row)

# Extract the different species
species = []
for i in range(1, len(imageData)):
    if imageData[i][1] not in species:
        species.append(imageData[i][1])

# image = np.load('./train_images/00549928dca501.jpg')
# print(image.shape)
image = Image.open('./train_images/00549928dca501.jpg')
data = np.asarray(image)
print(data.shape)
sh = (len(data), len(data[0]), len(data[0][0]))

data = np.c_[data, np.zeros(shape=sh)]
print(data.shape)
# image = mpimg.imread('./train_images/00549928dca501.jpg')
# plt.imshow(image)
# plt.show()
# data = np.asarray(image)
# dolphin = np.c_[data, np.zeros(len(data)), 3]
# print(data.shape)


# Create a label dict for species
speciesDict = {}
for i in range(len(species)):
    speciesDict[species[i]] = i
    
print(speciesDict['melon_headed_whale'])


# Extract the images
images = []
for i in range(1, int(len(imageData))):
#     image = mpimg.imread('./train_images/'+imageData[i][0])
#     data = np.asarray(image)
#     images.append(data)
    try:
        image = Image.open('./train_images/'+imageData[i][0])
    except:
        continue
    data = np.asarray(image)
    print(imageData[i][0])
    print("data:", data.shape)
    try:
        sh = (len(data), len(data[0]), len(data[0][0]))
    except:
        continue
    print("sh:", sh)
    data = np.c_[data, (speciesDict[imageData[i][1]])*np.ones(shape=sh)]
    images.append(data)

for i in images:
    print(i.shape)
