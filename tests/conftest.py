import sys
import os


# add the pokerreview dir to the PATH env to be able to access input in pytest tests
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../")),
)
print(sys.path)
