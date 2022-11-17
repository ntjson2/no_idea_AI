from dalle2 import Dalle2
import os

class Dalle():
    def __init__(self):
        self.d = Dalle2(os.getenv("DALLE2KEY"))

    def get_single_image_path(self, prompt):
        d = self.d
        g = d.generate(str(prompt))

        print(f"> length of list: {len(g)}")

        return g[0].get("generation").get("image_path")

def main():
    d = Dalle()
    r = d.get_single_image_path("Giant taco on a mountain.")
    print(r)



if __name__ == "__main__":
    main()