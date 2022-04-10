from random import randint
board = []
sayac = 0
puan = 250
for i in range(5):
    board.append(["0"]*5)

def print_board(board):
    for satir in board:
        print (" ".join(satir))
def rand(board):
    return randint(1,len(board)-1)

print("-" * 35)
print("Amiral battı oyununa hoş geldiniz")
print("-" * 35)
print("Puanınız:", puan)
print("-" * 35)
print_board(board)

gemi_satir = rand(board)
gemi_sutun = rand(board)
gemi1_satir = rand(board)
gemi1_sutun = rand(board)
gemi2_satir = rand(board)
gemi2_sutun = rand(board)

while True:
    if(gemi_satir == gemi1_satir and gemi_sutun == gemi1_sutun):
        gemi1_satir = rand(board)
        gemi1_sutun = rand(board)
        continue
    elif (gemi_satir == gemi2_satir and gemi_sutun == gemi2_sutun):
        gemi2_satir = rand(board)
        gemi2_sutun = rand(board)
        continue
    elif (gemi1_satir == gemi2_satir and gemi1_sutun == gemi2_sutun):
        gemi2_satir = rand(board)
        gemi2_sutun = rand(board)
        continue
    else:
        print("-" * 35)
        tahmin_satir = int(input("Satır giriniz: "))
        tahmin_sutun = int(input("Sütun giriniz: "))

        if (tahmin_satir == gemi_satir and tahmin_sutun == gemi_sutun)\
            or (tahmin_satir == gemi1_satir and tahmin_sutun == gemi1_sutun) \
            or (tahmin_satir == gemi2_satir and tahmin_sutun == gemi2_sutun):
            if board[tahmin_satir - 1][tahmin_sutun - 1] == "/":
                print("-" * 35)
                print("Zaten tahmin ettiniz")
                print_board(board)
                print(puan)
            else:
                print("-" * 35)
                print("Tebrikler gemiyi batırdınız!")
                board[tahmin_satir - 1][tahmin_sutun - 1] = "/"
                print("Puanınız:",puan)
                print("-" * 35)
                print_board(board)
                sayac += 1
        else:
            if (tahmin_satir < 0 or tahmin_sutun < 0) or (tahmin_satir >5 or tahmin_sutun >5):
                print("-" * 35)
                print("Alan sınırları dışında değer girdiniz")

            elif board[tahmin_satir - 1][tahmin_sutun - 1] == "X":
                print("-" * 35)
                print("Zaten tahmin ettiniz")
                print("-" * 35)
                print_board(board)
            else:
                print("-" * 35)
                print("Vuramadınız")
                board[tahmin_satir - 1][tahmin_sutun - 1] = "X"
                puan -= 10
                print("Puanınız:", puan)
                print("-" * 35)
                print_board(board)

            if sayac == 3:
                print("-" * 35)
                print("Tebrikler bütün gemileri batırdınız ve oyunu kazandınız")
                print("-" * 35)
                break