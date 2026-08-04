# Timeline
- first I tried directly using the samples, one vector per sample, but that was not enough, as i was using 80% of data to train the model, only 2 sets of data were left to test it, so the accuracy of getting right each movement could be 0, 0.5 or 1, but that is too little data and not a reliable metric. 
- during the process it became visible that the movement 1 gets low accuracy score, even with different methods, so i tried comparing it graphically to other movements, to see if maybe the muscle signals were too similar to some other movement, that explain the bunch of graphical visualisations of the data in the middle of training and retraining the models
- I tried windowing the data to get more pieces of information to train and test the model 
- next step is to compare the first try with a simple neural network created by myself and see the difference in outcomes
- first time i tried own neural network, i forgot to shuffle the data and trained only on 10 movements, which ended up in accuracy staying very low since the very beginning to the end, without improvement - it created a kind of bottleneck probably, so this line is important as i learnt: 

```
from sklearn.utils import shuffle
X_train_scaled, y_train_nn = shuffle(X_train_scaled, y_train_nn, random_state=42)
```
- EarlyStopping matched the manually-tuned baseline while removing the need to guess epoch count, which was initially guessed quite accuratelly as it seems. EarlyStopping didn't boost accuracy over a well-chosen fixed epoch
count, but removes the need to guess epochs and protects against overfitting
automatically as the model/data change.

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

## Fine tuning

There are three separate categories of things I can adjust to get a better results from my neural network:

- Architecture — number of layers, number of units per layer, dropout rate. These change what the model is capable of representing.

- Training process — number of epochs, batch size, learning rate, optimizer choice. These change how the model searches for good weights, not what it's capable of.

- Regularization — dropout, plus things like L2 weight penalties. These specifically fight overfitting.

Process: change one thing at a time, rerun, and compare against the current baseline