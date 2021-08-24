import random

"""
model how a printer takes print jobs from a print queue
"""

# print queue class
class PrintQueue:
  def __init__(self):
    self.queue = []

  def add(self, item):
    self.queue.insert(0, item)

  def remove(self):
    try:
      print(self.queue.pop())
    except:
      print("queue is empty")

# print job class
class Job:
  def __init__(self):
    self.pages = random.randint(1, 10)
    self.complete = False

  def print_page(self):
    if self.pages != 0:
      print("... printing page ", self.pages)
      self.pages -= 1
    else:
      self.complete == True

  def check_complete(self):
    return self.complete

# printer class
class Printer:
  def __init__(self):
    self.current_job = None
  
  # get_job(queue): get the first job from the print queue
  # def get_job(self, queue):
    

  # print_job(job): print all the pages on the current job
  def print_job(self, queue):
    try:
      self.current_job = queue.remove()
    except:
      print("queue is empty")

    job = self.current_job

    while job.pages > 0:
      job.print_page()
    
    # print("printing completed")
    print(job.check_complete())