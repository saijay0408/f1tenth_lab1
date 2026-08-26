from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    v_arg = DeclareLaunchArgument('v', default_value='1.0')
    d_arg = DeclareLaunchArgument('d', default_value='0.5')

    talker_node = Node(
        package='lab1_pkg',
        executable='talker',
        name='talker',
        parameters=[{
            'v': LaunchConfiguration('v'),
            'd': LaunchConfiguration('d'),
        }]
    )

    relay_node = Node(
        package='lab1_pkg',
        executable='relay',
        name='relay',
    )

    return LaunchDescription([
        v_arg,
        d_arg,
        talker_node,
        relay_node,
    ])
