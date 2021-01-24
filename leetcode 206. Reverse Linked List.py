    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None     # node가 None이 되고 뒤집힌 prev가 첫번째 값 head가 될때 종료

        while node:
            next, node.next = node.next, prev   # node의 다음값과 이전 값을 비교하면서 뒤집는다?
            prev, node = node, next

        return prev