
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
def H() -> cmat:
  rows = 2
  cols = 2
  scalar = cnum(1 / 2 ** 0.5, 0)
  entries = {(0, 0):cnum(1),
             (1, 0):cnum(1),
             (0, 1):cnum(1),
             (1, 1):cnum(-1)}
  return cmat(rows, cols, entries) << scalar

# Pauli-X
def X() -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 1):cnum(1),
             (1, 0):cnum(1)}
  return cmat(rows, cols, entries)

# Pauli-Y
def Y() -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 1):cnum(0, -1),
             (1, 0):cnum(0, 1)}
  return cmat(rows, cols, entries)

# Pauli-Z
def Z() -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(-1)}
  return cmat(rows, cols, entries)

# Phase (S)
def S() -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(0, 1)}
  return cmat(rows, cols, entries)

# pi/8 (T)
def T() -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 0):cnum(1),
             (1, 1):cexp(math.pi/4)}
  return cmat(rows, cols, entries)

# Controlled Not X (2 qubits)
def CX() -> cmat:
  rows = 4
  cols = 4
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(1),
             (2, 3):cnum(1),
             (3, 2):cnum(1)}
  return cmat(rows, cols, entries)

# Controlled Not Y (2 qubits)
def CY() -> cmat:
  rows = 4
  cols = 4
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(1),
             (2, 3):cnum(0, -1),
             (3, 2):cnum(0, 1)}
  return cmat(rows, cols, entries)

# Controlled Not Z (2 qubits)
def CZ() -> cmat:
  rows = 4
  cols = 4
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(1),
             (2, 2):cnum(1),
             (3, 3):cnum(-1)}
  return cmat(rows, cols, entries)

# Swap
def SWAP() -> cmat:
  rows = 4
  cols = 4
  entries = {(0, 0):cnum(1),
             (1, 2):cnum(1),
             (2, 1):cnum(1),
             (3, 3):cnum(1)}
  return cmat(rows, cols, entries)

# Toffoli (CCNOT) (3 qubits)
def CCNOT() -> cmat:
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
  return cmat(rows, cols, entries)

