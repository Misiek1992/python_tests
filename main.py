import ctypes

if __name__ == '__main__':
    mydll = ctypes.cdll.LoadLibrary("FibLib.dll")
    fib= mydll.fibonacci_init(1, 1)

    for i in range(0,10):
        mydll.fibonacci_index()
        print(mydll.fibonacci_current())
        mydll.fibonacci_next()


