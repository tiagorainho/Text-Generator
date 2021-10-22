from FCM import FCM

class Generator:

    def __init__(self, fcm: FCM):
        self.fcm = fcm

    
    def generate(self, text:str = None):
        last_characters = text
        if text != None:
            while True:
                next_character = self._get_next(last_characters[-self.fcm.k:])
                if next_character == None: break
                last_characters = last_characters + next_character
                yield next_character
        return None

    def _get_next(self, last_characters):
        tuple_list = self.fcm.finitecontext.get(last_characters)
        if tuple_list != None:
            return max(tuple_list, key=lambda t: t[1])[0]
        return None
