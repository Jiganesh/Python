def split_num(num):
    str_num = str(num)
    str_len = len(str(num))
    str_len_by = str_len//2

    if str_len & 1 == False:
        return str_num[:str_len_by], "", str_num[str_len_by:]
    else:
        return str_num[:str_len_by], str_num[str_len_by], str_num[str_len_by+1:]


'''

1221 will return '12', ' ' ,'21'
12340 will return '12',  '3',  '40'

'''


def next_palindrome(x):
    if x < 9:
        return x+1
    if x < 11:
        return 11
    num = x
    left, mid, right = split_num(num)
    len_num = len(str(num))

    if num == 10**len_num - 1:
        return num+2
    elif mid == "":
        if not int(left[::-1]) > int(right):
            left = str(int(left)+1)
        right = left[::-1]
    else:
        if not int(left[::-1]) > int(right):
            left = str(int(left+mid)+1)
            left, mid = left[:-1], left[-1]
        right = left[::-1]

    return int(left+mid+right)


print(next_palindrome(734546724582))
