from MarkovChain import MarkovChain

class Generator:

    markov_chain = None

    def __init__(self, k=1, ):
        markov_chain = MarkovChain()

    
    def get_next(self, character):
        while True:
            # ver ultimo valor
            ultimo = "A"
            yield next(ultimo)