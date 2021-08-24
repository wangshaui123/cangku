from threading import Thread
import time

class mianbao(Thread):
    chushou= ""
    yiyou = 0  #已买个数
    qian = 3000  #客户的钱

    def run(self) -> None:
        while True:
            self.yiyou += 1
            self.qian -= 3
            print(self.chushou,"买了",self.yiyou,"个面包")
            if self.yiyou == 500:
                print("买了",self.yiyou,"个面包，篮子满了，稍等一下")
                time.sleep(2)
            elif self.qian == 0:
                print("钱花完了")
                break

p1 = mianbao()
p2 = mianbao()
p3 = mianbao()
p1.chushou="孙建国"
p2.chushou="高振伟"
p3.chushou="王帅"
p1.start()
p2.start()
p3.start()