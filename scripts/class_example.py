class A:
    def f(self): print("A.f")

class B(A):
    def f(self):
        print("B 前")
        super().f()    # 不是「同上」，而是去呼叫 A.f
        print("B 後")
class C(B):
    def f(self):
        print("C 前")
        super().f()    # 動態地，下一層是 B.f，再往下又會是 A.f
        print("C 後")
if __name__ == "__main__":
    c = C()
    c.f()
    print("=================================")
    b = B()
    b.f()
    print("=================================")
    a = A()
    a.f()
    print("=================================")