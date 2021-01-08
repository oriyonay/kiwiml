"""
TEST_DATASETS: unit tests for the dataset importers (kiwiml.datasets).
this module requires sklearn as it compares results with it!
"""

# import the datasets.py file from the kiwiml module:
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from kiwiml import datasets

##### TEST THE BOSTON DATASET LOADER #####
def load_boston_test():
  from sklearn.datasets import load_boston as sklearn_lb
  X, y = sklearn_lb(return_X_y=True)

  X_kiwi, y_kiwi = load_boston()

  assert np.array_equal(X, X_kiwi)
  assert np.array_equal(y, y_kiwi)

  print('Boston dataset loader passed.')

##### TEST THE UCI BREAST CANCER DATASET LOADER #####
def load_breast_cancer_test():
  from sklearn.datasets import load_breast_cancer as sklearn_lbc

  X, y = sklearn_lbc(return_X_y=True)
  X_kiwi, y_kiwi = load_breast_cancer()

  assert np.array_equal(X, X_kiwi)
  assert np.array_equal(y, y_kiwi)

  print('Breast cancer dataset loader passed.')

##### TEST ALL DATASET LOADERS #####
def test_all_loaders():
  # test the boston dataset loader:
  load_boston_test()

  # test the breast cancer loader:
  load_breast_cancer_test()

  # NOTE: no test for MNIST loader.

  # if we made it here, all tests were passed:
  print('Passed all loader tests.')

# if this is being run as a standalone script (which it should), run all unit tests:
if __name__ == '__main__':
  test_all_loaders()
