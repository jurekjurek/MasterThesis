from discopy.grammar.pregroup import Cap, Cup, Id, Ty, Word, Diagram
from lambeq import pregroups

from discopy.symmetric import Diagram, Functor

# from discopy.tensor import Dim, Tensor
from discopy import tensor

from discopy.grammar.pregroup import Ty, Id, Word, Cup, Diagram
from discopy.drawing import Equation

n, s = Ty('n'), Ty('s')

Alice = Word("Alice", n)
loves = Word("loves", n.r @ s @ n.l)
Bob = Word("Bob", n)


# add grammar 
grammar = Cup(n, n.r) @ s @ Cup(n.l, n)

sentence = Alice @ loves @ Bob >> grammar
sentence.draw(figsize=(5, 5))

from discopy.cat import Category

F = tensor.Functor(
    ob={n: 2, s: 1},
    ar={Alice: [0, 1], loves: [0, 1, 1, 0], Bob: [1, 0]},
    dom=Category(Ty, Diagram))

print(F(Alice @ loves @ Bob))
print(F(grammar))

assert F(Alice @ loves @ Bob >> grammar).array == 1

q = Ty('q')

Who = Word("Who", q @ s.l @ n)

F.ob[q], F.ar[Who] = 2, [1, 0, 0, 1]

question = Who @ loves @ Bob\
    >> Id(q @ s.l) @ Cup(n, n.r) @ Id(s) @ Cup(n.l, n)\
    >> Id(q) @ Cup(s.l, s)

answer = Alice

assert F(question) == F(answer)

Equation(question, answer).draw(figsize=(6, 3))

