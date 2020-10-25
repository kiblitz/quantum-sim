
from cplx import *
from typing import List

import math
import random

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

# Probability a Complex number refers to
def prob(c : cnum) -> float:
  return c.real**2 + c.imag**2

# Read qubit
def read(cm : cmat) -> List[int]:
  if cm.cols != 1:
    raise Exception("Qubit complex matrix must have 1 col")
  lg = math.log(cm.rows, 2)
  qubits = (int)(lg)
  if qubits != lg:
    raise Exception("Qubit must contain 2^n rows")
  rng = random.random()
  for i in range(cm.rows):
    rng -= prob(cm.array[i][0])
    if rng < 0:
      state = bin(i)[2:] 
      state = '0' * (qubits - len(state)) + state
      val = []
      for q in state:
        val.append(int(q))
      cm.array = [[0] if r != i else [1] for r in range(cm.rows)]
      return val
  raise Exception("Invalid qubit probabilies")

# Print Dirac notation of qubits (Bra-ket)
def ket(cm : cmat, rem0 : bool = True, condensed : bool = False) -> None:
  if cm.cols != 1:
    raise Exception("Qubit complex matrix must have 1 col")
  lg = math.log(cm.rows, 2)
  qubits = (int)(lg)
  if qubits != lg:
    raise Exception("Qubit must contain 2^n rows")
  expression = ''
  for i in range(cm.rows):
    state = bin(i)[2:] 
    state = '0' * (qubits - len(state)) + state
    val = cm.array[i][0].to_string(rem0, condensed)
    space = ' ' * (not condensed)
    expression += '%s(%s)|%s)%s+'  % (space, val, state, space)
  if not condensed:
    expression = expression[1:-1]
  print(expression[:-1])
