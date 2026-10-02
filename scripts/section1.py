#!/usr/bin/env python3
import numpy as np
# add import and helper functions her
if __name__ == "__main__":
    # code goes here
    #print("Hello, World!")
    np.random.seed(42)
    A = np.random.normal(size=(4, 4))
    B = np.random.normal(size=(4, 2))
    #print(A@B)
    np.random.seed(42)
    x = np.random.normal(size=(4, 10))
    np.random.seed(42)
    diff = x[:, None, :] - x[None, :, :]   # (4, 4, 10)
    D = np.sum(np.square(diff), axis=-1)   # (4, 4)
    print(D)

