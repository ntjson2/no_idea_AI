from dalle2 import Dalle2

dalle = Dalle2("sess-zBareHPb14XZC1RgybLnfXK1udlhV9P2ryS3vZxS")

generations = dalle.generate("portal to another dimension, digital art")

# NOTE: Generates 4 images accessed by generations[0] through generations[3]
print(generations[0].get("generation").get("image_path"))

gen_url = []
for i in range(0, 4):
    gen_url.append(generations[i].get("generation").get("image_path"))

for i in gen_url:
    print(i)