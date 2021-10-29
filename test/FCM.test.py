
import sys
sys.path.append('../src')
from FCM import FCM

RED     = '\33[31m'
GREEN   = '\33[32m'
ENDL    = '\33[0m'

if __name__ == '__main__':
    k = 3
    alpha = 1
    files = ['../example/biblia.txt']


    fcm = FCM(k=k, alpha=alpha)
    for file in files:
        with open(file) as f:
            print(f'Reading file {f.name}')
            fcm.update(f.read().replace('\n', ''))

    assert fcm.calculate_entropy() == 4.6772849758349615, RED + 'fcm.calculate_entropy() is not well computed' + ENDL
    print(GREEN + 'fcm.calculate_entropy()' + ENDL)    

    print(GREEN + '[All tests passed!]' + ENDL)
