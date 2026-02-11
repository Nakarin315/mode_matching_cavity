# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 10:07:17 2026

@author: nakarin
"""

import numpy as np

# ==============================
# CAVITY PARAMETERS
# ==============================

L = 2e-3          # Cavity length (m)
R = 10e-2         # Mirror radius of curvature (m)
lambda0 = 853e-9  # Laser wavelength (m)

# Symmetric two-concave-mirror cavity
# If one mirror is flat R2 = inf
R1 = R
R2 = R

# g-parameters (stability parameters)
g1 = 1 - L / R1
g2 = 1 - L / R2

# Cavity beam waist at the center of the cavity
w0_cavity = (
    np.sqrt(lambda0 * L / np.pi)
    * (g1 * g2 * (1 - g1 * g2) / (g1 + g2 - 2 * g1 * g2)**2)**(1/4)
)

print("Cavity beam waist:", round(w0_cavity * 1e6, 2), "micron")


# ==============================
# MODE MATCHING WITH ONE LENS
# ==============================

# Input Gaussian beam waist before the lens
input_beam_waist = 1.13e-3   # (m)

# Focal length of mode-matching lens
f = 200e-3  # (m)

# Beam waist at the focus of the lens
# Formula: w0 = λf / (π w_in)
w0_lens = lambda0 * f / (np.pi * input_beam_waist)

# Rayleigh range of the focused beam
z_r = np.pi * w0_lens**2 / lambda0

print("Focused beam waist:", round(w0_lens * 1e6, 2), "micron")
print("Focused beam diameter:", round(2 * w0_lens * 1e6, 2), "micron")
print("Rayleigh range:", round(z_r * 1e3, 2), "mm")


# ==============================
# BEAM WAIST FROM FIBER COLLIMATOR
# ==============================

f_collimator = 11e-3   # Focal length of fiber collimator (m)
MFD = 5.3e-6  # Fiber mode field diameter MFD (m), e.g. 780HP fiber

# Estimated collimated beam waist from fiber output
# Using Gaussian beam transformation through a lens
w_collimated = f_collimator * 4 * lambda0 / (np.pi * MFD) / 2

print("Collimated beam waist:", round(w_collimated * 1e3, 2), "mm")
