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
- after finishing the classical models and MLP, I went back and had the whole notebook cleaned up and documented properly (it was basically just cells with no explanation before), since I want this to actually be readable by someone else, not just make sense to me.
- realized at that point that this whole project so far had a lot of AI-written code that I copy-pasted without fully understanding, so I decided to change how I work on the CNN part: I write the code myself from instructions instead of getting it handed to me. Slower, but I actually know what my own code does now.
- built the raw-signal pipeline for the CNN myself (with a lot of debugging): messed up variable scope (defined a list inside a loop instead of outside it, so it kept getting wiped), overwrote `X_raw` with an unrelated `X` variable from an earlier section, mixed up numpy array vs plain Python list indexing, and messed up the 1-indexed vs 0-indexed labels more than once. Each one was a real, separate bug, not the same mistake repeated.
- first CNN run got ~77% accuracy, worse than every other model. Turned out the validation split wasn't respecting repetition boundaries the way my train/test split does, so it was probably leaking overlapping windows between train and validation - inflated the validation accuracy I saw during training compared to real test accuracy.
- fixed it by holding out whole repetitions for validation too (not just for the test set), trained a fresh CNN with EarlyStopping this time (needed a bigger epoch budget - like 100 - for EarlyStopping to actually do anything, otherwise it never gets the chance to kick in before hitting a low fixed epoch cap). Final leak-free CNN result: ~75%, still the weakest model overall.
- CNN underperforming the feature-based models isn't something to chase and fix - with this little data (one subject, only 10 repetitions per gesture), hand-crafted features apparently still beat a small CNN learning from raw signal. Noted as a real finding, not a failure.
- one reassuring thing: gesture 9 vs 11 confusion (see below) showed up again in the CNN results, on a totally different architecture than the Random Forest. Makes me more confident it's a real sensor-placement limitation and not just a quirk of one model.

# Specific notes

## Gesture 9 vs. Gesture 11 confusion — analysis

Gestures 9 (thumb adduction) and 11 (thumb flexion) are the two most confused
classes in the Random Forest results (31 of gesture 11's true windows predicted
as gesture 9), and the same pair is still the most confused in the CNN results later on.
Both are thumb-only movements driven by overlapping intrinsic/
extrinsic thumb muscles, so some surface-EMG overlap is anatomically expected.

Comparing mean waveforms across all 10 electrodes: most electrodes show highly
similar shape between the two gestures, differing mainly in amplitude rather
than pattern. Electrode 8 shows the clearest separation in signal shape
(sharper peak timing/shape difference), making it likely the most informative
electrode for distinguishing this specific pair. Electrodes 4-6 show almost no
signal for either gesture, consistent with their placement being farther from
thumb-controlling muscles.

Takeaway: this confusion is a partly genuine sensor-placement limitation, not
purely a modeling bug - worth noting as a limitation in the final write-up. Confirmed
by it showing up again on a completely different model architecture (CNN).

## Fine tuning

There are three separate categories of things I can adjust to get a better results from my neural network:

- Architecture — number of layers, number of units per layer, dropout rate. These change what the model is capable of representing.

- Training process — number of epochs, batch size, learning rate, optimizer choice. These change how the model searches for good weights, not what it's capable of.

- Regularization — dropout, plus things like L2 weight penalties. These specifically fight overfitting.

Process: change one thing at a time, rerun, and compare against the current baseline.

## Workflow lessons (not modeling, just process)

- `.ipynb_checkpoints/` was accidentally where I was editing/committing from instead of the real notebook file at one point - added it to `.gitignore` and made sure to always open the actual project file, not a checkpoint copy.
- GitHub stopped accepting my password for `git push` (they removed password auth a while ago) - had to generate a personal access token and use that instead.
- notebooks only remember cells you've actually run, in the order you ran them, not the order they appear on the page - restarting the kernel or reopening the notebook wipes everything, so functions/variables from earlier sections need to be rerun before cells further down will work.

## Where this project stands now

Classical ML (RF, KNN) + MLP (with and without EarlyStopping) + CNN on raw signal, all
compared on the same task, all evaluated with a leak-free repetition-based split. Full
results, limitations, and reasoning are documented directly in the notebook now instead
of just here.

Next: an animated hand visualization driven by predictions, then this project is done
and I move on to something that covers different ground - probably something related to
inter-subject generalization or moving from offline to closer-to-real-time classification.
