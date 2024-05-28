from multiprocessing import Pipe, Process
from multiprocessing.connection import PipeConnection

def process1(left:PipeConnection):
    for i in range(100):
        print("Enviando:",i)
        left.send(i)
    left.send(None)
    left.close()


def process2(right:PipeConnection):
    objeto = right.recv()
    while objeto is not None:
        print("recibiendo",objeto)
        objeto = right.recv()
    right.close()


if __name__ == "__main__":
    left, right = Pipe()
    p1 = Process(target=process1, args=(left,))
    p2 = Process(target=process2, args=(right,))

    p1.start()
    p2.start()
