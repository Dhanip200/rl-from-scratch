import gymnasium as gym
env = gym.make("CartPole-v1",render_mode="human")
observation, info = env.reset()
done = False
score=0
while not done:
    if observation[2]+observation[3] > 0:
        action = 1
    else:
        action = 0
    observation, reward, terminated, truncated, info = env.step(action)
    print(observation)
    score +=reward       

    # Episode ends if either terminated OR truncated
    done = terminated or truncated

print(score)
env.close()
