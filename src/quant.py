
from cplx import *

#Hadamard
def H(cm : cmat):
  rows = 2
  cols = 2
  scalar = cnum(1 / 2 ** 0.5, 0)
  entries = {(0, 0):cnum(1, 0),
             (1, 0):cnum(1, 0),
             (0, 1):cnum(1, 0),
             (1, 1):cnum(-1, 0)}
  m = cmat(rows, cols, entries).smult(scalar)
  return cmatmult(cm, m)

#Pauli-X
def X(cm : cmat):
  rows = 2
  cols = 2
  entries = {(0, 1):cnum(1, 0),
             (1, 0):cnum(1, 0)}
  m = cmat(rows, cols, entries)
  return cmatmult(cm, m)

#Pauli-Y
def Y(cm : cmat):
  rows = 2
  cols = 2
  entries = {(0, 1):cnum(0, -1),
             (1, 0):cnum(0, 1)}
  m = cmat(rows, cols, entries)
  return cmatmult(cm, m)

#Pauli-Z
def Z(cm : cmat):
  rows = 2
  cols = 2
  entries = {(0, 0):cnum(1, 0),
             (1, 1):cnum(-1, 0)}
  m = cmat(rows, cols, entries)
  return cmatmult(cm, m)

