from multiprocessing import Pipe, Process
from multiprocessing.connection import PipeConnection
import random


def proceso1(left1: PipeConnection):
    for _ in range(10):
        octeto1 = random.randint(0,255)
        octeto2 = random.randint(0,255)
        octeto3 = random.randint(0,255)
        octeto4 = random.randint(0,255)
        ip = f"{octeto1}.{octeto2}.{octeto3}.{octeto4}"
        left1.send(ip)
    

def proceso2(right1: PipeConnection, left2: PipeConnection):
    for _ in range(10):
        ip = right1.recv()
        octeto1 = ip.split(".")[0]

        if int(octeto1) <= 223:
            left2.send(ip)

    left2.send(None)

def proceso3(right2: PipeConnection):
    ip = right2.recv()
    while ip is not None:
        octeto1 = int(ip.split(".")[0])
        if octeto1 <= 127:
            print(ip, "Clase A")
        elif octeto1 <=191:
            print(ip, "Clase B")
        else:
            print(ip, "Clase C")
        ip = right2.recv()

if __name__ == "__main__":
    left1, right1 = Pipe() #comunica el proceso1 con el proceso2
    left2, right2 = Pipe() #comunica el proceso2 con el proceso3

    p1 = Process(target=proceso1, args=(left1,))
    p2 = Process(target=proceso2, args=(right1, left2))
    p3 = Process(target=proceso3, args=(right2,))
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
