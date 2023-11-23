import rospy
import random
from geometry_msgs.msg import Twist


def main() -> None:

    rospy.init_node("rand_move")

    sim = rospy.Publisher(name="/car/cmd_vel", data_class=Twist, queue_size=10)
    message = Twist()

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        message.linear.x, message.linear.y, message.linear.z = (
            random.random() * 30,
            # random.random() * 30 - 15,
            0,
            0,
        )
        message.angular.x, message.angular.y, message.angular.z = (
            0,
            0,
            random.random() * random.random() * 16,
        )

        sim.publish(message)
        rate.sleep()


if __name__ == "__main__":
    main()
