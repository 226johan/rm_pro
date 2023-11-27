import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import Command

from launch_ros.actions import Node

def generate_launch_description():
    params_file = os.path.join(
        get_package_share_directory('rm_vision_bringup'), 'config', 'params.yaml')

    robot_description = Command(['xacro ', os.path.join(
        get_package_share_directory('rm_pioneer_gimbal_description'),
        'urdf', 'pioneer_gimbal.urdf.xacro')])

    detector_node = Node(
        package='armor_detector',
        executable='armor_detector_node',
        emulate_tty=True,
        output='screen',
        parameters=[params_file],
        arguments=['--ros-args', '--log-level', 'armor_detector:=INFO'],
    )

    processor_node = Node(
        package='armor_processor',
        executable='armor_processor_node',
        output='screen',
        emulate_tty=True,
        parameters=[params_file],
        arguments=['--ros-args', '--log-level', 'armor_processor:=INFO'],
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description,
                     'publish_frequency': 1000.0}]
    )

    return LaunchDescription([
        detector_node,
        processor_node,
        robot_state_publisher,
    ])
