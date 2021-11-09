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
    files = ["../example/hp/example1.txt","../example/hp/example2.txt","../example/hp/example3.txt","../example/hp/example4.txt","../example/hp/example5.txt",
             "../example/hp/example6.txt", "../example/hp/example7.txt"]
    if test_generator:
        files_str = []
        for file in files:
            with open(file) as f:
                print(f"Reading file {f.name}")
                files_str.append(f.read())
                
    for k in [15]:
        for alpha in [0, 0.5, 1]:
            if test_entropy:
                entropy = results_fcm(k, alpha, files)
                print(f"k: {k}  alpha: {alpha}  entropy: {entropy}")
            if test_generator:
                print("\\begin{lstlisting}[language={},caption={harry books all; k=",k,"; alpha=",alpha,": entry=Harry Potter was}]")
                print(f'\'{results_generator(k, alpha, files_str, "Harry Potter was", 100, 700)}\'')
                print("\end{lstlisting}")

