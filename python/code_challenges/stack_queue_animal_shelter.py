from data_structures.queue import Queue


class AnimalShelter:

    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, animal):
        if animal.type == "cat":
            self.cat_queue.enqueue(animal)
        elif animal.type == "dog":
            self.dog_queue.enqueue(animal)

    def dequeue(self, pref):
        if pref == "cat":
            new_pet = self.cat_queue.dequeue()
        elif pref == "dog":
            new_pet = self.dog_queue.dequeue()
        else:
            return None

        return new_pet

class Dog:

    def __init__(self):
        self.type = "dog"



class Cat:

    def __init__(self):
        self.type = "cat"
