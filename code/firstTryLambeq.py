from lambeq import SpacyTokeniser

from lambeq import BobcatParser, pregroups
from lambeq import remove_cups


tokeniser = SpacyTokeniser()

sentence = 'Alice drinks and Bob does too.'

tokens = tokeniser.tokenise_sentence(sentence)

print('test')

parser = BobcatParser()#verbose='suppress')

print('test')

diagram = parser.sentence2diagram(tokens, tokenised=True)

print('test')

pregroups.draw(diagram, figsize = (23,4), fontsize = 12)

exit()
from lambeq import Rewriter

rewriter = Rewriter(['coordination'])
rewritten_diagram = rewriter(diagram)


rewritten_diagram.draw(figsize=(11,5), fontsize=13)

exit()

normalised_diagram = rewriter(diagram).normal_form()
normalised_diagram.draw(figsize=(9,4), fontsize=13)

remove_cups(rewritten_diagram).draw()

'''
Does a given noun sentence contain a subject- or object-based relative clause? 



'''

import os
import warnings

warnings.filterwarnings('ignore')
os.environ['TOKENIZERS_PARALLELISM'] = 'true'
