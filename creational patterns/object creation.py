class objectManager: 
    pass

if __name__ == '__main__':
    a = objectManager()
    b = objectManager()

    print(id(a) == id(b))
    
    print(a, '\n')
    print(b, '\n')