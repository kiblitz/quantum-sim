
from cplx import *
from typing import Tuple

import math

# Identity
def I() -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(1)}
  return cmat(rows, cols, entries)

# Hadamard
def H(cm : cmat) -> cmat:
  rows = 2
  cols = 2
  scalar = cnum(1 / 2 ** 0.5, 0)
  entries = {(0, 0):cnum(1),
             (1, 0):cnum(1),
             (0, 1):cnum(1),
             (1, 1):cnum(-1)}
  m = cmat(rows, cols, entries).smult(scalar)
  return cmatmult(m, cm)

# Pauli-X
def X(cm : cmat) -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 1):cnum(1),
             (1, 0):cnum(1)}
  m = cmat(rows, cols, entries)
  return cmatmult(m, cm)

# Pauli-Y
def Y(cm : cmat) -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 1):cnum(0, -1),
             (1, 0):cnum(0, 1)}
  m = cmat(rows, cols, entries)
  return cmatmult(m, cm)

# Pauli-Z
def Z(cm : cmat) -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(-1)}
  m = cmat(rows, cols, entries)
  return cmatmult(m, cm)

# Phase (S)
def S(cm : cmat) -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(0, 1)}
  m = cmat(rows, cols, entries)
  return cmatmult(m, cm)

# pi/8 (T)
def T(cm : cmat) -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 0):cnum(1),
             (1, 1):cexp(math.pi/4)}
  m = cmat(rows, cols, entries)
  return cmatmult(m, cm)

# Controlled Not X
def CX(cm1 : cmat, cm2 : cmat) -> cmat:
  cm = kronecker(cm1, cm2)
  rows = 4
  cols = 4
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(1),
             (2, 3):cnum(1),
             (3, 2):cnum(1)}
  m = cmat(rows, cols, entries)
  return cmatmult(m, cm)

# Controlled Not Y
def CY(cm1 : cmat, cm2 : cmat) -> cmat:
  cm = kronecker(cm1, cm2)
  rows = 4
  cols = 4
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(1),
             (2, 3):cnum(0, -1),
             (3, 2):cnum(0, 1)}
  m = cmat(rows, cols, entries)
  return cmatmult(m, cm)

# Controlled Not Z
def CZ(cm1 : cmat, cm2 : cmat) -> cmat:
  cm = kronecker(cm1, cm2)
  rows = 4
  cols = 4
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(1),
             (2, 2):cnum(1),
             (3, 3):cnum(-1)}
  m = cmat(rows, cols, entries)
  return cmatmult(m, cm)

# Swap
def SWAP(cm1 : cmat, cm2 : cmat) -> cmat:
  cm = kronecker(cm1, cm2)
  rows = 4
  cols = 4
  entries = {(0, 0):cnum(1),
             (1, 2):cnum(1),
             (2, 1):cnum(1),
             (3, 3):cnum(1)}
  m = cmat(rows, cols, entries)
  return cmatmult(m, cm)

# Toffoli (CCNOT)
def CCNOT(cm1 : cmat, cm2 : cmat, cm3 : cmat) -> cmat:
  cm = kronecker(kronecker(cm1, cm2), cm3)
  rows = 8
  cols = 8
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(1),
             (2, 2):cnum(1),
             (3, 3):cnum(1),
             (4, 4):cnum(1),
             (5, 5):cnum(1),
             (6, 7):cnum(1),
             (7, 6):cnum(1)}
  m = cmat(rows, cols, entries)
  return cmatmult(m, cm)

