# Write your code below: 
from contextlib import contextmanager

@contextmanager
def generic(card_type, sender, recipient):
  card = open(card_type, "r")
  new_card = open(f"context_mgr_lesson/{sender}_generic.txt", "w")
  try:
    new_card.write(f"Dear {recipient},\n{card.read()}\nSincerely,\n{sender}")
    yield new_card
  finally:
    card.close()
    new_card.close()
with generic("context_mgr_lesson/thankyou_card.txt", "Mwenda", "Amanda") as gen:
  print("Card generated!")


with open("context_mgr_lesson/Mwenda_generic.txt", "r") as f:
  print(f.read())

class Personalized:
  def __init__(self, sender, receiver):
    self.sender = sender
    self.receiver = receiver
    self.file = open(f"context_mgr_lesson/{sender}_personalized.txt", "w")

  def __enter__(self):
    self.file.write(f"Dear {self.receiver},\n")
    return self.file

  def __exit__(self, exc_type, exc_name, traceback):
    self.file.write(f"\nSincerely,\n{self.sender}")
    self.file.close()

with Personalized("John", "Michael") as f:
  f.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")

with generic("context_mgr_lesson/happy_bday.txt", "Josiah", "Remy") as b, Personalized("Josiah", "Esther") as p:
  p.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!")