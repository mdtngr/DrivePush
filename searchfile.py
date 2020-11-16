from __future__ import print_function
import httplib2
import os, io

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
import auth
SCOPES = 'https://www.googleapis.com/auth/drive'
# INSERT the path to the client secret file!! That you get from google developers api
CLIENT_SECRET_FILE = 'path to client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.getCredentials()

http = credentials.authorize(httplib2.Http())
drive_service = discovery.build('drive', 'v3', http=http)
ip = input("Enter name of file to search: ")

def searchFol(val):
    page_token = None
    while True:
        response = drive_service.files().list(q="mimeType='image/jpeg'",
                                            spaces='drive',
                                            fields='nextPageToken, files(id, name)',
                                            pageToken=page_token).execute()
        for file in response.get('files', []):
            # Process change
            if(file.get('name')== val):
                print('Found file: ', file.get('name'))
        
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break

searchFol(ip)
