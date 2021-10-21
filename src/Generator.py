from FCM import FCM

class Generator:

    def __init__(self, fcm, k=1):
        self.fcm = fcm

    
    def generate(self, character):
        while True:
            # ver ultimo valor
            ultimo = "A"
            yield next(ultimo)