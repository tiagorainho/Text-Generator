import sys
from Generator import Generator
from FCM import FCM

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 aula01.py <file_path> <k> <alpha>") 
    fcm = FCM(int(sys.argv[2]), int(sys.argv[3]))
    f = open(sys.argv[1],'r')
    file_str = f.read().replace('\n', '')
    fcm.update(file_str)
    print(fcm.finitecontext)

    '''
    text = "hihi"
    text_generated = ""
    text_to_learn = "ola eu sou o justino"
    fcm = FCM(text_to_learn)
    generator = Generator(fcm)
    for c in text:
        text_generated.join(generator.generate(c))
    print(text.join(text_generated))
    '''
    

if __name__ == '__main__':
    main()