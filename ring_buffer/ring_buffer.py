from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # when full oldest element is overwritten with newest element, kind of like LRU cache
        # ['a', 'b', 'c', 'd', 'e'] - when not full just add to tail and change current to oldest or head
        # ['f', 'b', 'c', 'd', 'e'] - when full place new value where current is
        # ['f', 'g', 'h', 'i', 'e'] - after f is placed you will want to move current to next
        if self.current == None:
            self.current = self.storage.head
        if len(self.storage) == self.capacity:
            if self.current == self.storage.head:  # edge case for head
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.current.next

            elif self.current == self.storage.tail:  # edge case for tail
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.current = self.storage.head

            else:
                # self.current should start out at head here
                temp = self.current
                self.storage.delete(self.current)
                self.current = temp.next
                self.current.insert_before(item)
                self.storage.length += 1
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        temp = self.storage.head
        while temp.next != None:
            list_buffer_contents.append(temp.value)
            temp = temp.next
        # while loop wont get tail, this will
        list_buffer_contents.append(temp.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
