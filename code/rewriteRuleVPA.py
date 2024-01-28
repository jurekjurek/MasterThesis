from lambeq import RewriteRule


'''
Given a series of words, where does too are the last two words, this rewrite rule does a couple of things: 

    - it collapses does too -> does-too and assigns correct types 

    - it copies the verb using spider 

    - then connects the words using its own grammar rules 

'''



class VerbPhraseEllipsisRewriteRule(RewriteRule): 
    mapping = {
        'is' : 'was'
    }

    def matches(self, box) -> bool:
        return box.name in self.mapping

    def rewrite(self, box):
        new_name = self.mapping[box.name]
        return type(box)(name=new_name, dom = box.dom, cod = box.cod)
        
a = 6