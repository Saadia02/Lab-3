from rasterio.plot import show
import rasterio
from numpy import expand_dims
from keras.preprocessing.image import ImageDataGenerator, img_to_array
import matplotlib.pyplot as plt

# Open the raster file using rasterio
HHS = rasterio.open(r"D:\image processing\myenv\Unzip files\HV-ALPSRP247640510-H2.2_UA.tif")

# Read the image data and convert it to a NumPy array
data = HHS.read()
data = data.transpose(1, 2, 0)  # Transpose to (height, width, channels)

# Data augmentation
samples = expand_dims(data, 0)
datagen = ImageDataGenerator(zoom_range=[1,10])
it = datagen.flow(samples, batch_size=1)

# Display augmented images
plt.figure(figsize=(10, 10))
for i in range(9):
    plt.subplot(330 + 1 + i)
    batch = it.next()
    result = batch[0].astype('uint16')
    plt.imshow(result)

plt.show()