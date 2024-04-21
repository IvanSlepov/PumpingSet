import sys

sys.path.append('C:\\Users\\islie\\Documents\\work\\PumpingSET\\PumpingSet\\auto-tests-panda-pizza\\src')
print(sys.path)

# test

import os

try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []
