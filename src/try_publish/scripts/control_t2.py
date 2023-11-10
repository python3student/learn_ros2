import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


p0 = Pose()
p0.x, p0.y, p0.theta, p0.linear_velocity, p0.angular_velocity = 0, 0, 0, 0, 0


position = {
    "t1": p0,
    "t2": p0,
}


def control(p: tuple):
    # rospy.init_node("control")
    move = Twist()
    move.linear.x, move.linear.y = p[0], p[1]
    send = rospy.Publisher(name="/oth/t2/cmd_vel", data_class=Twist, queue_size=10)
    send.publish(move)


def cal_posion(pose: Pose, name_pose: [str, Pose]) -> None:
    # global position
    # rospy.init_node("ti_poaion")
    # ti_position = rospy.Publisher(name="t1_position")
    # print("名字：{0} \n 位子：{1}".format(type(name), position))
    name = name_pose[0]
    # x = pose.x
    # print("name: {0} x: {1}".format(name, x))
    position[name] = pose

    dy = position["t1"].y - position["t2"].y
    dx = position["t1"].x - position["t2"].x
    d_theta = 0
    control((dx, dy, d_theta))


def get_t1_position() -> Pose:
    rospy.init_node("get_t1")

    t1_position = rospy.Subscriber(
        name="/oth/turtle1/pose",
        data_class=Pose,
        callback=cal_posion,
        callback_args=["t1", Pose],
        queue_size=10,
    )
    t2_position = rospy.Subscriber(
        name="/oth/t2/pose",
        data_class=Pose,
        callback=cal_posion,
        callback_args=["t2", Pose],
        queue_size=10,
    )

    rospy.spin()
    print(233)


if __name__ == "__main__":
    get_t1_position()
