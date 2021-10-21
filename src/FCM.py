
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

    def calculate_entropy(self):
        pass
