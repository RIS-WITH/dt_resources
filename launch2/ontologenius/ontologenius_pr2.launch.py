import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    ontologenius_launch_file = os.path.join(
        get_package_share_directory('dt_resources'),
        'launch',
        'ontologenius',
        'ontology_init.launch.py'
    )
    
    custom_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(ontologenius_launch_file),
        launch_arguments={
            'language': 'pr2',
            'root': 'pepper'
        }.items()
    )
    
    return LaunchDescription([
        custom_launch
    ])