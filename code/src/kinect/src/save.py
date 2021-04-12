#! /usr/bin/python2
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import message_filters
import numpy as np
from sensor_msgs.msg import PointCloud2
import pcl_ros

class save:
    bridge=CvBridge()
    path=""
    i=0
    def __init__(self):
        self.path=rospy.get_param("~path")
        sub_rgb=message_filters.Subscriber("/camera/rgb/image_color", Image, queue_size=10)
        sub_dep=message_filters.Subscriber("/camera/depth/points", PointCloud2, queue_size=10)
        sync = message_filters.ApproximateTimeSynchronizer([sub_rgb, sub_dep],10,0.1)  #allow_headerless=True
        sync.registerCallback(self.process)
    
    def process(self,rgb,depth):
        if (self.i>=2):
            return
        cv_image=self.bridge.imgmsg_to_cv2(rgb,desired_encoding='passthrough')
        pub=rospy.Publisher("input",PointCloud2,queue_size=10)
        rospy.Rate(100)
        pub.publish(depth)
        rospy.sleep(2)

        if (cv2.imwrite(self.path,cv_image)):
            print("picture saved to "+self.path)
        else:
           print("picture save fail!")
        self.i+=1
        return

if __name__=='__main__':
    this=rospy.init_node('save', anonymous=False)
    ss=save()
    
    rospy.spin()

