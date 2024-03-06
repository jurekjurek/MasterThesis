from lambeq.backend.grammar import Cup, Diagram, Id, Word
from lambeq.backend.drawing import draw

from lambeq import AtomicType

N = AtomicType.NOUN
S = AtomicType.SENTENCE
     

from lambeq import Rewriter

rewriter = Rewriter()





cows = Word('cows', N)
that_subj = Word('that', N.r @ N @ S.l @ N)
that_obj = Word('that', N.r @ N @ N.l.l @ S.l)
eat = Word('eat', N >> S << N)
grass = Word('grass', N)

rewriter = Rewriter(['subject_rel_pronoun'])

diagram = Id().tensor(cows, that_subj, eat, grass)
diagram >>= Cup(N, N.r) @ Id(N) @ Diagram.cups(S.l @ N, N.r @ S) @ Cup(N.l, N)

draw(diagram)
print('↓ rewriting (subject relative pronoun rule)')
draw(Rewriter(['subject_rel_pronoun'])(diagram))







class CoordinationRewriteRule(RewriteRule):
    """A rewrite rule for coordination.

    This rule matches the word 'and' with codomain
    :py:obj:`a.r @ a @ a.l` for pregroup type :py:obj:`a`, and replaces
    the word, based on [Kar2016]_, with a layer of interleaving spiders.

    """
    def __init__(self, words: Container[str] | None = None) -> None:
        """Instantiate a CoordinationRewriteRule.

        Parameters
        ----------
        words : container of str, optional
            A list of words to be rewritten by this rule. If a box does
            not have one of these words, it will not be rewritten, even
            if the codomain matches.
            If omitted, the rewrite applies only to the word "and".

        """
        self.words = ['and'] if words is None else words


    '''
    Should the given box be rewritten???
    '''
    def matches(self, box: Box) -> bool:
        if box.name in self.words and len(box.cod) % 3 == 0:
            n = len(box.cod) // 3
            left, mid, right = box.cod[:n], box.cod[n:2*n], box.cod[2*n:]
            return bool(right.r == mid == left.l)
        return False


    ''' if matches(), then the box is rewritten '''
    
    def rewrite(self, box: Box) -> Diagrammable:
        n = len(box.cod) // 3
        left, mid, right = box.cod[:n], box.cod[n:2*n], box.cod[2*n:]
        assert right.r == mid == left.l
        return (Diagram.caps(left, mid) @ Diagram.caps(mid, right)
                >> Id(left) @ Spider(mid, 2, 1) @ Id(right))

