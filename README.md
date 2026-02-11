# Optical Cavity & Gaussian Beam Calculator

Python tool for calculating Gaussian beam parameters and optical cavity properties, including cavity beam waist, mode matching, and fiber collimation.

---

## Overview

This script computes:

- Cavity beam waist for a two-mirror resonator
- Cavity stability parameters (g-parameters)
- Focused beam waist using a thin lens
- Rayleigh range of the focused beam
- Collimated beam waist from a single-mode fiber

It is designed for students and researchers working in laser physics, quantum optics, and optical cavity experiments.

---

## Features

- Symmetric two-concave mirror cavity calculations
- Gaussian beam transformation through a lens
- Rayleigh range computation
- Fiber collimator beam estimation
- Clear unit handling (meters, microns, millimeters)

---

## Theory Background

### Cavity Stability Condition

A two-mirror cavity is stable when:

```
0 < g1 * g2 < 1
```

where:

```
g1 = 1 - L/R1
g2 = 1 - L/R2
```

---

### Cavity Beam Waist

The cavity waist is calculated using Gaussian beam resonator theory:

```
w0 = sqrt( (λL/π) * sqrt( g1g2(1 - g1g2) / (g1 + g2 - 2g1g2)^2 ) )
```

---

### Thin Lens Transformation

Focused waist after a lens:

```
w0 = (λ f) / (π w_in)
```

Rayleigh range:

```
zR = π w0² / λ
```

---

## Requirements

- Python 3.x
- NumPy

Install NumPy with:

```bash
pip install numpy
```

---

## Usage

1. Modify cavity parameters inside the script:
   - Cavity length `L`
   - Mirror radius `R`
   - Wavelength `lambda0`
   - Lens focal length `f`
   - Input beam waist

2. Run:

```bash
python mode_matching_cavity.py
```

---

## Applications

- Fabry–Pérot cavity design
- Mode-matching optimization
- Fiber-to-cavity coupling
- Laser beam propagation analysis
- Quantum optics experiments

---
