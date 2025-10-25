from time import sleep as s
from random import randint
from pathlib import Path
from os import system


class b2tb:
    def __init__(self) -> None:
        self.min: int = 1
        self.max: int = 3
        self.main()

    def main(self):
        while (True):
            timeout = randint(self.min, self.max) * 60
            print(timeout)
            s(timeout)

            mp = Path(".").glob("*.wav")

            mpL = []
            for i in mp:
                mpL.append(i)
            print(mpL)

            mp = mpL

            i = randint(0, len(mp))

            system(f"ffplay -autoexit -nodisp {mp[i].absolute()}")


b2tb()
