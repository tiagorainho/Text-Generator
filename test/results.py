import sys, random
from typing import List
sys.path.append('../src')
from FCM import FCM
from Generator import Generator


def results_generator(k:int, alpha:float, files:List[str], start_text:str, seed:int, generation_length:int):
    fcm = FCM(k=k, alpha=alpha)
    for file_str in files:
        fcm.update(file_str)
    
    random.seed(seed)
    generator = Generator(fcm)

    text_generator = generator.generate(start_text)
    result = ''
    for _ in range(generation_length):
        result += next(text_generator)
    
    return result


def results_fcm(k:int, alpha: float, files: List[str]):
    fcm = FCM(k=k, alpha=alpha)
    for file in files:
        with open(file) as f:
            print(f'Reading file {f.name}')
            fcm.update(f.read().replace('\n', ''))

    return fcm.calculate_entropy()

if __name__ == '__main__':

    files = ["../example/biblia.txt"]
    files_str = []
    for file in files:
        with open(file) as f:
            print(f"Reading file {f.name}")
            files_str.append(f.read().replace('\n', ''))

    alpha_range = [x/10 for x in range(0, 10)]
    alpha = 0.1
    for k in range(1,21):
        # for alpha in alpha_range:
        print(f"k: {k}  alpha: {alpha}")
        print(f'\'{results_generator(k, alpha, files_str, "and god said, let the", 10, 150)}\'')