from ket import *
from ket.code_ket import code_ket

def bell(aux0, aux1):
    q = quant(2)
    if aux0 == 1:
        x(q[0])
    if aux1 == 1:
        x(q[1])
    h(q[0])
    ctrl(q[0], x, q[1])
    return q

@code_ket
def teleport(a):
    b = bell(0, 0)
    with control(a):
        x(b[0])
    h(a)
    m0 = measure(a)
    m1 = measure(b[0])
    if m1 == 1:
        x(b[1])
    if m0 == 1:
        z(b[1])
    return b[1]

a = quant(1)    # a = |0>
h(a)            # a = |+> 
z(a)            # a = |->
y = teleport(a) # y <- a
h(y)            # y = |1>
print('Expected measure 1, result =', measure(y).get())
     