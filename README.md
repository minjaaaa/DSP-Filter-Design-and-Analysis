# Digital Signal Processing: Sensor System for an Autonomous Vehicle

This project focuses on the analysis, design, and implementation of digital filters for processing ultrasonic distance sensor signals, with the primary goal of removing impulse noise and Gaussian noise in autonomous vehicle systems.

## System Overview

In autonomous driving systems, the reliability of sensor data is critical. Ultrasonic sensors often produce impulse noise (false spikes) caused by signal reflections or interference, as well as continuous Gaussian noise. This project demonstrates a cascaded filtering architecture designed to obtain a stable and reliable sensor signal.

## Key Methods and Algorithms

The project uses the `scipy.signal` and `numpy` Python libraries to perform the following operations:

- **Spectral Analysis:** Fast Fourier Transform (FFT) (`fft`, `fftfreq`) for identifying the characteristics of the noise.
- **Linear Filters:** Design and implementation of FIR (window method) and IIR (Butterworth) filters.
- **Nonlinear Filters:** Implementation of a median filter (`medfilt`) for robust impulse noise removal.
- **Signal Smoothing:** Application of a Moving Average (MA) filter to reduce Gaussian noise.
- **Stability Analysis:** Evaluation of poles and zeros (`tf2zpk`) and group delay (`group_delay`).

## Cascaded Filtering Architecture

To achieve optimal filtering performance, a two-stage cascaded filtering architecture is implemented:

1. **Stage 1 (Median Filter):** Removes impulsive outliers while preserving sharp signal transitions.
2. **Stage 2 (Moving Average Filter):** Smooths the filtered signal to reduce Gaussian noise and provide stable measurements for vehicle control.

## Results

The project demonstrates the influence of selected filter parameters (window size and filter order) through:

- Amplitude and phase response (Bode plots).
- Step response analysis (transient behavior and delay).
- System stability in the Z-plane.

## Technologies

- **Programming Language:** Python 3.x
- **Libraries:** `numpy`, `scipy`, `matplotlib`, `pandas`
- **Environment:** Jupyter Notebook

---

*Developed as part of the Digital Signal Processing course in an engineering study program.*