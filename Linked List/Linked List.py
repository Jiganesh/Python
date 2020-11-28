''' Traversal, Appending, Prepend, Insert_after_Node, Delete, Reverse, Find_Middle, Detecting Loop, Making loop, Removing loop'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None

    def view(self, node=1000):
        if self.head is None:
            print("List is empty")
        else:
            last_node = self.head
            count = 0
            while last_node != None and count < node:
                print(last_node.data, end="----->")
                last_node = last_node.next
                count += 1
            print()
        print()

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next

            last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        new_node = Node(data)
        cur_node = self.head
        while cur_node.data != prev_node:
            cur_node = cur_node.next

        new_node.next = cur_node.next
        cur_node.next = new_node

    def delete(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def reverse_iterative(self):
        cur_node = self.head
        prev_node = None
        while cur_node != None:
            next_node = cur_node.next
            cur_node.next = prev_node

            prev_node = cur_node
            cur_node = next_node

        self.head = prev_node

    def reverse_recursive(self):

        def reverse_recursive(cur_node, prev_node):
            if not cur_node:
                return prev_node
            next_node = cur_node.next
            cur_node.next = prev_node

            prev_node = cur_node
            cur_node = next_node

            return reverse_recursive(cur_node, prev_node)
        self.head = reverse_recursive(cur_node=self.head, prev_node=None)

    def find_middle(self):
        fast = slow = self.head
        while slow and fast and fast.next:
            slow, fast = slow.next, fast.next.next

        return slow.data

    def detect_loop(self):
        fast = slow = self.head
        while slow and fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return "Loop detected"
        return "No Loop detected"

    def make_loop(self, k):
        temp = self.head
        count = 0
        while count != k:
            temp = temp.next
            count += 1
        joint = temp
        while temp.next != None:
            temp = temp.next
        temp.next = joint

    def remove_loop(self, node):
        ptr1 = self.head
        while True:
            ptr2 = node
            while ptr2.next != node and ptr2.next != ptr1:
                ptr2 = ptr2.next
            if ptr2.next != ptr1:
                break
            ptr1 = ptr1.next
        ptr2.next = None


List = Linkedlist()


List.append("B")
List.append("C")
List.append("G")
List.append("A")
List.append("Z")
List.view()

print("Appending : B, C, G ")
List.view()

List.prepend("A")
print("Prepending : A ")
List.view()

List.insert_after_node("G", "D")
print("Inserting after node : D")
List.view()

List.append("X")
List.append("Y")
print("Appending : X, Y ")
List.view()

List.delete("X")
List.delete("Y")
print("Deleting : X, Y")
List.view()


List.reverse_iterative()
print("Reversing Iterative Approach : ")
List.view()

List.reverse_recursive()
print("Reversing Recursive Approach : ")
List.view()


print("Middle element in LinkedList is : ", List.find_middle(), end="\n\n")

print(List.detect_loop(), end="\n")
List.view()

List.make_loop(2)

print(List.detect_loop())
List.view(7)

List.remove_loop(List.head.next.next)

print(List.detect_loop())
List.view()
