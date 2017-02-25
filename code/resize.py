import glob
import cv2

glob_path = '../resources/face_224x224/*/ok/*.jpg'
image_path_list = glob.glob(glob_path)

for i, image_path in enumerate(image_path_list):
    if i % 100 == 0:
        print(i)
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, (224, 224))
    cv2.imsave(image_path, resized_image)