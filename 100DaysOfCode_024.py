def find_common_chr(strs):
    pre = []
    for c in zip(*strs):
        if len(set(c)) == 1:
            pre.append(c[0])
        else:
            break
    return ''.join(pre)


print(find_common_chr(['pascal', 'paypal', 'panasonic']))
