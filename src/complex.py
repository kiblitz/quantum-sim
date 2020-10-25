
from typing import AnyStr, Dict, Tuple

class cnum:
  def __init__(self, real : float, imag : float = 0):
    self.real = real
    self.imag = imag

  def to_string(self) -> AnyStr:
    if self.imag < 0:
      op = '-'
    else:
      op = '+'
    return str(self.real) + op + str(abs(self.imag)) + 'i'

  def display(self) -> None:
    print(self.to_string())

def conj(c : cnum) -> cnum:
  return cnum(c.real, -c.imag)

def cmult(c1 : cnum, c2 : cnum) -> cnum:
  a = c1.real
  b = c1.imag
  c = c2.real
  d = c2.imag
  return cnum(a * c - b * d, b * c + a * d)

def cadd(c1 : cnum, c2 : cnum) -> cnum:
  a = c1.real
  b = c1.imag
  c = c2.real
  d = c2.imag
  return cnum(a + c, b + d)

class cmat:
  def __init__(self, rows : int, cols : int, entries : Dict[Tuple[int, int], cnum]):
    self.rows = rows
    self.cols = cols
    self.array = [[cnum(0, 0) for c in range(cols)] for r in range(rows)] 
    for key, value in entries.items():
      row = key[0]
      col = key[1]
      self.array[row][col] = value

  def display(self) -> None:
    sizes = []
    for col in [*zip(*self.array)]:
      sizes.append(len(max(col, key=lambda c : len(c.to_string())).to_string()))
    for row in self.array:
      line = '['
      for i in range(len(row)):
        num = row[i].to_string()
        size = len(num) 
        tail = sizes[i] - size
        line += num + ' ' * tail + ','
      print(line[:-1] + ']')

def cmatmult(cm1 : cmat, cm2 : cmat) -> cmat:
  shared = cm1.cols
  if shared != cm2.rows:
    raise Exception("Matrix multiplication invalid")
  rows = cm1.rows
  cols = cm2.cols
  entries = {}
  for r in range(rows):
    for c in range(cols):
      total = cnum(0, 0)
      for e in range(shared):
        total = cadd(total, cmult(cm1.array[r][e], cm2.array[e][c]))
      entries[(r, c)] = total
  return cmat(rows, cols, entries)

