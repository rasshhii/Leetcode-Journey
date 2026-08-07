class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        req = [0, 0, 0, 0]
        for i, p in enumerate([2, 3, 5, 7]):
            while t % p == 0:
                req[i] += 1
                t //= p
        if t > 1:
            return "-1"

        def factors(d):
            return (
                1 if d in (2, 6) else (2 if d == 4 else (3 if d == 8 else 0)),
                1 if d in (3, 6) else (2 if d == 9 else 0),
                1 if d == 5 else 0,
                1 if d == 7 else 0,
            )

        def make_suffix(c2, c3, c5, c7):
            c2, c3, c5, c7 = max(0, c2), max(0, c3), max(0, c5), max(0, c7)
            d9, c3 = divmod(c3, 2)
            d8, c2 = divmod(c2, 3)
            d6 = min(c2, c3)
            c2, c3 = c2 - d6, c3 - d6
            d4, c2 = divmod(c2, 2)
            return '2'*c2 + '3'*c3 + '4'*d4 + '5'*c5 + '6'*d6 + '7'*c7 + '8'*d8 + '9'*d9

        n = len(num)
        pref = [[0, 0, 0, 0] for _ in range(n + 1)]
        first_zero = n

        for i, ch in enumerate(num):
            if ch == '0':
                first_zero = i
                break
            f = factors(int(ch))
            for k in range(4):
                pref[i + 1][k] = pref[i][k] + f[k]

        if first_zero == n and all(pref[n][k] >= req[k] for k in range(4)):
            return num

        for i in range(min(n - 1, first_zero), -1, -1):
            cur = [max(0, req[k] - pref[i][k]) for k in range(4)]
            start = int(num[i]) + 1 if i < first_zero else 1

            for d in range(start, 10):
                f = factors(d)
                rem = [max(0, cur[k] - f[k]) for k in range(4)]
                suf = make_suffix(*rem)
                if len(suf) <= n - 1 - i:
                    return num[:i] + str(d) + '1' * (n - 1 - i - len(suf)) + suf

        min_suf = make_suffix(*req)
        target_len = max(n + 1, len(min_suf))
        return '1' * (target_len - len(min_suf)) + min_suf