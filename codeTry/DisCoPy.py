# from discopy.grammar.pregroup import Cap, Cup, Id, Ty, Word, Swap
# from lambeq import pregroups
# from discopy.drawing import Equation


'''
In this file, the transformation from 
does-too to does-too 
is done for one example. The task is to automate this! 
'''


from lambeq.backend.grammar import (Box, Cap, Cup, Diagram, Diagrammable,
                                    Functor, grammar, Id, Spider, Swap,
                                    Ty, Word)
from lambeq.backend.drawing import draw
import matplotlib.pyplot as plt
from lambeq import AtomicType

N = AtomicType.NOUN
S = AtomicType.SENTENCE




n, s = Ty('n'), Ty('s')

# words = [
#     Word('she', n),
#     Word('goes', n.r @ s @ n.l),
#     Word('home', n)
# ]



# create a diagram with the shape of verb phrase ellipsis
words = [
    Word('Alice', n),
    Word('drinks', n.r @ s),
    Word('and', s.r @ s @ s.l),
    Word('Bob', n),
    Word('does', n.r @ s),
    Word('too', s.r @ n.r.r @ n.r @ s)
]



cups = (Cup(N, N.r) @ Cup(S, S.r) @ Id(S) @ Id(s.l) @ Id(n) @ Id(n.r) @ Cup(s, s.r) @ Id(n.r.r) @ Id(n.r) @ Id(s) >> 
        Id(s) @ Id(s.l) @ Id(n) @ Cup(n.r, n.r.r) @ Id(n.r) @ Id(s) >> 
        Id(s) @ Id(s.l) @ Cup(n, n.r) @ Id(s) >> 
        Id(s) @ Cup(s.l, s))

assert Id().tensor(*words) == words[0] @ words[1] @ words[2] @ words[3] @ words[4] @ words[5]
# assert Ty().tensor(*[n.r, s, n.l]) == n.r @ s @ n.l
assert Ty().tensor(*[n.r, s]) == n.r @ s
# assert Ty().tensor(*[s.r, s]) == s.r @ s
# assert Ty().tensor(*[s.r, s, s.l]) == s.r @ s @ s.l
# assert Ty().tensor(*[s.r, n.r.r, n.r, s]) == s.r @ n.r.r @ n.r @ s


diagram = Id().tensor(*words) >> cups
# pregroups.draw(diagram)

diagram.draw()


# from discopy.frobenius import Spider
# from discopy import frobenius

# And what we want to do is to write a functor that gets us to this diagram:

n, s = Ty('n'), Ty('s')



# types of words stay the same, besides does and too: 
# create a diagram with the shape of verb phrase ellipsis
words = [
    Word('Alice', N),
    Word('drinks', N.r @ S),
    Word('and', S.r @ S @ S.l),
    Word('Bob', N),
    Word('does-too', S @ N.r @ N.r.r @ s.r)
]
# from discopy.drawing import Equation
# from discopy.grammar.pregroup import Spider, Ty




# firstLine is something like the new grammar here... 
# the >> means that the instructions are for a new line 


'''
From discopy to lambeq, spiders have different formats: 

DisCoPy: Spider(nLegsIn, nLegsOut, N / S)

Lambeq: Spider(N / S, nLegsIn, nLegsOut) 

'''

firstLine = (Id(N) @ Spider(N.r, 1,2) @ Spider(S, 1,2) @ Id(s.r) @ Id(s) @ Id(s.l) @ Id(n) @ Id(s) @ Id(n.r) @ Id(n.r.r) @ Id(s.r) >> 
            Cup(n, n.r) @ Id(n.r) @ Id(s) @ Cup(s, s.r) @ Id(s) @ Id(s.l) @ Swap(n,s) @ Id(n.r) @ Id(n.r.r) @ Id(s.r) >> 
            Id(n.r) @ Id(s) @ Id(s) @ Cup(s.l, s) @ Cup(n, n.r) @ Id(n.r.r) @ Id(s.r) >> 
            Id(n.r) @ Swap(s,s) @ Id(n.r.r) @ Id(s.r) >> 
            Id(n.r) @ Id(s) @ Swap(s, n.r.r) @ Id(s.r) >> 
            Id(n.r) @ Id(s) @ Id(n.r.r) @ Cup(s, s.r) >> 
            Swap(n.r, s) @ Id(n.r.r) >> Id(s) @ Cup(n.r, n.r.r))



diagram = Id().tensor(*words) >> firstLine

diagram.draw()




'''
ADD CAPS
'''



# we remove the word does-too step by step from the diagram, introducing two caps
firstLine = (Id(n) @ Id(n.r) @ Id(s) @ Id(s.r) @ Id(s) @ Id(s.l) @ Id(n) @ Cap(s.r, s) >> 
            Id(n) @ Id(n.r) @ Id(s) @ Id(s.r) @ Id(s) @ Id(s.l) @ Id(n) @ Swap(s.r, s) >> 
            Id(n) @ Id(n.r) @ Id(s) @ Id(s.r) @ Id(s) @ Id(s.l) @ Id(n) @ Id(s) @ Cap(N.r.r, N.r) @ Id(s.r) >> 
            Id(n) @ Spider(n.r, 1,2) @ Spider(s, 1,2) @ Id(s.r) @ Id(s) @ Id(s.l) @ Id(n) @ Id(s) @ Id(n.r.r) @ Id(n.r) @ Id(s.r) >> 
            Cup(n, n.r) @ Id(n.r) @ Id(s) @ Cup(s, s.r) @ Id(s) @ Id(s.l) @ Swap(n,s) @ Swap(n.r.r, n.r) @ Id(s.r) >> 
            Id(n.r) @ Id(s) @ Id(s) @ Cup(s.l, s) @ Cup(n, n.r) @ Id(n.r.r) @ Id(s.r) >> 
            Id(n.r) @ Swap(s,s) @ Id(n.r.r) @ Id(s.r) >> 
            Id(n.r) @ Id(s) @ Swap(s, n.r.r) @ Id(s.r) >> 
            Id(n.r) @ Id(s) @ Id(n.r.r) @ Cup(s, s.r) >> 
            Swap(n.r, s) @ Id(n.r.r) >> Id(s) @ Cup(n.r, n.r.r))

nextWords = [
    Word('Alice', n),
    Word('drinks', n.r @ s),
    Word('and', s.r @ s @ s.l),
    Word('Bob', n)
]

diagram = Id().tensor(*nextWords) >> firstLine
diagram.draw()
diagram.normal_form().draw()




# does not work
# from lambeq import RemoveSwapsRewriter
# remove_swaps = RemoveSwapsRewriter()
# diagWithoutSwaps = remove_swaps(diagram)
# diagWithoutSwaps.draw()



'''
finally, the simplified diagram 
'''


firstLine = (Id(n) @ Spider(n.r, 1,2) @ Spider(s, 1,2) @ Id(s.r) @ Id(s) @ Id(s.l) @ Id(n) >> 
            Cup(n, n.r) @ Id(n.r) @ Id(s) @ Cup(s, s.r) @ Swap(s, s.l) @ Id(n) >> 
            Id(n.r) @ Id(s) @ Cup(s.l, s) @ Id(n) >> 
            Id(n.r) @ Swap(s, n) >> 
            Swap(n.r, n) @ Id(s) >>
            Cup(n, n.r) @ Id(s))

nextWords = [
    Word('Alice', n),
    Word('drinks', n.r @ s),
    Word('and', s.r @ s @ s.l),
    Word('Bob', n)
]

diagram = Id().tensor(*nextWords) >> firstLine
diagram.draw()





from lambeq import RemoveSwapsRewriter, RemoveCupsRewriter
from lambeq import Rewriter 

remove_cups = RemoveCupsRewriter()
remove_swaps = RemoveSwapsRewriter()
diagWithoutSwaps = remove_cups(diagram)
diagWithoutSwaps.draw()
# diagram.normal_form().draw()

coordDiag = Rewriter(['coordination'])(diagram)



draw(remove_cups(coordDiag))
print('↓ normal form')

finalOne = remove_cups(coordDiag).normal_form()

# try to remove swaps again 
# finaOneWithoutSwaps = remove_swaps(finalOne)

# draw(finaOneWithoutSwaps)




# final, final diagram 
firstLine = (Spider(n, 2, 1) @ Id(n.r) @ Id(s) >> 
            Cup(n, n.r) @ Id(s) )

nextWords = [
    Word('Alice', n),
    Word('Bob', n),
    Word('drinks', n.r @ s)
]

diagram = Id().tensor(*nextWords) >> firstLine
diagram.draw()

finalDiag = remove_cups(diagram)

draw(finalDiag)



'''
Next Example: 

    Gary likes his code and Bill does too. 

'''


from lambeq import BobcatParser

sentence = 'Gary likes his code and Bill does too.'

# Parse the sentence and convert it into a string diagram
parser = BobcatParser(verbose='suppress')
diagram = parser.sentence2diagram(sentence)

diagram.draw(figsize=(14,3), fontsize=12)


# final, final diagram 
firstLine = (Spider(n, 3, 2) @ Id(n.r) @ Swap(s, n.l) >>
            Id(n) @ Cup(n, n.r) @ Id(n.l) @ Id(s) >>
            Swap(n, n.l) @ Id(s) >>
            Cup(n.l, n) @ Id(s))

nextWords = [
    Word('code', n),
    Word('Gary', n),
    Word('Bill', n),
    Word('likes', n.r @ s @ n.l)
]

diagram = Id().tensor(*nextWords) >> firstLine
diagram.draw()










