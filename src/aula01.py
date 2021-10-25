import sys
from Generator import Generator
from FCM import FCM
import time, string

def main(k, alpha):

    files = ['example/example3.txt', 'example/example4.txt']

    fcm = FCM(k, alpha)
    #fcm.load_alphabet("ACGT")

    for file in files:
        add_file(file ,fcm)

    fcm.update("From Romeo and Juliet to King Lear to Macbeth to all of his stunning sonnets and other works, William Shakespeare’s top spot in the literary world has been solidified for centuries. Although his work is well-covered in many schools, famous Shakespeare quotes do not only belong in English courses for study. We can all appreciate his tongue-in-cheek observations about society and individuals’ behavior, as well as gain inspiration and wisdom from his quick-witted quips and smart sense of humor. Not only that, he can help us find beauty through language—including an appreciation for vulnerable declarations of love.")
    
    generator = Generator(fcm)
    text = "famous Shakespeare quotes"

    returned_text = generator.generate(text)

    print("Input: " + text + "\nResponse: ", end='', flush=True)
    while True:
        next_char = next(returned_text)
        if next_char == None:
            print("No more characters could be made")
            break
        print(next_char, end='', flush=True)
        time.sleep(0.1)

def add_file(file, fcm):
    with open('../' + file) as f:
        file_str = f.read().replace('\n', '')#.lower()
        fcm.update(file_str)

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Usage: python3 aula01.py <k> <alpha>")

    #if len(sys.argv) != 4:
    #    print("Usage: python3 aula01.py <file_path> <k> <alpha>")
        
    #f = open(sys.argv[1], 'r')
    #file_str = f.read().replace('\n', '')

    main(int(sys.argv[1]), int(sys.argv[2]))