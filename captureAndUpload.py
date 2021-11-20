import cv2
import dropbox
import time
import random

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".jpg"
        cv2.imwrite(img_name, frame)
        result = False
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return(img_name)

def upload_file(img_name):
    print("Working... ")
    access_token = 'n1eOruYs7b8AAAAAAAAAAY8Sna0HqK1c8V09x62pDD2gmonxIHy-O7vss8nS2EUB'
    file_name = img_name
    file_from = file_name
    file_to = "/Sneaky Images/" + img_name
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(),file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File Loaded")

def main():
    start_time = time.time()
    while(True):
        if((time.time()-start_time)>=60):
            start_time = time.time()
            name = take_snapshot()
            upload_file(name)

main()