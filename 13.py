import numpy as np
def test():
    a = np.arange(15).reshape((3,5))
    b = np.ones((3,5))*5
    #a = np.array([[1,2,3]],dtype=np.int32)
    #a = np.linspace(0,0,10)
    #a = np.zeros((1,3))
    #a = np.diag([1,2,3])*4
    # b = a[0:2,1::2]
    # print(a.dtype)
    print(a)
    print(b)
    c= np.reciprocal(b)
    print(c)
    print(a.sum(axis=0))
    # print(a.ndim)
    # print(a.shape)
    # print(a.size)
    # print(a.itemsize)
def main():
    test()
if __name__ == '__main__':
     main()