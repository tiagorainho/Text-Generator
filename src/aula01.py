
from Generator import Generator
from FCM import FCM

def main():

    fcm = FCM(2, 1)
    fcm.update("ola eu sou o tiago, ola")
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