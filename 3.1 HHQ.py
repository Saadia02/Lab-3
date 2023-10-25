from rasterio.plot import show
import rasterio
import matplotlib.pyplot as plt #For plotting our visualizations
from keras.preprocessing.image import ImageDataGenerator #Keras dataset generator class.
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from PIL import Image

# %matplotlib inline  # Uncomment this line if running this code in Jypiter notebook

#SANGHAR HH
S1 = rasterio.open(r"D:\image processing\myenv\Unzip files\HH-ALPSRP247640510-H2.2_UA.tif")
plt.title("HHS")
show(S1)