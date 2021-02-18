import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import random
import pickle
import time

DATADIR = "F:/pythonSeries/ai series/Paint_AR/scripts/images_t"
CATEGORIES = ["rpress_click","release","test1"]

for category in CATEGORIES:
	path = os.path.join(DATADIR,category)
	for img in os.listdir(path):
		img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)
		plt.imshow(img_array, cmap='gray')
		plt.show()  # display!

		break
	break
print(img_array)
print(img_array.shape)
IMG_SIZE = 100
#new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
#ret,thresh1 = cv2.threshold(new_array,60,100,cv2.THRESH_BINARY)
#ret,thresh3 = cv2.threshold(new_array,127,255,cv2.THRESH_TRUNC)
# ret,thresh4 = cv2.threshold(new_array,127,255,cv2.THRESH_TOZERO)

# #plt.imshow(new_array, cmap='gray')
# plt.imshow(thresh4, cmap='gray')
# plt.show()

#Training data:::::::

training_data = []

def create_training_data():
	for category in CATEGORIES:

		path = os.path.join(DATADIR,category)
		class_num = CATEGORIES.index(category)

		for img in tqdm(os.listdir(path)[:200]):
			try:
				img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)
				new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
				
				#print(category)
				if category == "test1":
					cv2.imwrite("n1/{}.png".format(time.time()),new_array)
				#training_data.append([new_array, class_num])
			except Exception as e:
				pass
create_training_data()

# print(len(training_data))

# random.shuffle(training_data)
# for sample in training_data[:10]:
# 	print(sample[1])

# #Lets save our data set

# X = []
# y = []

# for features,label in training_data:
# 	X.append(features)
# 	y.append(label)

# print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))

# X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

# pickle_out = open("X.pickle","wb")
# pickle.dump(X, pickle_out)
# pickle_out.close()

# pickle_out = open("Y.pickle","wb")
# pickle.dump(y, pickle_out)
# pickle_out.close()