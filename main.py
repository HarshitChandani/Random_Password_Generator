"""
  Program to generate a random password string.
  @author: Harshit
"""
import string
import random

set1 = string.digits
set2 = string.punctuation
set3 = string.ascii_lowercase
set4 = string.ascii_uppercase


def createRandomPassword(items_from_each_set, Remainder=None) -> str:
  ItemsFromSet1 = random.sample(set1, items_from_each_set)
  ItemsFromSet2 = random.sample(set2, items_from_each_set)
  ItemsFromSet3 = random.sample(set3, items_from_each_set)
  ItemsFromSet4 = random.sample(set4, items_from_each_set) if Remainder is None else random.sample(set4, remainder)
  PasswordLengthList = ItemsFromSet1 + ItemsFromSet2 + ItemsFromSet3 + ItemsFromSet4
  random.shuffle(PasswordLengthList)
  return "".join(PasswordLengthList)


userEnteredLength = int(input("Enter password length. "))
randomPasswordStr = str()
if userEnteredLength % 4 == 0:
  ItemsFromSet = userEnteredLength // 4
  randomPasswordStr = createRandomPassword(ItemsFromSet)
else:
  remainder = (userEnteredLength % 3)
  ItemsFromSet = (userEnteredLength - remainder) // 3
  randomPasswordStr = createRandomPassword(ItemsFromSet,remainder)

print("Password: {}".format(randomPasswordStr))