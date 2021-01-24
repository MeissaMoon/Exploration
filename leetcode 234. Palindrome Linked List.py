Input: 1->2
Output: false


# 풀이 1 리스트 변환
def isPalindrome(self, head: ListNode) -> bool:
    # 데크 자료형 선언
    q: Deque = collections.Deque

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True