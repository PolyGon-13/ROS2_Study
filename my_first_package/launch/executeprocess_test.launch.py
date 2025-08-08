import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
	user_home=os.path.expanduser('~')

	return LaunchDescription([
		ExecuteProcess(
			cmd=['ls','-l',user_home],
			output='screen'
		),
		ExecuteProcess(
			cmd=['echo','Hello world!'],
			output='screen'
		),
	])