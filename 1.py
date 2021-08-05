class Father(object):
    def __init__(self):
        pass
    def sayHi(self, word1):
        print(word1)

class Son(Father):
    def __init__(self):
        pass
    def sayHello(self,word2):
        super(Son, self).sayHi(word2)
        #print("Hello")

father = Father()
son = Son()

print(father.sayHi("Hi"))
print(son.sayHi("Hello"))