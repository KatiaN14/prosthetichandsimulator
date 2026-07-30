# EMG Basics for Prosthetic Control

## What is EMG?

- **Definition**: Electromyography (EMG) is a technique for evaluating and recording the electrical activity produced by skeletal muscles.
- **How it works**: Muscles generate electrical potentials when activated. EMG sensors (electrodes) placed on the skin detect these potentials.
- **Applications in neuroengineering**:
  - Prosthetic control (e.g., bionic arms).
  - Rehabilitation (e.g., physical therapy monitoring).
  - Human-computer interfaces (e.g., gesture recognition).

## Types of EMG

- surface EMG: Assesses muscle function by recording muscle activity from the surface above the muscle on the skin, needs at least a pair of electrodes (to record potential difference).
- intramuscular EMG: different type of needles exists for different purposes, but superficial muscle activity can contaminate the recording of deeper muscles. First resting activity is assessed and later the procedure moves onto voluntary contractions. The electrode has to be placed at various locations to obtain an accurate study. 


## EMG Signal Properties

- **Frequency range**: Typically **20-500 Hz** (most energy between 50-150 Hz).
- **Amplitude range**: 0.1 mV to 10 mV (depends on muscle, electrode placement, and amplification).
- **Sampling rate**: Usually **1000-2000 Hz** (to avoid aliasing, per Nyquist theorem).

## Noise Sources in EMG

   Noise Type          | Cause                          | Frequency Range       | Mitigation Strategy               |
 |---------------------|--------------------------------|-----------------------|-----------------------------------|
 | Motion artifacts    | Movement of electrodes/cables   | < 20 Hz               | High-pass filter (e.g., 20 Hz)    |
 | Power-line interference | AC power (50/60 Hz)        | 50 Hz or 60 Hz        | Notch filter at 50/60 Hz          |
 | Electrode noise     | Poor skin contact              | Broadband            | Use gel, ensure good contact      |
 | EMG crossover       | Signals from nearby muscles     | 20-500 Hz             | Careful electrode placement       |

## EMG for Hand Gesture Recognition

- **Target gestures**: We will classify **4 gestures** for this project:
  1. **Hand open** (all fingers extended).
  2. **Hand close** (fist).
  3. **Grasp** (e.g., cylindrical grasp).
  4. **Pinch** (thumb + index finger).
- **Electrode placement**:
  - Typically on the **forearm** (e.g., flexor/extensor muscles).
  - Example: 8 electrodes around the forearm for NinaPro.

## Key Preprocessing Steps

1. **Filtering**:
   - High-pass filter (e.g., 20 Hz) to remove motion artifacts.
   - Low-pass filter (e.g., 500 Hz) to remove high-frequency noise.
   - Notch filter (50/60 Hz) to remove power-line interference.
2. **Full-wave rectification**: Convert negative amplitudes to positive (simplifies feature extraction, avoids null average, equivalent to taking the absolute value of the signal).
3. **Segmentation**: Split continuous EMG into windows (e.g., 150-300 ms) for gesture classification.
4. **Feature extraction**:
   - Time-domain: Mean absolute value (MAV), variance (VAR), root mean square (RMS).
   - Frequency-domain: Power spectral density (PSD), median frequency.

## Other uses

- wearable cockpit for pilots 
- silent speech recognition (thtrough observing muscles associated with speech)

