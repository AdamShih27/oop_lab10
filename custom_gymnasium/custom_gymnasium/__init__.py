from gymnasium.envs.registration import registry, register, make, spec

register(
    id='CustomLunarLander-v1',
    entry_point='custom_gymnasium.envs:CustomLunarLander_v1',
    max_episode_steps=4096,
)