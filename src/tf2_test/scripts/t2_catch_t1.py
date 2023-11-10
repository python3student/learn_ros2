import math
import rospy
import tf2_ros
from geometry_msgs.msg import Twist, TransformStamped

# from gazebo_msgs.msg import


def main():
    rospy.init_node("control_t2")

    buffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(buffer=buffer)

    control = rospy.Publisher(name="/t2/cmd_vel", data_class=Twist, queue_size=100)

    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        rate.sleep()
        try:
            trans: TransformStamped = buffer.lookup_transform(
                target_frame="t2", source_frame="turtle1", time=rospy.Duration(0)
            )

            twist = Twist()
            dx = trans.transform.translation.x
            dy = trans.transform.translation.y
            d = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))

            k = 3.18 if d >= 2 else 3.2
            twist.linear.x = k * d
            twist.angular.z = 2 * math.atan2(dy, dx)
            control.publish(twist)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
