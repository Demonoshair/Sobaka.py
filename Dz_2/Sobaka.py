import random
class Sobaka:
    def __init__(self, name="Sharik", poroda=None):
        self.name=name
        self.poroda=poroda
        self.health=100
        self.money=100
        self.happy=100
        self.sitost=100
        self.live=True
    def play(self):
        print("Собакин поиграл")
        self.sitost-=20
        self.happy+=40
    def luza(self):
        print("Собакин повалялся в луже")
        self.health-=20
        self.happy+=40
    def ukus(self):
        print("Собакин покусал прохожего. У вас потребовали выплатить компенсацию")
        self.money-=20
        self.happy+=40
    def poroda(self):
        poroda_cube=(random.randint(1,3))
        if poroda_cube==1:
            self.poroda="Chihuahua"
            print("Ваша порода собаки: Чихуахуа")
        if poroda_cube==2:
            self.poroda="Buldog"
            print("Ваша порода собаки: Бульдог")
        if poroda_cube==3:
            self.poroda="Korgi"
            print("Ваша порода собаки: Корги")
    def sleep(self):
        print("Собакин поспал")
        self.happy+=10
        self.sitost-=30
    def eat(self):
        print("Собакин покушал")
        self.sitost+=30
    def walk(self):
        walk_cube=(random.randint(1,4))
        if walk_cube==1:
            self.play()
        if walk_cube==2:
            self.luza()
        if walk_cube==3:
            self.ukus()
        if walk_cube==4 and self.poroda=="Chihuahua":
            self.ukus()
        if walk_cube==4 and self.poroda != "Chihuahua":
            self.play()
    def alive(self):
        if self.happy<1:
            self.live=0
            print("Depression...")
            return
        if self.health<1:
            self.live=0
            print("Virus...")
            return
        if self.money < 1:
            self.live = 0
            print("Not money...")
            return
        if self.sitost<1:
            self.live=0
            print("Dog is Hunger...")
            return
    def live(self):
        live_
        self.
        print(f"Здоровье собаки: {self.heath}")
        print(f"Деньги: {self.money}")
        print(f"Счастье собаки: {self.happy}")
        print(f"Сытость собаки: {self.sitost}")