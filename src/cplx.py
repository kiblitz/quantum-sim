
from __future__ import annotations
from typing import AnyStr, Dict, Tuple

import math

# Decimal precision
PRECISION = 8

# Complex number
class cnum:
  def __init__(self, real : float, imag : float = 0):
    self.real = real
    self.imag = imag
  
  # Modulus (Euclidean norm)
  def __abs__(self) -> float:
    return round((self.real**2 + self.imag**2)**0.5, PRECISION)

  # Complex Conjugate
  def __invert__(self):
    return cnum(self.real, -self.imag)

  # Complex Multiplication
  def __mul__(self, c : cnum) -> cnum:
    r1 = self.real
    i1 = self.imag
    r2 = c.real
    i2 = c.imag
    return cnum(round(r1 * r2 - i1 * i2, PRECISION), 
                round(i1 * r2 + r1 * i2, PRECISION))
 
  # Complex Addition
  def __add__(self, c : cnum) -> cnum:
    r1 = self.real
    i1 = self.imag
    r2 = c.real
    i2 = c.imag
    return cnum(r1 + r2, i1 + i2)

  # Scalar times Complex Matrix
  def __matmul__(self, cm : cmat) -> cmat:
    rows = cm.rows
    cols = cm.cols
    entries = {}
    for r in range(len(cm.array)):
      for c in range(len(cm.array[r])):
        entries[(r, c)] = cm.array[r][c] * self
    return cmat(rows, cols, entries)

  # String representation
  def to_string(self, rem0 : bool = True, condensed : bool = False) -> AnyStr:
    real = str(self.real)
    imag = str(self.imag) + 'i'
    if rem0:
      if not self.real and not self.imag:
        return '0'
      if not self.real:
        real = ''
      if not self.imag:
        imag = ''
      elif self.imag == 1:
        imag = 'i'
      elif self.imag == -1:
        imag = '-i'
    op = ''
    if real and imag:
      if self.imag < 0:
        op = '-'
        imag = imag[1:]
      else:
        op = '+'
      if not condensed:
        op = ' ' + op + ' '
    return real + op + imag

  # Print string representation
  def display(self, rem0 : bool = True, condensed : bool = False) -> None:
    print(self.to_string(rem0, condensed))

# Complex Exponential (e^ci)
def cexp(c : float):
  real = round(math.cos(c), PRECISION)
  imag = round(math.sin(c), PRECISION)
  return cnum(real, imag)

# Complex Matrix
class cmat:
  def __init__(self, rows : int, cols : int, entries : Dict[Tuple[int, int], cnum]):
    self.rows = rows
    self.cols = cols
    self.array = [[cnum(0, 0) for c in range(cols)] for r in range(rows)] 
    for key, value in entries.items():
      row = key[0]
      col = key[1]
      self.array[row][col] = value
  
  # Kronecker Product (Tensor)
  def __mul__(self, cm : cmat) -> cmat:
    row1 = self.rows
    col1 = self.cols
    row2 = cm.rows
    col2 = cm.cols
    rows = row1 * row2
    cols = col1 * col2
    entries = {}
    for r in range(rows):
      for c in range(cols):
        key = (r, c)
        r1 = r // row2
        c1 = c // col2
        r2 = r % row2
        c2 = c % col2
        e1 = self.array[r1][c1]
        e2 = cm.array[r2][c2] 
        entries[key] = e1 * e2
    return cmat(rows, cols, entries)

  # Complex Matrix Multiplication
  def __matmul__(self, cm : cmat) -> cmat:
    shared = self.cols
    if shared != cm.rows:
      raise Exception("Matrix multiplication invalid")
    rows = self.rows
    cols = cm.cols
    entries = {}
    for r in range(rows):
      for c in range(cols):
        total = cnum(0, 0)
        for e in range(shared):
          total += self.array[r][e] * cm.array[e][c]
        entries[(r, c)] = total
    return cmat(rows, cols, entries)

  # Complex Matrix Exponentiation
  def __pow__(self, exp : int) -> cmat:
    if exp < 0:
      raise Exception("Matrix exponent cannot be negative")
    ans = self
    for i in range(1, exp):
      ans @= self
    return ans

  # Print string representation
  def display(self, rem0 : bool = True, condensed : bool = False) -> None:
    sizes = []
    for col in [*zip(*self.array)]:
      sizes.append(len(max(col, key=lambda c : len(c.to_string(rem0, condensed))).to_string(rem0, condensed)))
    for row in self.array:
      line = '['
      for i in range(len(row)):
        num = row[i].to_string(rem0, condensed)
        size = len(num) 
        tail = sizes[i] - size
        line += num + ' ' * tail + ',' + ' ' * (not condensed)
      print(line[:-1 - (1 * (not condensed))] + ']')

