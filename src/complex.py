
class cnum:
  def __init__(self, real : float, imag : float = 0):
    self.real = real
    self.imag = imag

  def string(self):
    if self.imag < 0:
      op = '-'
    else:
      op = '+'
    return str(self.real) + op + str(abs(self.imag))

  def display(self):
    print(self.string())

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

