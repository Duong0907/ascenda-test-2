def merge_two_list(l1, l2):
    temp = l1 + l2
    result = []
    for e in temp:
        if e not in result:
            result.append(e)

    return result

def merge_two_value(v1, v2):
    if v1 == None:
        return v2
    else:
        return v1