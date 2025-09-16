#!/usr/bin/env python

import rclpy
import time
from rclpy.node import Node
import random

class MarsRoverSystemsTemperatureNode(Node):
    def __init__(self):
        super().__init__('temperature_monitor')
        self.get_logger().info('Temperature Monitor Node has been started . . . . . . . ')

        self.temperature_threshold = 70.0
        self.timer = self.create_timer(1.0, self.monitor_temperature_callback)

    def get_temperature(self):
        latest_temperature = random.uniform(20.0, 100.0)
        return latest_temperature

    def monitor_temperature_callback(self):
        current_temperature = self.get_temperature()
        ros_time_stamp = self.get_clock().now()
        if current_temperature>self.temperature_threshold:
            self.get_logger().warn("The current temperature for the rover is: " + str(current_temperature) + " degree Celcius at time: " + str(ros_time_stamp))
        else:
            self.get_logger().info("The current temperature for the rover is: " + str(current_temperature) + " degree Celcius at time: " + str(ros_time_stamp))

def start_monitor(args=None):
    rclpy.init(args=args)
    node = MarsRoverSystemsTemperatureNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    start_monitor()
    
"""
class MarsRoverSystemsNode(Node):
    def __init__(self, rover_name, timer_period=0.2):
        self._rover_name = rover_name
        super().__init__(self._rover_name)
        self.create_timer(timer_period, self.timer_callback)

    def get_temperature(self):
        latest_temperature = random.uniform(20.0, 100.0)
        return latest_temperature

    def timer_callback(self):
        current_temperature = self.get_temperature()
        ros_time_stamp = self.get_clock().now()
        if current_temperature>70.0:
            self.get_logger().warn("The current temperature for " + self._rover_name + " is: " + str(current_temperature) + " degree Celcius at time: " + str(ros_time_stamp))
        else:
            self.get_logger().info("The current temperature for " + self._rover_name + " is: " + str(current_temperature) + " degree Celcius at time: " + str(ros_time_stamp))

def start_monitor(args=None):
    rclpy.init(args=args)
    node = MarsRoverSystemsNode(rover_name="mars_rover_1", timer_period=1.0)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    start_monitor()        
"""