from code_challenges.stacks_and_queues.stacks_and_queues import Node, Stack

class PseudoQueue():
  def __init__(self):
    self.input =  Stack()
    self.output = Stack()

  def enqueue(self, value):
    self.input.push(value)

  def dequeue(self):
# Empty the input stack into output stack
    if self.input:
      try:
        value = self.input.pop()
        self.output.push(value)
      except Exception: 
        return("Unable to successfully dequeue")
    
# Return top of the output stack
    return self.output.pop()
      
