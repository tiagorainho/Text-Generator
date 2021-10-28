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
            random_number = random.randint(1, sum(t[1] for t in tuple_list))
            counter = 0
            for t in tuple_list:
                if random_number > counter and random_number <= counter+t[1]:
                    return t[0]
                counter += t[1]
        return random.sample(self.fcm.characters, 1)[0]
