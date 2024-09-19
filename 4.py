def func(a,b,c=4,d=5):
    print(a,b,c,d)
    return (a,b,c,d)
func(2,*(6,7))

#2675