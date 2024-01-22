import random
import string

gen = random.sample(string.ascii_letters +
                    string.digits + string.punctuation, k=16)

pswd = "".join(gen)

if __name__ == "__main__":
    print(pswd)
