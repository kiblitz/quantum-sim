
from cplx import *
from typing import Tuple

#Identity
def I() -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(1)}
  return cmat(rows, cols, entries)

#Hadamard
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

#Pauli-X
def X(cm : cmat) -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 1):cnum(1),
             (1, 0):cnum(1)}
  m = cmat(rows, cols, entries)
  return cmatmult(m, cm)

#Pauli-Y
def Y(cm : cmat) -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 1):cnum(0, -1),
             (1, 0):cnum(0, 1)}
  m = cmat(rows, cols, entries)
  return cmatmult(m, cm)

#Pauli-Z
def Z(cm : cmat) -> cmat:
  rows = 2
  cols = 2
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(-1)}
  m = cmat(rows, cols, entries)
  return cmatmult(m, cm)

#Controlled Not X
def CX(cm1 : cmat, cm2 : cmat) -> cmat:
  cm3 = kronecker(cm1, cm2)
  rows = 4
  cols = 4
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(1),
             (2, 3):cnum(1),
             (3, 2):cnum(1)}
  m = cmat(rows, cols, entries)
  return cmatmult(m, cm3)

#Controlled Not Y
def CY(cm1 : cmat, cm2 : cmat) -> cmat:
  cm3 = kronecker(cm1, cm2)
  rows = 4
  cols = 4
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(1),
             (2, 3):cnum(0, -1),
             (3, 2):cnum(0, 1)}
  m = cmat(rows, cols, entries)
  return cmatmult(m, cm3)

#Controlled Not Z
def CZ(cm1 : cmat, cm2 : cmat) -> cmat:
  cm3 = kronecker(cm1, cm2)
  rows = 4
  cols = 4
  entries = {(0, 0):cnum(1),
             (1, 1):cnum(1),
             (2, 2):cnum(1),
             (3, 3):cnum(-1)}
  m = cmat(rows, cols, entries)
  return cmatmult(m, cm3)

