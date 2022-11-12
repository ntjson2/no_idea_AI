from dalle2 import Dalle2
import os

class Dalle():
    def __init__(self, prompt):
        self.prompt = prompt
        self.dalle = Dalle2(os.getenv("DALLE2KEY"))
        self.generations = self.dalle.generate("portal to another dimension, digital art")

    def get_single_image_path(self):
        return self.generations[0].get("generation").get("image_path")

    def __str__(self):
        return f"{self.get_single_image_path}"