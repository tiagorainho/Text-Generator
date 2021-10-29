import sys, random
sys.path.append('../src')
from FCM import FCM
from Generator import Generator

RED     = '\33[31m'
GREEN   = '\33[32m'
ENDL    = '\33[0m'

if __name__ == '__main__':
    k = 3
    alpha = 1
    files = ['../example/biblia.txt']
    seed = 100
    generation_length = 100
    text_generations = {
        "jesus": ", and also: the burdecause senny; 30:7 and he saying be remnly in the comercy, and jord samuel of go",
    }


    fcm = FCM(k=k, alpha=alpha)
    for file in files:
        with open(file) as f:
            print(f"Reading file {f.name}")
            fcm.update(f.read().replace('\n', ''))
    
    random.seed(seed)
    generator = Generator(fcm)

    for input, output in text_generations.items():
        text_generator = generator.generate(input)
        result = ''
        for _ in range(generation_length):
            result += next(text_generator)
        assert result == output, RED + f'\'{input}\' does not equals the output of the generator: \'{result}\'' + ENDL
        print(GREEN + f'\'{input}\' is correct' + ENDL)

    print(GREEN + '[All tests passed!]' + ENDL)