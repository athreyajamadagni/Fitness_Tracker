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

![image](https://user-images.githubusercontent.com/75878205/182917315-7d56cf47-8c04-48f2-8940-f76423b9e823.png)

You will get your connection URL which will be used later in our program (Paste this URL in line 11 of dbOps.py file in the Data Base folder).

Module to be installed to use mongodb with python:

Pymongo : python -m pip install pymongo
https://pypi.org/project/pymongo/


