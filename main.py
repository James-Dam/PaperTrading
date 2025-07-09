import sys
import os

folder = os.path.abspath('/home/codio/workspace/modules')
sys.path.append(folder)

from paper_trading import run

if __name__ == "__main__":
    run()
