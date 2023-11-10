#! /usr/bin/env python
"""
    发布方:
        循环发送消息

"""
import rospy
from publish.msg import Person


def main() -> None:
    # 1.初始化 ROS 节点
    rospy.init_node("talker_person_p")
    # 2.创建发布者对象
    pub = rospy.Publisher("chatter_person", Person, queue_size=10)
    # 3.组织消息
    person = Person()
    person.name = "张三"
    person.age = 18
    person.height = 0.75

    # 4.编写消息发布逻辑
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(person)  # 发布消息
        rate.sleep()  # 休眠
        rospy.loginfo(
            "姓名:{0}, 年龄:{1}, 身高:{2}".format(person.name, person.age, person.height)
        )


if __name__ == "__main__":
    main()
