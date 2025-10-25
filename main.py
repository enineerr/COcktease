from time import sleep as s
from random import randint
from pathlib import Path
from os import system


class b2tb:
    def __init__(self) -> None:
        self.min: int = 1
        self.max: int = 3
        self.formats = ["mp3", "wav", "aac", "flac", "mp4", "mov"]
        self.main()

    def main(self):
        while (True):
            timeout = randint(self.min, self.max) / 60
            print(timeout)
            s(timeout)

            mpL = []
            for i in self.formats:
                mp = Path("/home/user/Music/Cocktease/.").glob(f"*.{i}")
                for i in mp:
                    mpL.append(i)

            print(mpL)

            i = randint(0, len(mpL))

            system(f"ffplay -autoexit -nodisp {mpL[i].absolute()}")


b2tb()
