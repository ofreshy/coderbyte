def adder(arr):
    newarr = ''
    for s in arr:
        newarr += s if s.isdigit() else '-'
    return sum([int(s) for s in newarr.split('-') if s ])


print adder([])
print adder("88Hello 3World!")


