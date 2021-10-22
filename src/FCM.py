
import math

# Finite Context Model
class FCM:

    '''
        str = "aabaac"
        k = 1
        {
            "a": [("a", 2), ("b", 1), ("c", 1)],
            "b": [("a", 1)]
        }
    '''
    
    def __init__(self, k, alpha): # assumimos que o context do modelo é o k
        self.finitecontext = dict()
        self.k = k
        self.alpha = alpha

    def update(self, text):
        last_characters = ''

        for c in text:
            if len(last_characters) == self.k:
                # adicionar ao finite context
                occurences = self.finitecontext.get(last_characters)
                if occurences != None:
                    found = False
                    for tpl in occurences:
                        if tpl[0] == c:
                            found = True
                            aux = (tpl[0], tpl[1]+1)
                            occurences.remove(tpl)
                            occurences.append(aux)
                            break
                    if not found:
                        occurences.append((c,1))
                    self.finitecontext[last_characters] = occurences # garantir que precisa msm desta linha ou fica por referencia
                else:
                    self.finitecontext[last_characters] = [(c,1)]
                # shift left the last characters
                last_characters = last_characters[1:]
            last_characters = last_characters + c

    def calculate_cardinality(self, text):
        return len(set(text))



    def calculate_entropy(self):
        cardinality = self.calculate_cardinality()
        H = 0
        for context, tuple_list in self.finitecontext.items():
            Hc = 0
            Pec = 0
            Psc = 0
            for t in tuple_list:
                Psc += t[1]
            for t in tuple_list:
                Pec = (t[1] + self.alpha) / (Psc + self.alpha * cardinality)
                information_amount = - math.log2(Pec)
                Hc = information_amount * Pec

            H += Hc*Pec
        return H

