#사용자의 이름,나이,연락처를 입력 받아서
#이름은 ~이며 나이는 연락처는~~입니다.

class Info:
    def __init__(self,name,age,ph):
        self.name=name
        self.age=age
        self.ph=ph
    def a(self):
        print('이름은',self.name,'이며, 나이는',self.age,', 그리고 연락처는',self.ph,'입니다.')

my_info=Info('김진수',27,'010-4559-1866')
my_info.a()