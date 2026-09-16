# Prosthetic Hand Simulation — EMG Gesture Classification

A small, self-contained neuroengineering project: classifying 12 finger/thumb
gestures from surface EMG signals, as a first step toward EMG-driven prosthetic
hand control. Built as an entry point into myoelectric prosthesis control — the
broader problem this project sits within.

## Goals

- Learn the fundamentals of EMG signal processing (filtering, windowing, feature
  extraction) from first principles
- Train and honestly evaluate multiple ML approaches (classical ML and neural
  networks) on the same classification task
- Build the practical skills — debugging, leak-free evaluation, reading model
  behavior critically — needed for more advanced neuroengineering work later

## Dataset

[NinaPro DB1](http://ninapro.hevs.ch), Subject 1, Exercise A (12 finger/thumb
gestures, 10-channel surface EMG). See Atzori et al., *Building the NinaPro
Database* (BioRob 2012) for the acquisition protocol and original benchmarking.

## What's in this repo

- `emg_gesture_classification.ipynb` — the full pipeline: data loading, EDA,
  feature extraction, classical ML (Random Forest, KNN), a feedforward neural
  network (MLP, with and without EarlyStopping), and a 1D CNN trained directly
  on raw signal windows for comparison. Fully documented with the reasoning
  behind each design decision, not just the code.

## Results (summary)

| Model | Test Accuracy |
|---|---|
| Random Forest | ~80% |
| KNN (k=5) | ~76% |
| MLP | ~81–82% |
| MLP + EarlyStopping | ~81% |
| CNN (raw signal) | ~75–77% |

Hand-crafted statistical features (mean/std/min/max/RMS per electrode) currently
outperform an end-to-end CNN learning from raw signal — a reasonable outcome given
the limited data (one subject, 10 repetitions/gesture), not a failure of either
approach. Full discussion, including a genuine sensor-placement-driven confusion
between thumb adduction and thumb flexion that shows up consistently across every
model tested, is in the notebook's final section.

## Status & next steps

Classification pipeline complete and evaluated. Next: an animated hand
visualization driven by model predictions, to connect the classification results
back to the "prosthetic hand" framing. Longer-term, a natural follow-up project
would target inter-subject generalization or real-time/online classification —
both flagged as open problems in the original NinaPro work.
