#!/usr/bin/env python

import rclpy
import time
from rclpy.node import Node

class HeartbeatNode(Node):
    def __init__(self, rover_name, timer_period=0.2):
        self._rover_name = rover_name
        super().__init__(self._rover_name) #super is called to initialize the Node object
        self.create_timer(timer_period, self.timer_callback) #create a timer with callback duration and timer function

    def timer_callback(self):
        ros_time_stamp = self.get_clock().now()
        self.get_logger().info(self._rover_name + " is alive . . ." + str(ros_time_stamp))

def main(args=None):
    rclpy.init(args=args)
    node = HeartbeatNode(rover_name="mars_rover_1", timer_period=1.0)
    rclpy.spin(node) #keep the node alive until killed
    rclpy.shutdown()

def main2(args=None):
    rclpy.init(args=args)
    node2 = HeartbeatNode(rover_name="mars_rover_2", timer_period=1.0)
    rclpy.spin(node2)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
"""
def main(args=None):
    rclpy.init(args=args)

    node = Node('mars_rover_1')

    i = 0
    max_i = 50
    while i < max_i:
        i += 1
        ros_time_stamp = node.get_clock().now()
        #time_stamp = time.time()
        node.get_logger().info(str(i)+" Mars rover 1 is alive..."+str(ros_time_stamp))
        #print(str(i)+"Mars rover 1 is alive..."+str(time_stamp))
        time.sleep(1)

    #print("Mars rover 1 is alive...")
    node.destroy_node()
    rclpy.shutdown()

def main_shutdown(args=None):
    rclpy.init(args=args)
    print("Shutting down Mars rover 1...")
    rclpy.shutdown()

if __name__== '__main__':
    main()
    """