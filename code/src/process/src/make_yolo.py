import rospy
import cv2
import os

class make_yolo:
    path=""
    size=640        #image size
    def __init__(self):
        present=os.getcwd()
        cat=present.split('/')
        for i in range(1,len(cat)-4):
            self.path+="/"+cat[i]
        #image process
        self.path+="/image"
        file=os.listdir(self.path)
        for i in range(len(file)):
            if(len(file[i].split("."))!=2):
                continue
            image=cv2.imread(self.path+"/"+file[i])
            image_yolo=cv2.resize(src=image,dsize=(self.size,self.size), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(self.path+"/yolo/"+file[i],image_yolo)
        print("image transformation done")
        
        #annotation process
        self.path=self.path[:-5]
        self.path+="annotation"
        an=os.listdir(self.path)
        for i in range(len(an)):
            if(len(an[i].split("."))!=2):
                continue
            a=os.open(self.path+"/"+an[i],"r")
            




if __name__ == '__main__':
    a=make_yolo()