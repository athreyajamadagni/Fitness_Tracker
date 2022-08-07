# Squat_Counter

This project scans your ID card using OCR and tracks/counts your squats with the proper form (hips on the same level or below the knee) takes this data (Roll Number and number of Squats) and uploads it to a mongodb data base.

This project is written using Python.


Creating a Mongodb database:

https://www.youtube.com/watch?v=2QQGWYe7IDU&ab_channel=TraversyMedia

You don't need to install Mongodb compass for this project.
After creating the cluster, in the database menu, you will see a connect button.
![image](https://user-images.githubusercontent.com/75878205/182916551-f84f4a53-7a6b-44a4-9544-37a5969a4b26.png)

Click the connect button, select the "Connect your application" option 
![image](https://user-images.githubusercontent.com/75878205/182916866-0f6c0db3-ae10-4a85-b758-c0ace2af2e0d.png)

Select Python in the "Driver" section and 3.4 or later in the "Version"

![M](https://user-images.githubusercontent.com/75878205/183059830-387cb286-8521-4309-9872-13512805a1e2.jpg)


You will get your connection URL which will be used later in our program (Paste this URL in line 11 of dbOps.py file in the Data Base folder).

Module to be installed to use mongodb with python:

Pymongo : python -m pip install pymongo
https://pypi.org/project/pymongo/

For the OCR part of the Project 

You will need:

OpenCV: pip install opencv-python / sudo pip install opencv-python

To run this script you’ll need OpenCV version 4.6 or better.
It is used to capture and save images and videos from the camera .
We convert the captured image to grayscale to make it easy to read the text.
![image](https://user-images.githubusercontent.com/75878205/183060135-0c362dc2-0b75-4818-88b6-4cd8f790fe15.png)

Tesseract-OCR: 

sudo apt-get install tesseract-ocr

pip install pytesseract

It reads the text from the image captured and converts it into a string 
![image](https://user-images.githubusercontent.com/75878205/183060224-7bcd7bbe-b2f0-4e0b-85b1-95e059b990bd.png)

When you scan your id card it reads all the text available in the image, converts it to a string and only extracts the required text (the SRN, here is the string starting with PES, change it to what ever sequence your ID cards starts with) from it. The line extracted is sent to the database.

For the Squat Counter of this project 

You will need:
OpenCv : pip install opencv-python / sudo pip install opencv-python

MediaPipe : sudo pip3 install mediapipe-rpi4

This code captures a real time video stream from the pi camera, which is then converted from BGR to RGB format. The mediapipe pose estimation model then detects the person, draws these detections on the image and connects all the detections using the drawing utilities. The IDs and coordinates of all these detections are stored. 

The pose landmarks are shown below:



Using the coordinates and landmarks of the knees and hip, we calculate their relative distance to determine if the person is doing the squat properly, and increase the count of squats accordingly. So, if the hip is at the same level as knees or below them, we will set the stage as ‘Down’ and when the hip is above the knees, the stage will change to ‘Up’ and it will be counted as one squat.If the person does not squat for a certain time, the code terminates automatically.


For the website part of the project we will be using Python flask and heroku.

Flask is a web application framework written in Python.

Heroku is a cloud platform as a service supporting several programming languages.

Follow these references to get started with flask and heroku

Flask:

https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=1&ab_channel=TechWithTim

Heroku with flask:

https://www.youtube.com/watch?v=23sp3cj5Pnc&ab_channel=ProgrammingKnowledge

To setup your raspberry pi for this project, follow the steps mentioned in these videos:
https://youtu.be/00c2GTpRaU8

https://youtu.be/mlwEJkrHBL8

Components used:
1.Raspberry pi 4

2.Pi camera


How to go about the project:

After running the code, hold 2 fingers up to intitate the ID card scanning process, if the ID card is not read successfully it will try to scan again, this happens for 3 times and if it fails all 3 times you have to hold up 2 fingers again to initiate the ID card scanning process.

Once the roll number is read correctly, the squat tracker begings. Squat with a proper form to add to the count of the number of squats performed. If no squat is detected in 15seconds then the counter automatically terminates.

This data (roll number and number of squats performed) is fed to the database. If the roll number does not already exist then it will create a new entry, if it already exists then it updated.

Then a tkinter window shows up with the Roll Number , number of squats perfomred in that session and the total number of squats that is linked to that roll number.

The window automatically closes after 8 seconds and it goes to the beginning to start a new session where you have to hold up 2 fingers to start the ID card scan process.

Any person can view their total number of squats that they have performed by visiting :

https://pesufitness-squat.herokuapp.com/
