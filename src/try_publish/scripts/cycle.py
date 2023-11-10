import rospy
import random
from geometry_msgs.msg import Twist

# import tools


def main() -> None:
    # linear = 0, 0, 0
    # linear = random.random() * 3, random.random() * 3, 0
    # angular = 0, 0, random.random() * 2

    rospy.init_node("sim_cycle")

    sim = rospy.Publisher(name="/oth/turtle1/cmd_vel", data_class=Twist, queue_size=10)
    message = Twist()
    # print(message)
    # sim.publish(message)

    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        message.linear.x, message.linear.y, message.linear.z = (
            random.random() * 30 - 15,
            random.random() * 30 - 15,
            0,
        )
        message.angular.x, message.angular.y, message.angular.z = (
            0,
            0,
            random.random() * random.random() * 16 - 8,
        )

        sim.publish(message)
        rate.sleep()


def tool_test() -> None:
    import tools

    # print("233")
    rospy.init_node("sim_cycle")
    rospy.loginfo("{0}333".format(tools.num))


if __name__ == "__main__":
    main()
    # tool_test()
