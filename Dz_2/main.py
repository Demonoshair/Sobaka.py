import random

class Child:
    def __init__(self, name=None, age=1, day=1, reputation=0.7, harak=None):
        self.day=day
        self.age=age
        self.name=name
        self.health=100
        self.stamina=70
        self.food=True
        self.happy=100
        self.money=100
        self.reputation=reputation                 #Это уверенность в себе
        self.intelekt=50
        self.harak=harak
        self.alive=True
        self.text=None
    def shkola(self):
        self.shkola_cube=random.randint(1,3)
        if self.shkola_cube==1:
            print("Вы решили прогулять школу")
            self.intelekt-=20
            self.happy+=random.randint(10,25)
        else:
            print("Вы пришли в школу")
            self.urok_cube=random.randint(1,3)
            if self.urok_cube==1 and self.harak==False:
                print("Ты сидишь на уроке, и занудничаешь, всех это бесит")
                self.reputation-=0.3
                self.intelekt+=20
            elif self.urok_cube==1 and self.harak==True:
                print("Ты сидишь на уроке и не слушаешь, учитель тебя наказывает")
                self.intelekt += 5
                self.happy-=5
            else:
                print("Ты сидишь на уроке и слушаешь")
                self.intelekt+=20
    def park(self):
        self.park_cube=random.randint(1,4)
        if self.park_cube==1:
            print("Вы пошли на атракционы")
            self.money-=20
            self.happy+=30
            self.stamina-=20
            self.reputation += 0.2
        if self.park_cube==2:
            print("Вы поиграли на площадке")
            self.plosh_cube=random.randint(1,3)
            if self.plosh_cube==1:
                print("На вас напали хулиганы")
                self.happy-=40
                self.health-=20
                self.reputation-=0.5
                self.stamina-=30
                self.money-=30
            else:
                print("Вам было очень весело)")
                self.happy+=20
                self.food-=10
                self.stamina-=20
                self.reputation += 0.2
        if self.park_cube==3:
            print("Вы упали в лужу, у расплакались")
            self.health-=10
            self.happy-=20
        if self.park_cube==4:
            print("Вы на асфальте нашли 20 гривень")
            self.grn_cube=random.randint(1,3)
            if self.grn_cube==1:
                print("Мама сказала не поднимать деньги, так как могут сглазить")
                self.happy-=random.randint(0,10)
            else:
                print("Вы подняли их")
                self.money+=20
                self.morozhka_cube=random.randint(1,2)
                if self.morozhka_cube==1:
                    print("Вы пошли купили на эти деньги мороженое")
                    self.money-=20
                    self.happy+=30
    def life(self):
        if self.alive==False:
            return
        self.text=f"Day{self.day}, Year {self.age} for {self.name}"
        print(f"{self.text:=^50}")
        self.day+=1
        if self.day==30:
            self.day=1
            self.age+=1
        self.rand_cube=random.randint(1,4)
        if self.rand_cube==1:
            print("Родители ушли на работу")
            self.happy-=20
            self.money+=60
        elif self.rand_cube==2:
            print("Вы решили пойти в парк")
            self.park()
        elif self.rand_cube==3:
            print("Вам сказали ложиться спать")
            self.stamina+=40
        elif self.rand_cube==4:
            print("Вам сказали идти в школу")
            self.shkola()
        if self.health<30 and self.money>30:
            self.money-=30
            self.health=70
        if self.money>10:
            self.money-=10
            self.food=True
        else:
            self.food=False
        if self.health>100:
            self.health=100
        if self.happy>100:
            self.happy=100
        if self.intelekt>100:
            self.intelekt=100
        if self.stamina>100:
            self.stamina=100
        if self.reputation>1:
            self.reputation=1
        self.reputation=round(self.reputation,1)
        print(f"Health: {self.health}")
        print(f"Money: {self.money}")
        print(f"Stamina: {self.stamina}")
        print(f"Happy: {self.happy}")
        print(f"Intelekt: {self.intelekt}")
        print(f"Reputation: {self.reputation}")
        if self.health<1:
            self.alive=False
            print("Virus...")
        if self.happy<1:
            self.alive=False
            print("Depression...")
        if self.stamina<1:
            self.alive=False
            print("Pereutomlenie...")
        if self.intelekt<1:
            self.alive=False
            print("Tupost...")
        if self.reputation<0.1:
            self.alive=False
            print("Bulling...")
        if self.food==False:
            self.alive=False
            print("Golod...")

class Uchitel:
    def __init__(self, zlost=0, monep):
        self.zlost=zlost
        self.monep=monep
    def live(self):
        self.zlost+=random(1,3)
        if self.zlost>10:
            print("Учитель заставляет сдать на новые шторы")
            self.shtori()
    def shtori(self):
        self.zlost=0
        if self.monep
#Обьект класса Ребёнок
mihail=Child(name="Mihail")
for day in range(1,366):
    if mihail.alive==False:
        break
    mihail.life()