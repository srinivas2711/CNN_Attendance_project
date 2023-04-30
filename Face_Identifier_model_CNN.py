# Specifying the folder where images are present
TrainingImagePath='C:/Users/Srini/Desktop/Proj_images/Training_images/'
from keras.preprocessing.image import ImageDataGenerator
#Performing Data augmentation here by mix of images
train_datagen = ImageDataGenerator(
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True)
t='C:/Users/Srini/Desktop/Proj_images/Testing_images'

#No transformations on image need to test the model so empty data generator
test_datagen = ImageDataGenerator()

# Generating the Training Data
training_set = train_datagen.flow_from_directory(
        TrainingImagePath,
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')


# Generating the Testing Data
test_set = test_datagen.flow_from_directory(
        t,
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')

# Printing class labels for each face
test_set.class_indices

import pickle
# class_indices have the numeric tag for each face
TrainClasses=training_set.class_indices

# Storing the face and the numeric tag for future reference
ResultMap={}
for faceValue,faceName in zip(TrainClasses.values(),TrainClasses.keys()):
    ResultMap[faceValue]=faceName

# Saving the face map for future reference
with open("ResultsMap.pkl", 'wb') as fileWriteStream:
    pickle.dump(ResultMap, fileWriteStream)

# This mapping will help to get the corresponding face name for it
print("Mapping of Face and its ID",ResultMap)

# The number of neurons for the output layer is equal to the number of faces
OutputNeurons=len(ResultMap)
print('\n The Number of output neurons: ', OutputNeurons)


from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPool2D
from keras.layers import Flatten
from keras.layers import Dense
import time
classifier= Sequential()
classifier.add(Convolution2D(32, kernel_size=(5, 5), strides=(1, 1), input_shape=(64,64,3), activation='relu'))
classifier.add(MaxPool2D(pool_size=(2,2)))
classifier.add(Convolution2D(64, kernel_size=(5, 5), strides=(1, 1), activation='relu'))
classifier.add(MaxPool2D(pool_size=(2,2)))
classifier.add(Flatten())
classifier.add(Dense(64, activation='relu'))
classifier.add(Dense(OutputNeurons, activation='softmax'))
#classifier.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
classifier.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics=["accuracy"])
classifier.fit(training_set,
                steps_per_epoch=2,
                epochs=40,
                validation_data=test_set,
                validation_steps=10)

EndTime=time.time()
print("#"*5+" Total Time Taken: ", round((EndTime-StartTime)/60), 'Minutes'+'#'*5')

#---------- Automatic Image Capture and Prediction with trained model---------------
import numpy as np
from tensorflow.keras.preprocessing import image
import cv2

# Load the face detection model
face_cascade = cv2.CascadeClassifier('C:/Users/Srini/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    cv2.imshow('Video Stream', frame)
    if frame is not None:
        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(250,250))
    # If a face is detected, capture the image and exit the loop
    if len(faces) > 0:
        # Capture the current frame
        cv2.imwrite('C:/Users/Srini/Desktop/captured_face.png', frame)
        # Display the captured image for a few seconds
        cv2.imshow('Captured Face', frame)
        cv2.waitKey(3000)
        break
    #If want to exit
    if cv2.waitKey(1) == ord('q'):
        break
# Release the camera when image captured
cap.release()
cv2.destroyAllWindows()
ImagePath='C:/Users/Srini/Desktop/captured_face.png'
test_image=image.load_img(ImagePath,target_size=(64, 64))
test_image=image.img_to_array(test_image)
test_image=np.expand_dims(test_image,axis=0)
result=classifier.predict(test_image,verbose=0)
conf_value=np.max(result,axis=1)
if conf_value[0] > 0.95:
    print('####'*10)
    print('Welcome Student',ResultMap[np.argmax(result)])
    val1=ResultMap[np.argmax(result)]
    q1="UPDATE student SET pres_stat= %s WHERE student_name = %s"
    status=(1,val1)
    c.execute(q1,status)
    q2="UPDATE student SET No_pre = No_pre + %s WHERE student_name = %s"
    up=(1,val1)
    c.execute(q2,up)
    connection.commit()
    print("Your Presence noted successfully!")
else:
    print("Model getting Confused! Please contact our Head Srinivasamoorthy Er,!!")
