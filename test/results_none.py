import sys, random
from typing import List
sys.path.append('../src')
from FCM import FCM
from Generator import Generator

def results_generator_optimized(fcm: FCM, start_text:str, seed:int, generation_length:int):
    random.seed(seed)
    generator = Generator(fcm)

    text_generator = generator.generate(start_text)
    result = ''
    next_char  = ''
    while len(result) < generation_length:
        try:
            next_char = next(text_generator)
            print(next_char, end='', flush=True)
        except StopIteration:
            break
        
        result += next_char
    return result


def results_generator(k:int, alpha:float, files:List[str], start_text:str, seed:int, generation_length:int):
    fcm = FCM(k=k, alpha=alpha)
    for file_str in files:
        fcm.update(file_str)
    
    random.seed(seed)
    generator = Generator(fcm)

    text_generator = generator.generate(start_text)
    result = ''
    next_char  = ''
    while len(result) < generation_length:
        try:
            next_char = next(text_generator)
            print(next_char, end='', flush=True)
        except StopIteration:
            print(f"Num. caracters: {len(result)}")
            break
        
        result += next_char
    print(f"Num. caracters: {len(result)}")
    return result


def results_fcm(k:int, alpha: float, files_str: List[str]):
    fcm = FCM(k=k, alpha=alpha)
    for f_str in files_str:
        fcm.update(f_str)

    return fcm.calculate_entropy()

if __name__ == '__main__':

    files = ["../example/hp/example1.txt","../example/hp/example2.txt","../example/hp/example3.txt","../example/hp/example4.txt","../example/hp/example5.txt","../example/hp/example6.txt","../example/hp/example7.txt"]
    files_str = []
    for file in files:
        with open(file) as f:
            print(f"Reading file {f.name}")
            files_str.append(f.read().replace('\n', ''))
    alpha_range = [x/10 for x in range(0, 11)]
    
    for k in range(1,13):
        fcm = FCM(k=k, alpha=1)

        for file_str in files_str:
            fcm.update(file_str)
        
        for alpha in alpha_range:
            fcm.alpha = alpha
            #entropy = results_fcm(k, alpha, files_str)
            print(f"k: {k}  alpha: {alpha}")  #entropy: {entropy}")
            results = results_generator_optimized(fcm, "Harry Potter", 10, 500)
            print(f'\'{results}\'\nNum. of Chars: {len(results)}\n\n')

