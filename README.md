# Passport-Size-Photo-Cropping
Made a program using OpenCV which will help us to detect the face from an image and crop the face to a passport size image. The passport size photo is detected by using some mathematical calculations.

## The Project Involves
1. Detecting the face from any given image.
2. Cropping the image to a passport size photo and moving it to a new directory named Cropped
3. If the face is not detected, then the photo will be moved to another directory named Notdetected.

## Modules used:
1. **OpenCV** - It is used for face detection and cropping.
2. **OS** - It is used for traversing the file and moving the photo to another directory.

### Sample Input

<img align="center" src="Original/sample_1.jpg?raw=true" width="250"> <img align="center" src="Original/sample_3.jpg?raw=true" width="250"> <img align="center" src="Original/sample_4.jpg?raw=true" width="250">

### Sample Output

<img align="center" src="Cropped/sample_1.jpg?raw=true" width="250"> <img align="center" src="Cropped/sample_3.jpg?raw=true" width="250"> <img align="center" src="Cropped/sample_4.jpg?raw=true" width="250">
