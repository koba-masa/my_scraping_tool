import sys
import os

base_path = os.path.dirname(os.path.abspath(__file__)) + "/../"

sys.path.append(os.path.abspath(base_path))

os.environ['ENV'] = 'test'
