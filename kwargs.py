def sum_kwargs(**kwargs):
    return sum(kwargs.values())
add = sum_kwargs(a=4, b=7, c=10, d=17)
print(add)
    