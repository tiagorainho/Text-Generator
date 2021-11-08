import sys, random
from typing import List
sys.path.append('../src')
from FCM import FCM
from Generator import Generator
import time
import cProfile


def results_generator(k:int, alpha:float, files:List[str], start_text:str, seed:int, generation_length:int):
    fcm = FCM(k=k, alpha=alpha)
    for file_str in files:
        fcm.update(file_str)
    random.seed(seed)
    generator = Generator(fcm)
    return generator.generate_string(start_text, generation_length)


def calculate_entropy_fast(k_range:List[int], alpha_range:List[int], files_str: List[str]):
    for k in k_range:
        start = time.time()
        fcm = FCM(k=k, alpha=0)
        for file_str in files_str:
            fcm.update(file_str)
        print(f"#####   FCM creation: k={k}, creation_time={round(time.time()-start,3)} seconds   #####")
        for alpha in alpha_range:
            fcm.alpha = alpha
            start = time.time()
            entropy = fcm.calculate_entropy()
            print(f"k: {k}  alpha: {alpha}  entropy: {entropy}  entropy_calculation_time: {round(time.time()-start,3)}")


def results_fcm(k:int, alpha: float, files_str: List[str]):            
    start = time.time()
    fcm = FCM(k=k, alpha=alpha)
    for file_str in files_str:
        fcm.update(file_str)
    print(f"fcm len: {str(len(fcm.finitecontext))}")
    print(f"fcm_creation_elapsed_time: {time.time()-start}")
    #start = time.time()
    #entropy = fcm.calculate_entropy()
    #print(f"fcm_calculate_entropy_time: {time.time()-start}")
    #return entropy


def main():
    test_entropy, test_generator = True, False
    fast_run = False
    seed = 100
    chars_to_generate = 500
    alpha_range = [0.4]#[x/10 for x in range(0, 11)]
    k_range = [20]#[k for k in range(1,21)]
    files = ["../example/biblia.txt"]
    
    '''
    files = ["../example/hp/example1.txt",
        "../example/hp/example2.txt",
        "../example/hp/example3.txt",
        "../example/hp/example4.txt",
        "../example/hp/example5.txt",
        "../example/hp/example6.txt",
        "../example/hp/example7.txt",
    ]
    '''

    files_str = []
    for file in files:
        with open(file) as f:
            print(f"Reading file {f.name}")
            files_str.append(f.read())
    
    
    if test_entropy:
        if fast_run:
            calculate_entropy_fast(k_range, alpha_range, files_str)
        else:
            for alpha in alpha_range:
                for k in k_range:
                    entropy = results_fcm(k, alpha, files_str)
                    print(f"k: {k}  alpha: {alpha}  entropy: {entropy}")
    if test_generator:
        print(f'\'{results_generator(k, alpha, files_str, "and god said, let the", seed, chars_to_generate)}\'')


if __name__ == '__main__':
    cProfile.run('main()')
