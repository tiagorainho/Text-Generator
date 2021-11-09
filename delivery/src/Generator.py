from FCM import FCM
import random, time, signal
from argparse import ArgumentParser

passNext: bool = False

class Generator:

    def __init__(self, fcm: FCM):
        self.fcm = fcm


    def generate_string(self, context:str, output_length:int):
        generator_iterator = self.generate(context)
        text = ''
        for _ in range(output_length):
            next_char = next(generator_iterator)
            if next_char == None: break
            text += next_char
        return text

    
    def generate(self, context:str = None) -> str:
        last_characters = context[-self.fcm.k:]
        if context != None:
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
            probabilities = [(event, self.fcm.probability_e_c(event, last_characters)) for event, count in tuple_list]
            random_float = random.random()%sum([p[1] for p in probabilities])
            for event, probability in probabilities:
                if random_float > counter and random_float <= counter+probability:
                    return event
                counter += probability
        return ''.join(random.choice(''.join(char for char in self.fcm.characters)))
        #return None


def KillHandler(signum, frame):
    global passNext
    passNext = True

signal.signal(signal.SIGTSTP, KillHandler)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--files", metavar="files", nargs="+", type=str, required=True,
                        help="List of files to train the model")
    parser.add_argument("--alpha", metavar="alpha", type=float, required=False, default=1,
                        help="Variable responsible for smoothing")
    parser.add_argument("--k", metavar="sliding window", type=int, required=False, default=5,
                        help="Size of shifting window")
    parser.add_argument("--seed", metavar="seed", type=int, required=False, default=time.time_ns(),
                        help="Seed of the pseudo-random value generator")
    parser.add_argument("--context", metavar="context", nargs="+", type=str, required=False, default=None,
                        help="Context to generate the next characters")
    parser.add_argument("--output", metavar="output size ", type=int, required=False, default=100,
                        help="Output size in characters of the values generated")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    
    random.seed(a=args.seed)

    fcm = FCM(k=args.k, alpha=args.alpha)
    for file in args.files:
        with open(file) as f:
            print(f"Reading file {f.name}")
            fcm.update(f.read())

    generator = Generator(fcm)
    
    if args.context == None:
        print("Press Ctrl-Z to stop response")  
        while True:
            context = input("Input: ")
            text_generated = generator.generate_string(context, args.output)
            print("Generated:")
            for char in text_generated:
                print(char, end='', flush=True)
                if passNext:
                    passNext = False
                    break
                time.sleep(0.05)
            print("\n")
    else:
        print(generator.generate_string(' '.join(args.context), args.output))