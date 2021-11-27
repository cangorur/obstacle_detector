import math

import rospy
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Twist, PoseStamped, Pose, PoseWithCovarianceStamped, Point, Quaternion

from obstacle_detector.msg import Obstacles

rospy.init_node("analyze_obs")

# obj_id_to_follow = 3

quaternion = Quaternion()
quaternion.x = 0.0
quaternion.y = 0.0
quaternion.z = 0.0
quaternion.w = 1.0
robot_orientation = quaternion


def obstacles_callback(msg):
    # global obj_id_to_follow
    # print(msg)
    # import pdb;pdb.set_trace()
    obs_arr = msg.circles

    for i in range(len(obs_arr)):

        velocity_magnitude = math.sqrt(obs_arr[i].velocity.x * obs_arr[i].velocity.x + 
            obs_arr[i].velocity.y * obs_arr[i].velocity.y)

        if velocity_magnitude > 0.1:
            print('Walking human index: {}'.format(i))
            # pose = Pose()
            # pose.position.x = obs_arr[i].center.x
            # pose.position.y = obs_arr[i].center.y
            # pose.position.z = 0.0
            break

    # for marker in msg.markers:
    #     if marker.id == obj_id_to_follow:
    #         # marker.pose
    #         go_to_goal(marker.pose)
    #         break


obstacles_sub = rospy.Subscriber('obstacles', Obstacles, obstacles_callback)

print('Spinning')
rospy.spin() 