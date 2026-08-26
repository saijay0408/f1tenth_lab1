# Lab 1: Intro to ROS 2

## Written Questions

### Q1: During this assignment, you've probably ran these two following commands at some point: ```source /opt/ros/foxy/setup.bash``` and ```source install/local_setup.bash```. Functionally what is the difference between the two?

Answer: The first one sources the actual ROS 2 install itself - it's what sets up all the env vars so `ros2` as a command even exists, plus all the base message types etc. You need this one no matter what, it's the foundation. The second one is for YOUR workspace specifically, the stuff that gets built when you run colcon build. It doesn't replace the first one, it just adds your own packages (like lab1_pkg) on top of it so ros2 run can actually find them. If you only source the first one, ros2 works fine but has no idea your package exists.

### Q2: What does the ```queue_size``` argument control when creating a subscriber or a publisher? How does different ```queue_size``` affect how messages are handled?

Answer: It's basically how many messages can sit in the buffer if the subscriber can't keep up with how fast they're coming in. Once that buffer fills up, old ones start getting dropped to make room. So a bigger number means you can survive short bursts without losing data, but if your subscriber is consistently too slow you'll just end up processing old/stale messages with a delay. Smaller (like 1) means you basically always get the latest message and nothing older, which is usually what you want for something like steering commands where an old value is worse than no value.

### Q3: Do you have to call ```colcon build``` again after you've changed a launch file in your package? (Hint: consider two cases: calling ```ros2 launch``` in the directory where the launch file is, and calling it when the launch file is installed with the package.)

Answer: Depends how you're running it. If you point ros2 launch directly at the file in your src folder, no, it just reads whatever's there right now. But if you're launching it through the package (ros2 launch lab1_pkg lab1_launch.py), that's actually reading the copy that got placed in install/ during the build, so your edit won't show up until you rebuild. Only exception is if you built with --symlink-install, since then install/ just links back to your src files instead of copying them.
