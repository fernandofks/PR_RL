from stable_baselines3 import DQN
import gymnasium as gym
from stable_baselines3.common.logger import configure
from stable_baselines3.common.evaluation import evaluate_policy

tmp_path = "./results/"
new_logger = configure(tmp_path, ["stdout", "csv", "tensorboard"])

env = gym.make('LunarLander-v2')
model = DQN(policy = "MlpPolicy", env = env, tau=1.0, target_update_interval=100)

model.set_logger(new_logger)
model.learn(total_timesteps=100000)

mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)
print(f'Mean reward: {mean_reward} +/- {std_reward:.2f}')

model.save("./models/lunar_lander_1_100")

print('modelo treinado')
env = gym.make('LunarLander-v2', render_mode='human')
# obs, info = env.reset()
(obs,_) = env.reset()

for i in range(300):
    action, _state = model.predict(obs, deterministic=True)
    obs, reward, done, truncated, info = env.step(action)
    env.render()
    print(i)
    if done:
      (obs,_) = env.reset()
