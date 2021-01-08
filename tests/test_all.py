"""
TEST_ALL: runs all unit tests.
"""

import test_datasets

##### RUN ALL TESTS #####
if __name__ == '__main__':
  print('----- Starting all unit tests -----')
  test_datasets.test_all_loaders()
  print('----- All tests passed -----')
