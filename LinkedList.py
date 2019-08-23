class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def add(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        curr_node=self.head
        while curr_node.next!=None:
            curr_node=curr_node.next
        curr_node.next=newnode
    def print_list(self):
        curr_node=self.head
        if curr_node is None:
            print('no list exist')
        while curr_node!=None:
            print(curr_node.data)
            curr_node=curr_node.next
    def prepend(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def insert_after_node(self,prevnode,data):
        if prevnode is None:
            print('previous node is none')
            return
        newnode=Node(data)
        newnode.next=prevnode.next
        prevnode.next=newnode
    def delete_node(self,key):
        curr_node=self.head
        if curr_node!=None and curr_node.data==key:
            self.head=curr_node.next
            curr_node=None
            return
        prev_node=None
        while curr_node and curr_node.data!=key:
            prev_node=curr_node
            curr_node=curr_node.next
        if curr_node is None:
            return
        prev_node.next=curr_node.next
        curr_node=None
    def delete_node_by_pos(self,pos):
        curr_node=self.head
        if curr_node and pos==0:
            self.head=curr_node.next
            curr_node=None
            return
        prev_node=None
        count=0
        while curr_node and count!=pos:
            prev_node=curr_node
            curr_node=curr_node.next
            count+=1
        if curr_node is None:
            print("you position doesen't belong to list ")
            return
        prev_node.next=curr_node.next
        curr_node=None
llist=LinkedList()
llist.add('abhishek')
llist.add('kumar')
llist.add('gupta')
llist.delete_node_by_pos(4)
llist.print_list()


