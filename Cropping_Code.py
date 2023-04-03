import cv2
import os

Og_dir = 'E:\Project\Passport_Photo\Original'
Crp_dir = 'E:\Project\Passport_Photo\Cropped\\'
notDetect_dir = 'E:\Project\Passport_Photo\\NotDetected\\'

def rotate_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=42)
    print(len(faces))
    if len(faces) == 0:
        for i in range(4):
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=42)
            if len(faces) != 0:
                return faces,image
    return faces,image

for file_name in os.listdir(Crp_dir):
    file = Crp_dir + file_name
    os.remove(file)

for file_name in os.listdir(notDetect_dir):
    file = notDetect_dir + file_name
    os.remove(file)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

for filename in os.listdir(Og_dir):
    image = cv2.imread(os.path.join(Og_dir, filename))
    print(filename)

    if image is None:
        print(filename," - Error 404: Image not found")
        continue

    faces,new_image = rotate_image(image)
    height,width,useless=new_image.shape

    if len(faces) == 0:
        cv2.imwrite(os.path.join(notDetect_dir, filename), image)
        continue

    for (x, y, w, h) in faces:
        u = int(h*0.5)
        o=u
        v = int(w*0.45)
        p=v

        if (y-u<0):
            u = y
        if (x-v<0):
            v = x
        if((y+h+u-10)>height):
            o=height
        if((x+w+v)>width):
            p=width
        if((y+h+o-10)-(y-h)<=200 or ((x+w+p)-(x-v)<=200)):
            cv2.imwrite(os.path.join(notDetect_dir, filename), image)
            break

        cropped_face = new_image[y-u:y+h+o-10, x-v:x+w+p]
        cv2.imwrite(os.path.join(Crp_dir, filename), cropped_face)
        break

print("Executed")
