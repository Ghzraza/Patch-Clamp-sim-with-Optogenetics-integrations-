# optogenetics.py
# Author: Ghazal Raza
# Purpose: Define light-gated conductances for optogenetic simulations

import numpy as np

def light_conductance(t_index, light_on_array, g_max):
    """
    Returns light-induced conductance at a given timestep
    """
    return g_max * light_on_array[t_index]
