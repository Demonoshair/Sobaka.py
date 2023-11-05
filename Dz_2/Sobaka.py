import random
class Sobaka:
    def __init__(self, name="Sharik", porod=None):
        self.name=name
        self.porod=porod
        self.health=100
        self.money=200
        self.happy=100
        self.sitost=100
        self.live=True
    def play(self):
        print("Собакин поиграл")
        self.sitost-=30
        self.happy+=20
    def luza(self):
        print("Собакин повалялся в луже")
        self.health-=30
        self.happy+=40
    def ukus(self):
        print("Собакин покусал прохожего. У вас потребовали выплатить компенсацию")
        self.money-=20
        self.happy-=40
    def poroda(self):
        self.poroda_cube=(random.randint(1,3))
        if self.poroda_cube==1:
            self.porod="Chihuahua"
            print("Ваша порода собаки: Чихуахуа")
        if self.poroda_cube==2:
            self.porod="Buldog"
            print("Ваша порода собаки: Бульдог")
        if self.poroda_cube==3:
            self.porod="Korgi"
            print("Ваша порода собаки: Корги")
    def sleep(self):
        print("Собакин поспал")
        self.happy+=10
        self.health+=20
    def eat(self):
        print("Собакин покушал")
        self.sitost+=60
        self.money-=15
    def walk(self):
        self.walk_cube=(random.randint(1,4))
        if self.walk_cube==1:
            self.play()
        if self.walk_cube==2:
            self.luza()
        if self.walk_cube==3:
            self.ukus()
        if self.walk_cube==4 and self.porod=="Chihuahua":
            self.ukus()
        if self.walk_cube==4 and self.porod != "Chihuahua":
            self.play()
    def alive(self):
        if self.happy<1:
            self.live=False
            print("Depression...")
            return
        if self.health<1:
            self.live=False
            print("Virus...")
            return
        if self.money < 1:
            self.live=False
            print("Not money...")
            return
        if self.sitost<1:
            self.live=False
            print("Dog is Hunger...")
            return
    def life(self,day):
        if self.live==False:
            self.alive()
            return
        if self.porod==None:
            self.poroda()
        day = "day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        self.live_cube=random.randint(1,3)
        if self.live_cube==1:
            self.sleep()
        if self.live_cube==2:
            self.walk()
        if self.live_cube==3:
            self.eat()

        if self.happy>100:
            self.happy=100
        if self.sitost>100:
            self.sitost=100
        if self.health>100:
            self.health=100
        print(f"Здоровье собаки: {self.health}")
        print(f"Деньги: {self.money}")
        print(f"Счастье собаки: {self.happy}")
        print(f"Сытость собаки: {self.sitost}")
        self.alive()

dogus=Sobaka()

for day in range (1,22):
    if dogus.live==False:
        break
    else:
        dogus.life(day)
input()