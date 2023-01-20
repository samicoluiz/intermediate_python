
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    n = yield line_data[0]
    if n != None:
      line_data = n.split(",")
      name = line_data[0]
      age = int(line_data[1])
      guests[name] = age
      yield line_data[0]



def gen_table1():
  for y in range(5):
    yield ("Chicken", "Table 1", f"Seat {y+1}")


def gen_table2():
  for y in range(5):
    yield ("Beef", "Table 2", f"Seat {y+1}")


def gen_table3():
  for y in range(5):
    yield ("Fish", "Table 3", f"Seat {y+1}")


def populate_tables():
  yield from gen_table1()
  yield from gen_table2()
  yield from gen_table3()
  

def gen_seating(guests, populate):
  for g in guests:
    yield g, next(populate)

guests = {}

generator = read_guestlist("guest_list.txt")

for i in range(10):
  next(generator)

generator.send("Jane, 35")

for i in generator:
  next(generator)

print(guests)

over_21 = (guest[0] for guest in guests.items() if guest[1] > 21)
for i in over_21:
  print(i)

populate = populate_tables()
for i in gen_seating(guests, populate):
  print(i)
  