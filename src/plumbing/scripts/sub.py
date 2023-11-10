#! /usr/bin/env python

"""
    需求: 
        编写两个节点实现服务通信，客户端节点需要提交两个整数到服务器
        服务器需要解析客户端提交的数据，相加后，将结果响应回客户端，
        客户端再解析

    客户端实现:
        1.导包
        2.初始化 ROS 节点
        3.创建请求对象
        4.发送请求
        5.接收并处理响应

    优化:
        加入数据的动态获取


"""
# 1.导包
import rospy
from plumbing.srv import *
import sys

if __name__ == "__main__":
    # 优化实现
    argv = sys.argv
    # print(argv)
    if len(argv) == 5:
        # print("已适配参数")
        argv = argv[0:3]
        # print("launch适配参数: ", argv)
        rospy.logerr("launch适配参数: {0}".format(str(argv)))
    if len(argv) != 3:
        rospy.logerr("请正确提交参数")
        sys.exit(1)

    # 2.初始化 ROS 节点
    rospy.init_node("AddInts_Client_p")
    # 3.创建请求对象
    client = rospy.ServiceProxy("AddInts", AddInts)
    # 请求前，等待服务已经就绪
    # 方式1:
    # rospy.wait_for_service("AddInts")
    # 方式2
    client.wait_for_service()
    # 4.发送请求,接收并处理响应
    # 方式1
    # resp = client(3,4)
    # 方式2
    # resp = client(AddIntsRequest(1,5))
    # 方式3
    req = AddIntsRequest()
    # req.num1 = 100
    # req.num2 = 200

    # 优化
    # rospy.Rate(1)
    for i in range(10):
        req.num1 = int(int(argv[1]) + i)
        req.num2 = int(int(argv[2]) + i * 2)

        resp = client.call(req)
        rospy.loginfo("响应结果:%d", resp.sum)
        rospy.sleep(0.2)
    rospy.loginfo("全部结果已计算完成")
