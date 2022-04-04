from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]

  def hash(self, key):
    hash_code = sum(key.encode())
    return hash_code

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    hash_code = self.hash(key)
    arr_index = self.compress(hash_code)
    list_at_arr = self.array[arr_index]
    payload = Node([key, value])
    list_at_arr.insert(payload)

    for i in list_at_arr:
      if i[0] == key:
        i[1] = value
      else:
        return None

  def retrieve(self, key):
    hash_code = self.hash(key)
    arr_index = self.compress(hash_code)
    list_at_index = self.array[arr_index]

    for item in list_at_index:
      if item[0] == key:
        return item[1]
      else:
        return None
    
    if arr_index != None:
      if payload[0] == key:
        return payload[1]
      else:
        return None

hash_map = HashMap(15)
blossom = HashMap(len(flower_definitions))
for i in flower_definitions:
  blossom.assign(i[0], i[1])

print(blossom.retrieve('daisy'))
