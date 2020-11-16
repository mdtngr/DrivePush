# DrivePush
- Python based script to directly upload file to google drive
- Automation of file upload and view in Google drive using google apis(further creation of alias that displays results on the teminal itself)


- To Setup:

Get your client_secret file from google developers api

	- main.py-> Code snippet containing all functions to list,upload data

	- auth.py-> Code snippet to use client secter to authorise the script

	- listfile.py-> Code snippet to print the list of latest 50 files on drive

	- upload.py-> Code snippet to upload a image file to google drive


- Requirements:

	clientid and client_secret json file need to be generated from Google Developer API

	To congigure run auth.py then, the list and update function can be performed by the listfile.py and upload.py


- Working:

	-Further configuration in linux terminal is done by 

alias drivepush_up="python <path_to_upload.py>"

alias drivepush_list="python <path_to_listfile.py> | cut -d '(' -f 1"

Thus the final linux command required -

	- drivepush_list     #Lists latest updated 50 files on your google drive

	- drivepush_up       #Uploads jpg file to google drive(the path to file needs to be given on prompt)