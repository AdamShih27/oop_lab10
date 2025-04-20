import numpy as np
import gymnasium as gym
from typing import TYPE_CHECKING, Optional
from custom_gymnasium.utils.base_lander import BASE_LANDER

class CustomLunarLander_v1(BASE_LANDER):
    def __init__(
        self,
        render_mode: Optional[str] = None,
        continuous: bool = False,
        gravity: float = -10.0,
        enable_wind: bool = False,
        wind_power: float = 15.0,
        turbulence_power: float = 1.5,
        fuel: float = 100,):
        pass

        '''
        Task:
        - Implement a custom lunar lander environment where the lander has a fuel tank of size `fuel`.
        '''
        # =====================type your code here=====================
        
        
        # =============================================================

    def reset(
        self,
        *,
        seed: Optional[int] = None,
        options: Optional[dict] = None,):
        pass
        '''
        Task:
        - Reset the fuel tank to its original size.
        '''
        # =====================type your code here=====================
        
        # =============================================================
        
    def step(self, action):
        pass
        '''
        Task:
        - The lander can only move if it has fuel left. If the fuel is exhausted, the lander can no longer move.
        
        Hint:
        - If the lander moves, the fuel tank should be decremented by 1.
        - If the lander doesn't move, the fuel tank should remain the same.
        '''
        # =====================type your code here=====================
        
        # =============================================================
