# Timeline
- first I tried directly using the samples, one vector per sample, but that was not enough, as i was using 80% of data to train the model, only 2 sets of data were left to test it, so the accuracy of getting right each movement could be 0, 0.5 or 1, but that is too little data and not a reliable metric. 
- during the process it became visible that the movement 1 gets low accuracy score, even with different methods, so i tried comparing it graphically to other movements, to see if maybe the muscle signals were too similar to some other movement, that explain the bunch of graphical visualisations of the data in the middle of training and retraining the models
- I tried windowing the data to get more pieces of information to train and test the model 
- next step is to compare the first try with a simple neural network created by myself and see the difference in outcomes

# Specific notes

## Gesture 9 vs. Gesture 11 confusion — analysis

Gestures 9 (thumb adduction) and 11 (thumb flexion) are the two most confused
classes in the Random Forest results (31 of gesture 11's true windows predicted
as gesture 9). Both are thumb-only movements driven by overlapping intrinsic/
extrinsic thumb muscles, so some surface-EMG overlap is anatomically expected.

Comparing mean waveforms across all 10 electrodes: most electrodes show highly
similar shape between the two gestures, differing mainly in amplitude rather
than pattern. Electrode 8 shows the clearest separation in signal shape
(sharper peak timing/shape difference), making it likely the most informative
electrode for distinguishing this specific pair. Electrodes 4-6 show almost no
signal for either gesture, consistent with their placement being farther from
thumb-controlling muscles.

Takeaway: this confusion is a partly genuine sensor-placement limitation, not
purely a modeling bug — worth noting as a limitation in the final write-up.