import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
def detect_faces(image_path):
    
    image = cv2.imread(image_path)
    if image is None:
        print("Could not read the image.")
        return
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

  
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Image with detected faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = "D:\\b_w SRK.jpeg"
detect_faces(image_path)
