
from cplx import *

#Hadamard
def H(cm : cmat):
  hrows = 2
  hcols = 2
  hscalar = cnum(1 / 2 ** 0.5, 0)
  hentries = {(0, 0):cnum(1, 0),
              (1, 0):cnum(1, 0),
              (0, 1):cnum(1, 0),
              (1, 1):cnum(-1, 0)}
  h = cmat(hrows, hcols, hentries).smult(hscalar)
  return cmatmult(cm, h)
