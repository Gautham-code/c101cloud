import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from)
        dbx.files_upload(f.read(), file_to)

def filePath() :
    access_token = '/'
    transferData = TransferData(access_token)

    file_from = input("Enter the file name:")
    file_to = input("enter the full path to upload to dropbox:- ")  
    transferData.upload_file(file_from, file_to)
    print("file not found")


filePath()
