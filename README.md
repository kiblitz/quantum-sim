# quantum-sim
## About
Quantum computation simulation library with qubits and quantum logic gates implemented as complex matrices

## Use
Download the release and run the following command
```
pip install <release-file>
```

## Modules
- `quantSim.cplx`: Complex
- `quantSim.qgates`: Quantum gates
- `quantSim.qubit`: Qubits

## Features
### Complex
#### Numbers
- `c = cnum(r, i)`: where `r` is the real part and `i` is the imaginary part (defaulted 0)
- `~c`: complex conjugate of `c`
- `abs(c)`: modulus of `c` (Euclidean norm)
- `c1 + c2`, `c1 * c2`: complex addition/multiplication
- `c @ cm`: complex scalar times complex matrix `cm`
- `c.to_string(rem0, condensed)` and `c.display(rem0, condensed)`: get/print the string representation
  - `rem0`: replace 0 values with empty space (default `True`)
  - `condensed`: condense the output by removing spaces (default `False`)

- `cexp(x)`: get the complex exponential `e^(xi)` where `x` is a constant

#### Matrices
 - `cm = cmat(rows, cols, entries)`: where `rows`, `cols` refer to the number of rows and columbs in the matrix respectively, and `entries` refers to the non-zero entries of the matrix
   - `entries = {(r_1, c_1):cnum(a_1, b_1), (r_2, c_2):cnum(a_2, b_2),..., (r_n, c_n):cnum(a_n, b_n)}` where the `r_j``c_j` entry of the matrix has value `a_j + b_j i`
 - `cm.transpose()`: transpose of `cm`
 - `~cm`: dagger of `cm`
 - `cm1 * cm2`: returns the tensor (Kronecker) product of `cm1` and `cm2`
 - `cm1 @ cm2`: matrix multiplication
 - `cm**n`: matrix exponentiation to the power of `n`
 - `c.display(rem0, condensed)`: print the string representation
   - `rem0`: replace 0 values with empty space (default `True`)
   - `condensed`: condense the output by removing spaces (default `False`)
 
### Quantum Gates
 - `I()`: Identity
 - `H()`: Hadamard
 - `X()`: Pauli-X
 - `Y()`: Pauli-Y
 - `Z()`: Pauli-Z
 - `S()`: Phase
 - `T()`: pi/8 (T^2 = S)
 - `CX()`: Controlled Not X (2 qubits)
 - `CY()`: Controlled Not Y (2 qubits)
 - `CZ()`: Controlled Not Z (2 qubits)
 - `SWAP()`: Swap (2 qubits)
 - `CCNOT()`: Toffoli (3 qubits)

### Qubits
 - `zero()`, `one()`: qubits initialized with 0 and 1 respectively
 - `prob(c)`: calculates the probability corresponding to complex number `c` (a^2 + b^2)
 - `read(cm)`: reads superpositioned qubits as a matrix `cm` and destroys qubit data
 - `ket(cm, rem0, condensed)`: prints the data in a superpositioned qubit as a matrix `cm` in ket (Dirac) notation
   - `rem0`: replace 0 values with empty space (default `True`)
   - `condensed`: condense the output by removing spaces (default `False`)
 
