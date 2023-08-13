

<div class='PortMarker'>

### Description

<div class='StyledHR StyledHRProjects'></div>

Collaboration and Competition in Tennis

Project Overview: In this innovative project, a sophisticated collaborative training approach was implemented to teach two agents to play tennis against each other in a Tennis environment.

**Objective**: The agents, each controlling a racket, aimed to keep the ball in play by hitting it over the net. Collaboration and competition were integral, with the goal set to achieve an average score of +0.5 over 100 consecutive episodes.

**Reward Structure**: Rewards were structured to incentivize successful play, with a reward of +0.1 for successful volleys and a penalty of -0.01 for letting the ball hit the ground or sending it out of bounds.

**Observation and Action Space**: The complexity of the environment was captured through an observation space encompassing 24 variables, detailing the position and velocity of both the ball and racket. The agents had access to two continuous action spaces, governing movement left/right and up/down within the range of [-1:1].

**Scoring Mechanism**: The scoring mechanism involved summing the rewards for each agent per episode, then taking the maximum of the two scores, yielding a single score per episode.

**Solution**: The environment's solution was defined by an average score of at least +0.5 over 100 episodes, considering the maximum of the two agents' scores.

**Visual Demonstration**: A GIF displaying the trained network in action visually represents the success of the model in learning both cooperative and competitive strategies, underscoring the model's ability to handle nuanced multi-agent interactions.

**Conclusion**: This project serves as an excellent demonstration of the potential applications of machine learning in creating intelligent agents capable of both collaboration and competition, with direct relevance to more complex real-world tasks.