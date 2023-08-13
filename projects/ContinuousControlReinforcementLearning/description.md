

<div class='PortMarker'>

### Description

<div class='StyledHR StyledHRProjects'></div>

Continuous Control with Double-Jointed Arm:
Project Overview: In this advanced project, a double-jointed arm was trained to follow a moving target, showcasing the capabilities of continuous control within a complex environment provided by Unity.

**Challenge**: The challenge was to control the arm's two joints, utilizing a continuous action space ranging between [-1:1], to apply torque and maintain the tip of the arm at the target's location. With a detailed observation space of 33 variables, including the arm's position, rotation, velocity, and angular velocities, the model was meticulously tuned to achieve precision.

**Reward Structure**: Rewards were strategically structured to motivate the correct positioning of the arm, with a reward of +0.1 for alignment with the target and 0.0 otherwise.

**Learning Environment**: The learning environment featured 20 parallel agents interacting independently, leveraging the DDPG algorithm to capitalize on individual experiences.

**Outcome**: The project's success was marked by achieving an average score of +30 points over 100 episodes, demonstrating the efficiency of the learning algorithm in handling continuous control in a multi-agent context.

**Visual Demonstration**: A GIF showcasing the trained network's performance visually illustrates the prowess of the model in accurately and consistently controlling the double-jointed arm to align with the moving target.