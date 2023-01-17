class School:
  def __init__(self, name, level, nstudents):
    self.name = name
    self.level = level
    self.numberOfStudents = nstudents

  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students."

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, new_number):
    self.numberOfStudents = new_number
  

class Primary(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parent_repr = super().__repr__()
    return parent_repr + f" The pickup policy is: {self.pickupPolicy}."


class Midde(School):
  def __init__(self, name, numberOfStudents):
    super().__init__(name, "middle", numberOfStudents)

class High(School):
  
  def __init__(self, name, numberOfStudents, sportsTeams):
    self.sportsTeams = sportsTeams
    super().__init__(name, "high", numberOfStudents)
    

  def get_sportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    return f"{self.sportsTeams}"

nazare = School("Colégio Marista Nossa Senhora de Nazaré", "high", 3000)
print(nazare)

peteleco = Primary("Peteleco", 200, "Pickup after 12:30")
print(peteleco)

ideal = High("Ideal", 500, ["Natação", "Futebol", "Basquete"])
print(ideal.get_sportsTeams())
print(ideal)