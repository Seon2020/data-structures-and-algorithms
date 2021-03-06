from code_challenges.stacks_and_queues.stacks_and_queues import Node, Queue

class Animal():
  def __init__(self, type:str, name:str) -> str:
    self.type = type
    self.name = name

class AnimalShelter():
    def __init__(self):
      self.cats = Queue()
      self.dogs = Queue()

    def enqueue(self, animal:str) -> str:
      if animal.type == "cat":
        self.cats.enqueue(animal)
      elif animal.type == "dog":
        self.dogs.enqueue(animal)
      else:
        raise Exception("Animal type provided is not valid")

    def dequeue(self, preference:str) -> str:
      if preference == "cat":
        return self.cats.dequeue()
      elif preference == "dog":
        return self.dogs.dequeue()
      else:
        raise Exception("Unable to successfully dequeue")


