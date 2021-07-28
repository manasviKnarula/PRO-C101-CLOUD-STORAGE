import os
import shutil
import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

class TransferData:

    def __init__(self,AccessToken):
        self.AccessToken=AccessToken

    def upload_file(self,fileFrom,fileTo):

        for root, dirs, files in os.walk(fileFrom, fileTo):
            relative_path = os.path.relpath(local_path,fileFrom)
            dropbox_path=os.path.join(fileTo,relative_path)
        
        with open(self.local_path,'rb') as f:
            dbx.files_upload(f.read(),dropbox_path, mode= WriteMode('overwrite'))
    

        def main():
            AccessToken = '4MdHONpUTo0AAAAAAAAAAV7lnLpivlSwWfOtRErOTPWvFfaG1yjDCnf_DCnAxb90'
            transferData = TransferData(AccessToken)
            fileFrom=input("please enter the file path: ")
            fileTo=input("please enter the full path: ")
            transferData.upload_files(fileFrom, fileTo)
            print("YAY! the file has been moved 🥳🥳🥳")


