#I moduli
#/lib/site-packages

import script
script.hello_world()

#import geometry
#from geometry import Triangle, Square

import os
print(os.getcwd())

import datetime
print(datetime.datetime.now())

from time import time
from math import pow as power
import numpy as np

print(time())

n = 2
pow = 10
n_pow = 20

tick = time()

power(n, n_pow)

n_pow = np.power(n, n_pow)

for _ in range(pow):
    n_pow=n

duration = time() - tick
print(duration)