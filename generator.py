import random
import string


def generate():
    gen = random.sample(string.ascii_letters +
                        string.digits + string.punctuation, k=16)

    pswd = "".join(gen)

    return pswd


if __name__ == "__main__":
    print(generate())
    input()
