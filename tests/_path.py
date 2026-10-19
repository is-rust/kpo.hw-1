import sys
import os

path: str = __file__
path = os.path.dirname(path)
path = os.path.dirname(path)
path = os.path.join(path, 'src')
sys.path.append(path)
