import os
import cv2

#vid=cv2.VideoCapture()
path = "thing\images"

images = []
print(os.listdir(path))

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
vaa=cv2.imread(images[-1])
width,height,channels=vaa.shape
sizee=(width,height)
#height=int(vid.get())

yeee=cv2.VideoWriter("eeee.mp4",cv2.VideoWriter_fourcc(*"mp4v"),0.5,(500,330))



for i in range (-1,count):
    vaa=cv2.imread(images[i])
    yeee.write(vaa)

    #print(sizee)

yeee.release()
print("done")
