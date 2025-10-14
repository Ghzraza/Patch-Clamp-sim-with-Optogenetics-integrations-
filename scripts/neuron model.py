# neuron_model.py
# Author: Ghazal Raza
# Purpose: Define modular neuron and synapse functions for LIF simulations

import numpy as np

def lif_neuron_step(V_prev, g_L, E_L, g_exc, E_exc, g_inh, E_inh, C_m, dt, V_th, V_reset):
    """
    Single time step update for a leaky integrate-and-fire neuron.
    """
    I_syn = g_exc*(E_exc - V_prev) + g_inh*(E_inh - V_prev)
    dV = (g_L*(E_L - V_prev) + I_syn)/C_m * dt
    V = V_prev + dV
    if V >= V_th:
        V = V_reset
    return V

def update_synapse(g_prev, tau, dt, g_max, spike):
    """
    Update synaptic conductance (exponential decay + spike increment)
    """
    g = g_prev*np.exp(-dt/tau) + g_max*spike
    return g
