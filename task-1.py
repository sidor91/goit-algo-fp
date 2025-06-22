class Node:
  def __init__(self, key):
    self.value = key
    self.next = None


class Linked_list:
  def __init__(self):
    self.head = None
    self.tail = None

  def insert(self, key):
    new_node = Node(key)
    if not self.head:
      self.head = self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node

  def reverse(self):
    prev = None
    current = self.head

    while current:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node

    self.head = prev



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  ll = Linked_list()
  ll.insert(10)
  ll.insert(20)
  ll.insert(30)

  ll.reverse()

  current = ll.head
  while current:
    print(current.value, end=" -> ")
    current = current.next