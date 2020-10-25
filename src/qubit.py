
from cplx import *

# Zero qubit
def zero() -> cmat:
  rows = 2
  cols = 1
  entries = {(0, 0):cnum(1)}
  return cmat(rows, cols, entries)

# One qubit
def one() -> cmat:
  rows = 2
  cols = 1
  entries = {(1, 0):cnum(1)}
  return cmat(rows, cols, entries)

