move=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

st=f'''
{move[0]}|{move[1]}|{move[2]}
------
{move[3]}|{move[4]}|{move[5]}
______
{move[6]}|{move[7]}|{move[8]}
'''
print(st)
turn='x'
while 1:

      loc=int(input(f'{turn}turn enter the location 0-8:'))
      if  loc>8 or move[loc]!=" ":
        print("location already in use try again")
        continue
      else:

       move [loc] = turn
      print(f'''
      {move[0]}|{move[1]}|{move[2]}
------
      {move[3]}|{move[4]}|{move[5]}
______
      {move[6]}|{move[7]}|{move[8]}
      ''')
      if ' ' not in move:
        print("tie")
        break
      if move[0]==move[1]==move[2]!=" ":
        print(move[0],"win")
        break
      if move[0]==move[4]==move[8]!=" ":
        print(move[0],"win")
        break
      if move[1]==move[4]==move[7]!=" ":
        print(move[1],"win")
        break
      if move[2]==move[5]==move[8]!=" ":
        print(move[2],"win")
        break
      if move[3]==move[4]==move[5]!=" ":
        print(move[0],"win")
        break
      if move[6]==move[7]==move[8]!=" ":
        print(move[6],"win")
        break
      if move[2]==move[4]==move[6]!=" ":
        print(move[2],"win")
        break
      turn= "x" if turn=="o" else"o"



