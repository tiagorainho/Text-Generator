import sys
from Generator import Generator
from FCM import FCM
import time

def main(k, alpha, text):

    fcm = FCM(k, alpha)
    #fcm.load_alphabet("ACGT")

    fcm.update(text)
    fcm.update("abcdefghijklmnopqrstuvxzABCDEFGHIJKLMNOPQRSTUVXZ")
    fcm.update("From Romeo and Juliet to King Lear to Macbeth to all of his stunning sonnets and other works, William Shakespeare’s top spot in the literary world has been solidified for centuries. Although his work is well-covered in many schools, famous Shakespeare quotes do not only belong in English courses for study. We can all appreciate his tongue-in-cheek observations about society and individuals’ behavior, as well as gain inspiration and wisdom from his quick-witted quips and smart sense of humor. Not only that, he can help us find beauty through language—including an appreciation for vulnerable declarations of love.")
    
    generator = Generator(fcm)
    text = "O livro O Principezinho fala de um menino que vivia num planeta"

    returned_text = generator.generate(text)

    print("Input: " + text + "\nResponse: ", end='', flush=True)
    while True:
        next_char = next(returned_text)
        if next_char == None:
            print("No more characters could be made")
            break
        print(next_char, end='', flush=True)
        time.sleep(0.1)
    

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 aula01.py <file_path> <k> <alpha>")
        
    f = open(sys.argv[1], 'r')
    file_str = f.read().replace('\n', '')

    main(int(sys.argv[2]), int(sys.argv[3]), file_str)