#문자 메시지 길이 판별 클래스
#문자 메시지의 길이에 따라 부과되는 요금은,클래스를 생성할 때 속성 정보로 갖게 된다.
#요금이 부과될 문자 메시지의 길이를 정할 수 있도록 설정하시오.(속성 정보)
#이 때 사용자로부터 문자메시지를 입력 받아서 문자 요금을 반환하는 코드를 작성하시오.

# class Mms:
#     def __init__(self,mms):
#         self.mms=mms
#     def price(self):
#         if len(self.mms)>20:
#             print('문자 요금은 100원입니다.')
#             result=100
#         else :
#             print('문자 요금은 50원입니다.')
#             result=50
#         return result
# # my_mms=Mms("")
# # my_mms.price()
#
# class Mms:
#     def __init__(self,mms,len,p1,p2):
#         self.mms=mms
#         self.len=len
#         self.p1=p1
#         self.p2=p2
#     def price(self):
#         if len(self.mms)>=self.len:
#             print("문자 요금은",self.p1,"입니다.")
#             result=self.p1
#         elif len(self.mms)<self.len:
#             print("문자 요금은",self.p2,"입니다.")
#             result=self.p2
#         return result
# my_mms=Mms("날씨 왜이리 우중충하지",20,100,50)
#
# my_mms.price()

class Mms:
    def __init__(self,len,p1,p2):
        self.len=len
        self.p1=p1
        self.p2=p2
    def price(self,x):
        if len(x)>=self.len:
            print("문자 요금은",self.p1,"입니다.")
            result=self.p1
        elif len(x)<self.len:
            print("문자 요금은",self.p2,"입니다.")
            result=self.p2
        return result

message=input('문자를 입력하세요.:')
my_mms=Mms(10,100,50)

my_mms.price(message)