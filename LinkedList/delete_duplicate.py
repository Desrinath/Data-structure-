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

def deleteDuplicates(head):
    current = head

    while current and current.next:
        if current.val == current.next.val:

            current.next = current.next.next
        else:

            current = current.next

    return head

def print_linked_list(head):
    while head:
        print(head.val, end=" → ")
        head = head.next
    print("None")


head = create_linked_list([1, 1, 2, 3, 3])
new_head = deleteDuplicates(head)

print("After removing duplicates:")
print_linked_list(new_head)
