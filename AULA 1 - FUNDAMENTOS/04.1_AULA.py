import random
import emoji

num = random.random()
print(num)

num2 = random.randint(1, 10)
print(num2)

print("")
print("==================")
print("")

print(emoji.emojize("Ola, mundo 😎"))
print(emoji.emojize("Ola, mundo :smiling_face_with_sunglasses:",  language='alias'))
