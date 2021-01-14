import pytest
from code_challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter, Animal

def test_animal_enqueue_one():
  animal_instance = Animal("cat", "Fluffers")
  shelter_instance = AnimalShelter()
  shelter_instance.enqueue(animal_instance)
  actual = shelter_instance.cats.peek()
  expected = animal_instance
  assert actual == expected

def test_animal_enqueue_several():
  animal_instance_one = Animal("dog", "Doggy")
  animal_instance_two = Animal("cat", "Kitty")
  shelter_instance = AnimalShelter()
  shelter_instance.enqueue(animal_instance_one)
  shelter_instance.enqueue(animal_instance_two)
  actual = shelter_instance.cats.peek()
  expected = animal_instance_two
  assert actual == expected

def test_animal_enqueue_invalid_type():
  animal_instance = Animal("cow", "Moo")
  shelter_instance = AnimalShelter()
  with pytest.raises(Exception):
    shelter.enqueue(animal_instance)

def test_animal_dequeue_one():
  animal_instance = Animal("cat", "Carl")
  shelter_instance = AnimalShelter()
  shelter_instance.enqueue(animal_instance)
  actual = shelter_instance.dequeue("cat")
  expected = animal_instance
  assert actual == expected

def test_animal_dequeue_several():
  animal_instance_one = Animal("dog", "Trump")
  animal_instance_two = Animal("dog", "Ivanka")
  shelter_instance = AnimalShelter()
  shelter_instance.enqueue(animal_instance_one)
  shelter_instance.enqueue(animal_instance_two)
  shelter_instance.dequeue("dog")
  actual = shelter_instance.dequeue("dog")
  expected = animal_instance_two
  assert actual == expected

def test_animal_dequeue_several_types():
  animal_instance_one = Animal("cat", "Meow")
  animal_instance_two = Animal("dog", "Bark")
  shelter_instance = AnimalShelter()
  shelter_instance.enqueue(animal_instance_one)
  shelter_instance.enqueue(animal_instance_two)
  shelter_instance.dequeue("cat")
  actual = shelter_instance.dequeue("dog")
  expected = animal_instance_two
  assert actual == expected

