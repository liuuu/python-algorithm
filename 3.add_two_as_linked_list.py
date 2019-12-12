class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumber(self, x, y, h):
        if x or y:
            if not x:
                x = Node(0)
            if not y:
                y = Node(0)
            sum = (x.val + y.val + h) % 10
            carry = (x .val + y.val + h) // 10
            node = Node(sum)
            node.next = self.addTwoNumber(x.next, y.next, carry)
            return node
        else:
            return

    def addTwoNumber1(self, a, b, c):
        x = a
        y = b
        ret = current = None
        carry = 0
        while x or y:
            if not x:
                x = Node(0)
            if not y:
                y = Node(0)

            sum = (x.val + y.val + carry) % 10
            carry = (x.val + y.val + carry) // 10
            if current:
                current.next = Node(sum)
                current = current.next
            else:
                current = Node(sum)
                ret = current
            x = x.next
            y = y.next

        return ret


l1 = Node(1)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

# answer = Solution().addTwoNumber(l1, l2, 0)
answer = Solution().addTwoNumber1(l1, l2, 0)


while answer:
    print('answet.val', answer.val)
    answer = answer.next
