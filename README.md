# Ransomware-Predication

#### In this project we are targetting to detect a file whether it is ransomware or not without executing it.

> Our aim is to deploy this as a free service to anyone as the process is complicated to setup the testing

**Process for Testing for Ransomware:**
```
1. Select the doubtfull application using our application
2. It will convert the file into image in background
3. The image is then encoded into a base64 string
4. Then the base64 string will be streamed to our cloud hosted REST Api
5. The api will convert the encoding back to image
6. Predict with the model 
7. Stream the result back to client
8. And client will be able to see wether the application is infected or not
9. The whole process will happen within fraction of seconds
```

**Technology Used:**
```
- Python 3.6
- CNN (Convolutional Neural Network)
- Flask as REST Api
- Tensorflow
- Keras
- OpenCV3 (processing the images)
- Python Pillow
```

**Target & Progress-**
- [x] Get The Dataset
- [x] Algorithm to convert Binary data to RGB image
- [x] CNN Model
- [x] Accuracy > 97%
- [ ] Prepare Rest API
- [ ] Deploy to some hosting

**Targetted accuracy > 97%**

> This project is still under development as our Final year Project
