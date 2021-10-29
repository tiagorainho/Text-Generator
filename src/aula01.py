import sys
from typing import List
from Generator import Generator
from FCM import FCM
import time, json

def add_files(fcm: FCM, files: List[str]):    
    #fcm.load_alphabet("ACGT")
    for file in files:
        add_file(file, fcm)


def add_conversational_files(fcm: FCM):
    conversations = []
    f = open("example/movie-conversations.json")
    data = json.load(f)
    for conversation in data:
        for c in conversation["utterances"]:
            conversations.append(c["speaker"] + ": " + c["text"])
    f.close()
    for c in conversations:
        fcm.update(c)


def main(k, alpha):

    fcm = FCM(k, alpha)
    add_files(fcm, ['example/biblia.txt'])
    #add_conversational_files(fcm)
    
    generator = Generator(fcm)
    
    while True:
        text = input("Input: ")

        text_generator = generator.generate(text)

        print("\nResponse: ", end='', flush=True)
        while True:
            next_char = next(text_generator)
            if next_char == None:
                print("No more characters could be made")
                break
            print(next_char, end='', flush=True)
            if next_char == '.':
                break
            time.sleep(0.05)
        print("\n")

def add_file(file, fcm):
    with open(file) as f:
        file_str = f.read().replace('\n', '')
        fcm.update(file_str)




if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Usage: python3 aula01.py <k> <alpha>")

    main(int(sys.argv[1]), float(sys.argv[2]))
