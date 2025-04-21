import numpy as np
import gymnasium as gym
from gymnasium import Env, spaces

class CustomLunarLander_v1(Env):
    
    metadata = {"render_modes": ["rgb_array"], "render_fps": 30}

    def __init__(self, gravity=-5.0, fuel=100, turbulence_power=1, render_mode=None):
        super(CustomLunarLander_v1, self).__init__()

        self.gravity = gravity
        self.initial_fuel = fuel
        self.fuel = fuel
        self.turbulence_power = turbulence_power
        self.render_mode = render_mode

        # Define action space (e.g. 4 actions: do nothing, left, main, right)
        self.action_space = spaces.Discrete(4)

        # Observation space: example [x, y, vx, vy, angle, ang_vel, leg1, leg2]
        self.observation_space = spaces.Box(
            low=np.array([-np.inf]*8, dtype=np.float32),
            high=np.array([np.inf]*8, dtype=np.float32),
            dtype=np.float32
        )

        self.state = None

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.fuel = self.initial_fuel
        self.state = np.zeros(8, dtype=np.float32)
        return self.state, {}

    def step(self, action):
        assert self.fuel >= 0, "Fuel should never go below 0"

        # Simulate dummy dynamics
        self.state = np.random.randn(8).astype(np.float32)

        reward = 0.0
        terminated = False
        truncated = False
        info = {}

        # Fuel consumption logic (only if action != 0)
        if action != 0 and self.fuel > 0:
            self.fuel -= 1
            reward += 1.0  # dummy reward for using thruster
        elif action != 0 and self.fuel <= 0:
            reward -= 1.0  # penalize trying to use thruster when empty

        # Terminate episode if fuel is out
        if self.fuel <= 0:
            terminated = True
            info["reason"] = "out_of_fuel"

        return self.state, reward, terminated, truncated, info

    def render(self):
        if self.render_mode == "rgb_array":
            return np.zeros((400, 600, 3), dtype=np.uint8)  # dummy image
        else:
            return None
