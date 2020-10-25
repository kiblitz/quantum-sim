
class cnum:
  def __init__(self, real : float, imag : float = 0):
    self.real = real
    self.imag = imag

  def to_string(self):
    if self.imag < 0:
      op = '-'
    else:
      op = '+'
    return str(self.real) + op + str(abs(self.imag))

  def display(self):
    print(self.to_string())

def conj(c : cnum):
  return cnum(c.real, -c.imag)

def cmult(c1 : cnum, c2 : cnum):
  a = c1.real
  b = c1.imag
  c = c2.real
  d = c2.imag
  return cnum(a * c - b * d, b * c + a * d)

def cadd(c1 : cnum, c2 : cnum):
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
    for key, value in entries.items:
      row = key[0]
      col = key[1]
      self.array[row][col] = value

  def display(self):
    sizes = []
    for col in zip(self.array):
      sizes.append(max(col, key=lambda c : len(c.to_string())))
    for row in self.array:
      line = '['
      for i in range(len(self.array[row])):
        num = row[i].to_string()
        size = len(num) 
        tail = sizes[i] - size
        line += num + ' ' * tail + ','
      print(line + ']')

def cmatmult(cm1 : cmat, cm2 : cmat):
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

