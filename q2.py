def func1(*args):
    print("printing values:")
    for arg in args:
        print(arg)

func1(20,40,60)
func1("hello",80)