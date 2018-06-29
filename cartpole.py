import random
import gym.spaces                               # load framework

env = gym.make("FrozenLake-v0")                 # load environment

print(env.observation_space)                    # prints "Discrete 16," which means it's a 4x4 grid of 16
print(env.action_space)                         # prints "Discrete 4," meaning there are 4 directions (L/D/R/U)
score = 0                                       # declare score

for _ in range(10000):                          # runs 10000 episodes
    env.reset()                                 # resets environment to start state
    for t in range(100):
        x = random.randint(1, 2)                            # chooses random integer between 1 and 2
        # action = env.action_space.sample()                # defines "action" as taking one step in random direction
        observation, reward, done, info = env.step(x)       # takes action x
        env.render()                                        # displays environment
        if done:
            score += reward                     # change score: the reward is added to it each loop
            print(score)                        # 0.0 means it fell into a hole; 1.0 means it reached the goal
            break                               # stops running script when game ends

