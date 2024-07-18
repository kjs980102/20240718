#게임 캐릭터 만들기 게임 캐릭터 생성 클래스는 아이디, 성별, 직업 정보를 갖으며 기본 공격에 함수를 갖는다.
#기본 공격 함수는 사용시 '공격!' 문자열을 화면에 출력한다.

class Game:
    def __init__(self,id,sex,job):
        self.my_id = id
        self.my_sex = sex
        self.my_job = job
    def atk(self,상대방_id):
        print(self.my_id,'가',상대방_id,'를 공격!')

my=Game('kjs980102','남자','백수')
my.atk('몬스터')