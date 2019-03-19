class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class LL():
    def __init__(self):
        self.head = None

    #There is a lot of boilerplaer here
    #Need to abstract it out. Later
    def add(self, node):
        if self.head:
            cur = self.head
            while True:
                if cur.next == None:
                    cur.next = node
                    break
                else:
                    cur = cur.next
        else:
            self.head = node

    def print_list(self):
        cur = self.head
        while True:
            print(cur.val)
            if cur.next:
                cur = cur.next
            else:
                break

    def remove(self, val):
        #This has fun edge cases in here.
        #Mostly, removing the head, middle and end
        if val == self.head.val:
            self.head = self.head.next
        else:
            cur = self.head
            while True:
                if cur.next == None:
                    print("Can't find {}".format(val))
                    break
                elif cur.next.val == val:
                    cur.next = cur.next.next
                    break
                else:
                    cur = cur.next

linked = LL()
n1 = Node(4)
n2 = Node(5)
n3 = Node(6)
n4 = Node(7)
n5 = Node(9)

linked.add(n1)
linked.add(n2)
linked.add(n3)
linked.add(n4)
linked.add(n5)

linked.print_list()

print("-----")
linked.remove(4)
linked.print_list()

print("-----")
linked.remove(6)
linked.print_list()


print("-----")
linked.remove(8)
linked.print_list()

