#두 수의 덧셈, 뺄셈, 나눗셈, 곱셈 함수를 포함하는 클래스를 만들고, 객체를 생성하시오.
class 사칙연산:
    def num1(self,a,b):
        result=a+b
        return result
    def num2(self,a,b):
        result=a-b
        return result
    def num3(self,a,b):
        result=a*b
        return result
    def num4(self,a,b):
        result=a/b
        return result
app=사칙연산()
print(app.num1(1,2))