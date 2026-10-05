def row_correct(sudoku:list,row_no:int):
    aranan_düzenli_liste=sorted(sudoku[row_no])
    for i in range(1,len(aranan_düzenli_liste)):
        if aranan_düzenli_liste[i]!=0:
            
            if aranan_düzenli_liste[i]==aranan_düzenli_liste[i-1]:
                return False
            else:
                continue
            
    return True
    
    
def column_correct(sudoku:list,column_no:int):
    kontrol_listesi=[]
    for i in range(len(sudoku)):
        if sudoku[i][column_no]!=0:
            if sudoku[i][column_no] in kontrol_listesi:
                return False
            else:
                kontrol_listesi.append(sudoku[i][column_no])
    return True


def block_correct(sudoku:list,row_no:int,column_no:int):
    sayi_kontrol_listesi=[]
    for satir in range(row_no,(row_no+3)):
        for eleman in range(column_no,(column_no+3)):
            if sudoku[satir][eleman]!=0:
                if sudoku[satir][eleman] in sayi_kontrol_listesi:
                    return False
                else:
                    sayi_kontrol_listesi.append(sudoku[satir][eleman]) 

    return True


def sudoku_grid_correct(sudoku: list):

    for x in range(0,7,3):
        for y in range(0,7,3):
            if row_correct(sudoku,x)!=True:
                return False
            if column_correct(sudoku,y)!=True:
                return False
            if block_correct(sudoku,x,y)!=True:
                return False
            
    return True


sudoku2 = [
  [2, 6, 7, 8, 3, 1, 5, 0, 4],
  [9, 0, 3, x, 1, 0, x, 0, 0],
  [0, 5, 1, x, 0, x, 8, 3, 9],
  [5, x ,9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, x, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, x, 5, 7, 2, 6, 3],
  [3, x, x, 0, 8, 0, 0, 5, x],
  [7, 4, x, 0, 0, 3, 9, 0, 1]
]

