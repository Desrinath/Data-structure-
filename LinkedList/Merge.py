class ListNode():
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def merge(list1,list2):
    dummy=ListNode(-1)
    prev=dummy 

    while list1 and list2:
        if list1.val<=list2.val:
            prev.next=list1
            list1=list1.next
        else:
            prev.next=list2
            list2=list2.next
        prev=prev.next

    prev.next=list1 if list1 else list2
    return dummy.next

def print_linked_list(head):
    while head:
        print(head.val, end=" → ")
        head = head.next
    print("None")

list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

merged_list = merge(list1, list2)
print("Merged Sorted Linked List:")
print_linked_list(merged_list)
