import sys, random
from typing import List
sys.path.append('../src')
from FCM import FCM
from Generator import Generator
import time


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
    files_str = []
    for file in files:
        with open(file) as f:
            files_str.append(f.read())
            
    start = time.time()
    fcm = FCM(k=k, alpha=alpha)
    for file_str in files_str:
        fcm.update(file_str)
    print(f"fcm_creation_elapsed_time: {time.time()-start}")
    start = time.time()
    entropy = fcm.calculate_entropy()
    print(f"fcm_calculate_entropy_time: {time.time()-start}")
    return entropy


if __name__ == '__main__':
    test_entropy, test_generator = False, True

    files = ["../example/biblia.txt"]
    if test_generator:
        files_str = []
        for file in files:
            with open(file) as f:
                print(f"Reading file {f.name}")
                files_str.append(f.read())

    for alpha in [x/10 for x in range(0, 11)]:
        for k in range(1,21):
            if test_entropy:
                entropy = results_fcm(k, alpha, files)
                print(f"k: {k}  alpha: {alpha}  entropy: {entropy}")
            if test_generator:
                print(f'\'{results_generator(k, alpha, files_str, "and god said, let the", 10, 500)}\'')

