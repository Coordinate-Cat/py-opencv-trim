import cv2

image = cv2.imread('sample_img.jpg')
 
cascade_file = 'haarcascade_frontalface_alt2.xml'
cascade_face = cv2.CascadeClassifier(cascade_file)
 
face_list = cascade_face.detectMultiScale(image, minSize=(30, 30))
 
for (x, y, w, h) in face_list:
    border_color = (255, 0, 0)
 
    border_size = 2
    cv2.rectangle(image, (x, y), (x+w, y+h), border_color, thickness=border_size)

for i, (x, y, w, h) in enumerate(face_list):
    trim = image[y: y+h, x:x+w]
    cv2.imwrite('cut' + str(i+1) + '.jpg', trim)
 
cv2.imwrite('sample_out.jpg', image)
