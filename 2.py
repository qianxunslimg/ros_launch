from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Declare arguments
    declared_arguments = []
    declared_arguments.append(
        DeclareLaunchArgument(
            "namespace1",
            default_value="turtlesim1",
            description="Namespace for turtlesim1.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "namespace2",
            default_value="turtlesim2",
            description="Namespace for turtlesim2.",
        )
    )

    # Initialize Arguments
    namespace1 = LaunchConfiguration("namespace1")
    namespace2 = LaunchConfiguration("namespace2")

    # Create Nodes
    turtlesim_node1 = Node(
        package="turtlesim",
        executable="turtlesim_node",
        name="sim",
        namespace=namespace1
    )

    turtlesim_node2 = Node(
        package="turtlesim",
        executable="turtlesim_node",
        name="sim",
        namespace=namespace2
    )
    #this is wrong
    mimic_node = Node(
        package="turtlesim",
        executable="mimic",
        name="mimic",
        remappings=[
            ("/input/pose",  f"{namespace1}/turtle1/pose"),
            ("/output/cmd_vel", f"{namespace2}/turtle1/cmd_vel")
        ]
    )
    # # this is right
    # mimic_node = Node(
    # package="turtlesim",
    # executable="mimic",
    # name="mimic",
    # remappings=[
    #     ("input/pose", "turtlesim1/turtle1/pose"),
    #     ("output/cmd_vel", "turtlesim2/turtle1/cmd_vel")
    #     ]   
    # )

    return LaunchDescription(declared_arguments + [turtlesim_node1, turtlesim_node2, mimic_node])

