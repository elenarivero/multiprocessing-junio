from multiprocessing import Process, Queue

def productor(queue: Queue):
    for i in range(100):
        print("añadiendo: ", i)
        queue.put(i)
    queue.put(None)

def consumidor(queue: Queue):
    objeto = queue.get()
    while objeto is not None:
        print("obteniendo: ", objeto)
        objeto = queue.get()


if __name__ =="__main__":
    queue = Queue()
    p1 = Process(target=productor, args=(queue,))
    p2 = Process(target=consumidor, args=(queue,))
    
    p1.start()
    p2.start()