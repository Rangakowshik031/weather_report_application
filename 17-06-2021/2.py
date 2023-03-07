''' combination of multilevel inheritance and multiple inheritance'''
''' A,C,D,E -----> multilevel    A,B,E--->multiple'''

class A:
    pass
class B:
    pass
class C(A):
    pass
class D(C):
    pass
class E(D):
    pass
class F(A,B):
    pass


print(E.mro())
print(F.mro())
