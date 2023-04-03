import cv2
import os

Og_dir = 'E:\Project\Passport_Photo\Passport-Size-Photo-Cropping-Using-OpenCV\Original'
Crp_dir = 'E:\Project\Passport_Photo\Passport-Size-Photo-Cropping-Using-OpenCV\Cropped\\'
notDetect_dir = 'E:\Project\Passport_Photo\Passport-Size-Photo-Cropping-Using-OpenCV\\NotDetected\\'

for file_name in os.listdir(Crp_dir):
    file = Crp_dir + file_name
    os.remove(file)

for file_name in os.listdir(notDetect_dir):
    file = notDetect_dir + file_name
    os.remove(file)

def ImageRotation(image):
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

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

for filename in os.listdir(Og_dir):
    image = cv2.imread(os.path.join(Og_dir, filename))
    print(filename)
    if image is None:
        print(filename," - Image not found (Corrupt Image)")
        continue

    faces,new_image = ImageRotation(image)
    height,width,useless=new_image.shape

    if len(faces) == 0:
        cv2.imwrite(os.path.join(notDetect_dir, filename), image)
        continue

    for (x, y, w, h) in faces:
        a = int(h*0.5)
        o=a
        b = int(w*0.45)
        p=b

        if (y-a<0):
            a = y
        if (x-b<0):
            b = x
        if((y+h+a-10)>height):
            o=height
        if((x+w+b)>width):
            p=width
        if((y+h+o-10)-(y-h)<=200 or ((x+w+p)-(x-b)<=200)):
            cv2.imwrite(os.path.join(notDetect_dir, filename), image)
            break

        cropped_face = new_image[y-a:y+h+o-10, x-b:x+w+p]
        cv2.imwrite(os.path.join(Crp_dir, filename), cropped_face)
        break

print("Executed")
