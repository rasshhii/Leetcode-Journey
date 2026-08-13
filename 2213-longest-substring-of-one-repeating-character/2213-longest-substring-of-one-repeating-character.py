class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree = [None] * (4 * n)

        def merge(left, right):
            if not left: return right
            if not right: return left
            lc, lrc, llen, lp, ls, lb = left
            rlc, rc, rlen, rp, rs, rb = right
            
            length = llen + rlen
            prefix = llen + rp if lrc == rlc and lp == llen else lp
            suffix = rlen + ls if lrc == rlc and rs == rlen else rs
            best = max(lb, rb, ls + rp if lrc == rlc else 0)
            
            return [lc, rc, length, prefix, suffix, best]

        def build(node, start, end):
            if start == end:
                tree[node] = [s[start], s[start], 1, 1, 1, 1]
                return
            mid = (start + end) // 2
            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, start, end, index, char):
            if start == end:
                tree[node] = [char, char, 1, 1, 1, 1]
                return
            mid = (start + end) // 2
            if index <= mid:
                update(node * 2, start, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, end, index, char)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)
        ans = []
        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            ans.append(tree[1][5])
            
        return ans