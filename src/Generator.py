from FCM import FCM
import random, time, signal
from argparse import ArgumentParser

passNext: bool = False

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
        #return random.sample(self.fcm.characters, 1)[0]
        return None

def KillHandler(signum, frame):
    global passNext
    passNext = True

signal.signal(signal.SIGTSTP, KillHandler)

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--files", metavar="files", nargs="+", type=str, required=True,
                        help="File to read")
    parser.add_argument("--alpha", metavar="alpha", type=float, required=False, default=1,
                        help="Variable responsible for smoothing")
    parser.add_argument("--k", metavar="k", type=int, required=False, default=5,
                        help="Size of shifting window")
    parser.add_argument("--seed", metavar="seed", type=int, required=False, default=100,
                        help="Seed of the pseudo-random value generator")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    fcm = FCM(k=args.k, alpha=args.alpha)
    for file in args.files:
        with open(file) as f:
            print(f"Reading file {f.name}")
            fcm.update(f.read().replace('\n', ''))
    
    random.seed(args.seed)
    generator = Generator(fcm)
    
    print("Press Ctrl-Z to stop response")
    while True:
        text = input("Input: ")
        text_generator = generator.generate(text)

        print("\nResponse: ", end='', flush=True)
        while True:
            next_char = next(text_generator)
            if next_char == None:
                print("No more characters could be made")
                break
            print(next_char, end='', flush=True)
            if passNext:
                passNext = False
                break
            time.sleep(0.05)
        print("\n")
    