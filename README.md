Cosmic Classifier

With millions of celestial objects catalogued in surveys like SDSS, manual classification is impractical. This classifier automates the distinction between stars, galaxies, and quasars using spectral features.

The main aim of this project is to handle large-scale survey data more efficiently while maintaining high accuracy. The model is also integrated into a user-friendly web-application for researchers and enthusiasts alike. 

The model used here is a 4-layer sequential CNN trained on 10000 SDSS observations with 14 spectral features each (redshift, right ascension, etc.). The data was normalised and trained with a 75/25 train/test split for 40 epochs using ReLU activation and Adam optimiser. It achieved a classification accuracy of 98.6%.

Future Improvements: Extend the model to accept astronomical images as input, eliminating the need for manual feature extraction.
