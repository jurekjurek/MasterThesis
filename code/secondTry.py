from discopy.tensor import Cup, Cap, Id 
from discopy.tensor import Dim, Tensor
from discopy.symmetric import Ty
from discopy.drawing import Equation
from discopy import tensor


# left_snake = Cap(Dim(2), Dim(2)) @ Id(Dim(2)) >> Id(Dim(2)) @ Cup(Dim(2), Dim(2))
# right_snake = Id(Dim(2)) @ Cap(Dim(2), Dim(2)) >> Cup(Dim(2), Dim(2)) @ Id(Dim(2))

# Equation(left_snake, Id(Dim(2)), right_snake).draw(figsize=(5, 2), draw_type_labels=False)

'''
Other stuff
'''

f = tensor.Box("f", Dim(2), Dim(2), data=[1, 2, 3, 4])

Equation(f.transpose(), f.r).draw(figsize=(3, 2), draw_type_labels=False)

assert f.r.eval() == f.transpose().eval()
print(f.r.eval())


from discopy.quantum import qubit, H, Id, CX, QuantumGate

assert H == QuantumGate("H", qubit, qubit, data=[2 ** -0.5 * x for x in [1, 1, 1, -1]], is_dagger=None, z=None)


circuit = H @ qubit >> CX

circuit.draw(figsize=(2, 2), draw_type_labels=True, margins=(.1, .1))
