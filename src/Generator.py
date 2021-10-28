from FCM import FCM
import random

class Generator:

    def __init__(self, fcm: FCM):
        self.fcm = fcm

    
    def generate(self, text:str = None) -> str:
        last_characters = text[-self.fcm.k:]
        if text != None:
            while True:
                next_character = self._get_next(last_characters)
                if next_character == None: break
                last_characters = last_characters[1:] + next_character
                yield next_character
        return None

    def _get_next(self, last_characters:str):
        tuple_list = self.fcm.finitecontext.get(last_characters)
        if tuple_list != None:
            counter = 0
            probabilities = [(event, self.fcm.probability_e_c(event, last_characters)) for (event, count) in tuple_list]
            random_float = random.random()%sum([p[1] for p in probabilities])
            for event, probability in probabilities:
                if random_float > counter and random_float <= counter+probability:
                    return event
                counter += probability
        return random.sample(self.fcm.characters, 1)[0]

        # (1 + 0.5 )/ (9 + 0.5*91) = 0.0275229358



