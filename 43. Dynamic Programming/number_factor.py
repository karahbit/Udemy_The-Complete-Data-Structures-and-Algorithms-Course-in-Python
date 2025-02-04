# Top-Down + Memo
def number_factor_memo(n, memo={}):
    if n in (0, 1, 2):
        return 1
    if n == 3:
        return 2
    if n in memo:
        return memo[n]
    memo[n] = number_factor_memo(n-1, memo) + number_factor_memo(n-3, memo) + \
        number_factor_memo(n-4, memo)
    return memo[n]


# Bottom-up + Tab
def number_factor_tab(n):
    tb = [1, 1, 1, 2]
    for i in range(4, n+1):
        tb.append(tb[i-1] + tb[i-3] + tb[i-4])
    return tb[n]


# Optimized Bottom-Up + Tab
def number_factor_opt(n):
    tb = [1, 1, 1, 2]
    for _ in range(4, n+1):
        fourth = tb[-1] + tb[-3] + tb[-4]
        tb[0] = tb[1]
        tb[1] = tb[2]
        tb[2] = tb[3]
        tb[3] = fourth
    return tb[3]


print(number_factor_memo(7))
print(number_factor_tab(7))
print(number_factor_opt(7))
