import gymnasium as gym
env = gym.make("CartPole-v1",render_mode="human")
observation, info = env.reset()
done = False
score=0
while not done:
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    score +=reward
    # Episode ends if either terminated OR truncated
    done = terminated or truncated

print(score)
env.close()
