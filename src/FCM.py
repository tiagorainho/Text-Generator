
import math

# Finite Context Model
class FCM:
    
    def __init__(self, k, alpha): # assumimos que o context do modelo é o k
        self.finitecontext = dict()
        self.k = k
        self.alpha = alpha
        self.characters = set()
        self.cardinality = None

    def update(self, text: str):
        last_characters = ''

        if self.cardinality == None:
            self.load_alphabet(self.characters.union(set(text)))

        for c in text:
            self.characters.add(c)

            #print("----------------------------------")
            #print("total entropy: " + str(self.calculate_entropy()))
            if len(last_characters) == self.k:

                #print("P(" +c + "|" + last_characters + ": " + str(self.information_amount(c, last_characters)))
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

    def load_alphabet(self, text):
        self.cardinality = len(set(text))

    def information_amount(self, event, context):
        Psc = 0
        Pec = 0
        tuple_list = self.finitecontext.get(context)
        if tuple_list == None: return 0
        for t in tuple_list:
            Psc += t[1]
        for t in tuple_list:
            if t[0] == event:
                Pec = (t[1] + self.alpha) / (Psc + self.alpha * self.cardinality)
        if Pec == 0:
            Pec = (0 + self.alpha) / (Psc + self.alpha * self.cardinality)
        return -1*math.log2(Pec)

    def calculate_entropy(self):
        H = 0
        for context, tuple_list in self.finitecontext.items():
            Hc = Psc = Pec = 0
            for t in tuple_list:
                Psc += t[1]
            for t in tuple_list:
                Pec = (t[1] + self.alpha) / (Psc + self.alpha * self.cardinality)
                information_amount = - math.log2(Pec)
                Hc += information_amount * Pec
            if self.cardinality > len(tuple_list):
                Pec = (0 + self.alpha) / (Psc + self.alpha * self.cardinality)
                information_amount = - math.log2(Pec)
                Hc += (information_amount * Pec) * (self.cardinality - len(tuple_list)) #verify
            H += Hc * 1/len(self.finitecontext.keys()) #verify
        return H

