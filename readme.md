本数据集针对于垃圾分类的抓取网络设计
分为四个文件夹和一个txt，可以根据需求进行增减，后文为更新日志
<--------------------------------------------------->  
version--2021/4/12 
增加数据集采集流程代码，具体执行如下： 
1. 配置环境变量 
2. roslaunch kinect show.launch --启动kinect相机并查看相机图像 
3. roslaunch kinect save.launch --存储当前rgb和点云信息，注意每次采集之前需要修改save.launch内部的路径 




<--------------------------------------------------->  
version--2021/3/8

暂定标注格式为：
0		--所属小类编号
102 230		--下两行代表二维垃圾位置的矩形框，其不含旋转
302 101		--
253 319		--下四行代表二维抓取框，包含旋转
309 324 	--
307 350 	--
251 345		--

每7行代表图片中的一个垃圾

category.txt说明：
3		--小类数量
bottle		--小类名称
cigeratte	--
paper		--
2		--大类数量
recycle		--大类名称
unrecycle	--
0		--小类与大类的所属关系
1		--
0		--

