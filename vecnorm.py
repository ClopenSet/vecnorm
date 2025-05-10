#!/usr/bin/env python3

import sys
import numpy as np

def main():
    if len(sys.argv) < 2:
        print("Usage: vecnorm <num1> <num2> ...")
        sys.exit(1)
    try:
        vec = np.array([float(x) for x in sys.argv[1:]])
        print(np.linalg.norm(vec))
    except ValueError:
        print("All inputs must be numbers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
