from dalle2 import Dalle2
import os

class Dalle():
    def __init__(self):
        self.d = Dalle2(os.getenv("DALLE2KEY"))

    def get_single_image_path(self, prompt):
        d = self.d
        g = d.generate(str(prompt))

        try:
            return g[0].get("generation").get("image_path")
        except:
            print(f"Generating image has failed.\nReason: {g[0]}\nStatus Code: {g[1]}\nRetrying...")
            self.get_single_image_path(prompt)


def main():
    d = Dalle()
    r = d.get_single_image_path("Giant taco on a mountain.")
    print(r)


if __name__ == "__main__":
    main()