from send_message import sendMsg
from drive_upload import uploadFile


file = 'assets/kenndypic.png'
file_id = uploadFile(file)
url = 'https://drive.google.com/file/d/{}/view?usp=sharing'.format(file_id)

sendMsg(url, '+2348138077441')