# kiwi v0.0.5
A tiny, simple, instructional machine learning library in python, written by Ori Yonay. Mostly written as a personal reference for classic ML algorithms. Follows similar syntax to sklearn :)

To install:
`pip3 install kiwiml`

Current Features:
* Machine Learning Models:
  * KNN
  * Linear Regression
  * Logistic Regression
  * Naive Bayes
  * Perceptron
  * Single Dimensional Analysis (experimental)
* Utilities:
  * Accuracy score function for calculating model accuracy
  * train_test_split
  * A function to plot cost histories
  * PCA Decomposition (will be in its own dimensionality reduction class in the future)
* Error Functions:
  * Mean-Squared Error
  * Cross-Entropy Loss
* Dataset Loaders:
  * Boston dataset
  * Breast cancer dataset
  * Iris dataset
  * MNIST dataset

TODO:
* Error Functions:
  * Add mean absolute deviation
  * Change error functions to take parameters (w, X, predicted) instead of (X, y, predicted) so can be differentiated with autodiff
* Machine Learning Models:
  * SVM
  * Decision Tree
  * Random Forest
  * K-Means Clustering
  * Neural Network Library
     * Fully-Connected layer
     * Convolutional Layer
     * ...
* More dataset importers
* Automatic learning
