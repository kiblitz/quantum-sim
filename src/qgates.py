
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
  m = cmat(rows, cols, entries) << scalar
  return m @ cm

# Pauli-X
def X(cm : cmat) -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 1):cnum(1),
             (1, 0):cnum(1)}
  m = cmat(rows, cols, entries)
  return m @ cm

# Pauli-Y
def Y(cm : cmat) -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 1):cnum(0, -1),
             (1, 0):cnum(0, 1)}
  m = cmat(rows, cols, entries)
  return m @ cm

# Pauli-Z
def Z(cm : cmat) -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(-1)}
  m = cmat(rows, cols, entries)
  return m @ cm

# Phase (S)
def S(cm : cmat) -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(0, 1)}
  m = cmat(rows, cols, entries)
  return m @ cm

# pi/8 (T)
def T(cm : cmat) -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 0):cnum(1),
             (1, 1):cexp(math.pi/4)}
  m = cmat(rows, cols, entries)
  return m @ cm

# Controlled Not X (2 qubits)
def CX(cm : cmat) -> cmat:
  rows = 4
  cols = 4
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(1),
             (2, 3):cnum(1),
             (3, 2):cnum(1)}
  m = cmat(rows, cols, entries)
  return m @ cm

# Controlled Not Y (2 qubits)
def CY(cm : cmat) -> cmat:
  rows = 4
  cols = 4
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(1),
             (2, 3):cnum(0, -1),
             (3, 2):cnum(0, 1)}
  m = cmat(rows, cols, entries)
  return m @ cm

# Controlled Not Z (2 qubits)
def CZ(cml : cmat) -> cmat:
  rows = 4
  cols = 4
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(1),
             (2, 2):cnum(1),
             (3, 3):cnum(-1)}
  m = cmat(rows, cols, entries)
  return m @ cm

# Swap
def SWAP(cm : cmat) -> cmat:
  rows = 4
  cols = 4
  entries = {(0, 0):cnum(1),
             (1, 2):cnum(1),
             (2, 1):cnum(1),
             (3, 3):cnum(1)}
  m = cmat(rows, cols, entries)
  return m @ cm

# Toffoli (CCNOT) (3 qubits)
def CCNOT(cm : cmat) -> cmat:
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
  return m @ cm

