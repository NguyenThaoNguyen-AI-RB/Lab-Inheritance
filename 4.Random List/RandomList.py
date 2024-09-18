import random
class RandomList(list):
    def get_random_element(self):
        if len(self) == 0:
            print("Cannot get a random element from an empty list.")
            return
        index = random.randint(0, len(self) - 1)
        return self.pop(index)



