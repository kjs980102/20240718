class Home:
    def __init__(self, 위치, 평수, 종류, 가격, 년도):
        home=[]
        self.home_a = 위치
        self.home_b = 평수
        self.home_c = 종류
        self.home_d = 가격
        self.home_e = 년도

    def object(self):
        print(self.home_a,self.home_b,self.home_c,self.home_d,self.home_e)
my_home=Home("서울",'27억',"아파트","1억원",'2009년도')
my_home.object()