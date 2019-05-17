from contracts import contract


@contract(x='int,>=0')
def f(x):
    pass


@contract(returns='int,>=0')
def f2(x):
    return x


f(-2)
f2(-1)
