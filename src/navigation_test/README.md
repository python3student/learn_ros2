# Install

安装 gmapping 包(用于构建地图):sudo apt install ros-neotic-gmapping

安装地图服务包(用于保存与读取地图):sudo apt install ros-neotic-map-server

安装 navigation 包(用于定位以及路径规划):sudo apt install ros-neotic-navigation

# Error

````bash
无法定位软件包 ros-neotic-gmapping
无法定位软件包 ros-neotic-map-server
无法定位软件包 ros-neotic-navigation
````
````bash
sudo sh -c '. /etc/lsb-release && echo "deb http://mirrors.ustc.edu.cn/ros/ubuntu/ `lsb_release -cs` main" > /etc/apt/sources.list.d/ros-latest.list'
````

````bash
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
````
````bash
sudo apt update
````

# control

````bash
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >

t : up (+z)
b : down (-z)

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

CTRL-C to quit
````

