from pprint import pprint

class My_chess():
    def __init__(self):
        #empty bord
        self.bord = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
        #white pieces
        self.king0 = 6.0
        self.quin0 = 5.0
        self.rook0 = 4.0
        self.bishop0 = 3.0
        self.knight0 = 2.0
        self.pone0 = 1.0

        # black pieces
        self.king1 = 6.1
        self.quin1 = 5.1
        self.rook1 = 4.1
        self.bishop1 = 3.1
        self.knight1 = 2.1
        self.pone1 = 1.1
    #sets the bord
    def start(self):
        self.bord = [[4.1, 2.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                     [4.0, 3.0, 2.0, 5.0, 6.0, 2.0, 3.0, 4.0]]
        pprint(self.bord)
    #valid moves
    def v_moves(self,r,c):
        move = self.bord[r][c]
        #moves for pone
        if move == 1.1:
            flag = False
            v_moves = []
            for i in range(8):
                if r == 1 and c == i+1:
                    v_moves = [(r+2,c+1),(r+3,c+1)]
                    print(v_moves)
                    print(i)
                    flag = True
            if flag == False:
                v_moves = [(r + 2, c + 1)]
                print(v_moves)
        #rook moves
        elif move == 4.1:
            Lr = [(r+1,i+1) for i in range(8)]
            Lc = [(i+1,c+1) for i in range(8)]
            R = (r+1, c+1)
            Lc.remove(R)
            Lr.remove(R)
            L = Lr+Lc

            print(L)
        #bishop moves
        if move == 2.1:
            v_moves = []
            L1 = []
            L2 = []
            L3 = []
            L4 = []

            for i in range(2,8-r):
                L1.append(((r+i),(c+i)))
                print(L1)
            for j in range(0,r):
                L2.append(((r-j),(c-j)))
                #print(L2)
            for k in range(1,8-c):
                L3.append(((r-k)+1,(c+k)+1))
                #print(L3)
            for l in range(1,r+2):
                L4.append(((r+l)+1,(c-l)+1))
                print(L4)
            L = L1+L2+L3+L4


    def moves(self):
        r = eval(input('enter roll:'))
        c = eval(input('enter column:'))
        self.v_moves(r-1, c-1)
a = My_chess()
a.start()
a.moves()