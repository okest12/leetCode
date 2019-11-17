class listNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def add_two_number(s1, s2):
    l1 = create_list_node(s1)
    l2 = create_list_node(s2)
    result = dummy = listNode(-1)
    carry = 0
    while l1 or l2 or carry:
        sum = carry
        if l1:
            sum += l1.value
            l1 = l1.next
        if l2:
            sum += l2.value
            l2 = l2.next
        if sum >= 10:
            carry = 1
            sum -= 10
        else:
            carry = 0
        dummy.next = listNode(sum)
        dummy = dummy.next
    return result.next


def print_list_node(l):
    s = ''
    while l:
        s = str(l.value) + s
        l = l.next
    print(s)


def create_list_node(s):
    result = dummy = listNode(-1)
    for i in range(len(s), 0, -1):
        dummy.next = listNode(int(s[i - 1]))
        dummy = dummy.next
    return result.next


l3 = add_two_number("12345", "67890")
print_list_node(l3)
