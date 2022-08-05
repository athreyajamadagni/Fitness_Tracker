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


