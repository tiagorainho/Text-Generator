
from Generator import Generator

def main():
    text = "gosto mt da luisa, mas ela n curte de mim"
    text_generated = ""
    generator = Generator()
    for c in text:
        text_generated.join(generator.get_next(c))
    print(text.join(text_generated))

if __name__ == '__main__':
    main()