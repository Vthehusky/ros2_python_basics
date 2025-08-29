#!/usr/bin/env python

import rclpy

def main(args=None):
    rclpy.init(args=args)
    print("Mars rover 1 is alive...")
    rclpy.shutdown()

def main_shutdown(args=None):
    rclpy.init(args=args)
    print("Shutting down Mars rover 1...")
    rclpy.shutdown()

if __name__== '__main__':
    main()