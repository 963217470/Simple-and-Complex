map_queue=[]#存储map的队列

def create_map_queue():
    map=[[0]*(300//30) for _ in range(300//30)]

    map[0]=[-1 for i in range(10)]
    map[-1]=[-1 for i in range(10)]
    for i in range(10):
        map[i][0]=-1
        map[i][-1]=-1
    map[1][1]=-1
    map[1][2]=-1
    map[1][5]=-1
    map[1][6]=-1
    map[1][8]=-1
    map[3][4]=-1
    map[6][1]=-1
    map[6][6]=-1
    map[6][7]=-1
    map[8][3]=-1
    map[8][8]=-1

    map_queue.append(map)
    for i in map:
        print(i,end='\n')