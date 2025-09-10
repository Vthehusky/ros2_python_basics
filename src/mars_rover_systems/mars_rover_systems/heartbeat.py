#!/usr/bin/env python

import rclpy
import time
from rclpy.node import Node

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