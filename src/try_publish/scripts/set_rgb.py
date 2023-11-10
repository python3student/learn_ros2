#! /usr/bin/env python

import rospy

if __name__ == "__main__":
    rospy.init_node("hehe")
    rospy.set_param("/t1/background_r", 202)
    rospy.set_param("/t1/background_g", 158)
    rospy.set_param("/t1/background_b", 122)
    # rospy.set_param("background_r",255)
    # rospy.set_param("background_g",255)
    # rospy.set_param("background_b",255)  # 调用时，需要传入 __ns:=xxx
