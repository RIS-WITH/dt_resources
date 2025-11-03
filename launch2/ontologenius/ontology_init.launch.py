import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, TextSubstitution

def generate_launch_description():
    DeclareLaunchArgument(
        'language',
        default_value='en'
    )
    DeclareLaunchArgument(
        'root',
        default_value='none'
    )

    ontologenius_launch_file = os.path.join(
        get_package_share_directory('ontologenius'),
        'launch',
        'ontologenius_multi_full.py'
    )
    
    custom_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(ontologenius_launch_file),
        launch_arguments={
            'language': LaunchConfiguration('language'),
            'intern_file': 'none',
            'config_file': os.path.join(get_package_share_directory('dt_resources'), "configs/ontologenius.yaml"),
            'display': 'false',
            'root': LaunchConfiguration('root'),
            'files': (
                os.path.join(get_package_share_directory('common_ground_ontology'), "CG_root.owl") + " " +
                os.path.join(get_package_share_directory('common_ground_ontology'), "ris_agents.owl") + " " +
                os.path.join(get_package_share_directory('dt_resources'), "ontologies/dt_objects.owl") + " " +
                os.path.join(get_package_share_directory('dt_resources'), "ontologies/dt_humans.owl")
            ),
            'robot_file': 'none',
            'human_file': 'none'
        }.items()
    )
    
    return LaunchDescription([
        custom_launch
    ])