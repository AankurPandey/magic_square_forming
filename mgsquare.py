                                  # MAGIC SQUARE


# print("\n\n\t\t\tTHIS IS THE PROGRAM FOR MAGIC SQUARE \n \n")
# while 1:
# 	print(" \n\n\t\tenter your choice:")
# 	print("\t\t1.creat and enter the values of square")
# 	print("\t\t2.check wheather the square is a magic square or not")
# 	print("\t\t3.change value of a specific element")
# 	print("\t\t4.change values of a specific row")
# 	print("\t\t5.change values of a specific column")
# 	print("\t\t6.show square")
# 	print("\t\t7.exit")
# 	choice=int(input())
# 	############################################################code for creating the square
# 	if choice==1:
# 		row=int(input("enter the no rows\n"))
#		sss=(row((row**2)+1)//2)
# 		mainSquare=[]
# 		i=0
# 		while i<row:
# 			a=[]
# 			for r in range(row):
# 				print("enter the element at row",(i+1),"and column",(r+1))
# 				a.append(int(input()))
# 			mainSquare.append(a)
# 			i+=1
# 			del a
# 		del i
# 	############################################################code tocheck wheather the square is a magic square or not
# 	elif choice==2:
# 		######################################################################	code for sum of row and column
# 		i=0
# 		k=row-1
# 		rowSum=[]
# 		colSum=[]
# 		diog1=0
# 		diog2=0
# 		while i<len(mainSquare):
# 			diog1+=mainSquare[i][i]
# 			diog2+=mainSquare[i][k]
# 			tolRow=0
# 			tolCol=0
# 			j=0
# 			while j<len(mainSquare):
# 				tolRow+=mainSquare[i][j]
# 				tolCol+=mainSquare[j][i]
# 				j+=1
# 			rowSum.append(tolRow)
# 			colSum.append(tolCol)
# 			i+=1
# 			k-=1

# 		##############################################################comparing the values of column and rows AND printing result
# 		i=0
# 		k=1
# 		for i in range(row-1):
# 			if rowSum[i]==rowSum[i+1]==sss and colSum[i]==colSum[i+1]==sss and colSum[i]==rowSum[i]==sss and diog1==diog2==sss:
# 				k+=1
# 		if k==row:
# 			print("its a magic square") 
# 		else:
# 			print("its not a magic square")				
			

# 	####################################################################change value of a specific element##########
# 	elif choice==3:
# 		r=int(input("enter the row"))
# 		c=int(input("enter the column"))
# 		mainSquare[r-1][c-1]=int(input("enter the value"))
# 		print("changed")
# 		del r,c
# 	##################################################################change values of a specific row##############
# 	elif choice==4:
# 		r=int(input("enter the row"))
# 		for i in range(row):
# 			print("enter element at row",r,"and column",i+1)
# 			mainSquare[r-1][i]=int(input())
# 		print("elements of row",r,"changed")
# 		del r	
# 	######################################################################change values of a specific column
# 	elif choice==5:
# 		c=int(input("enter the column"))
# 		for i in range(row):
# 			print("enter element at row",i+1,"and column",c)
# 			mainSquare[i][c-1]=int(input())
# 		print("elements of column",c,"changed")
# 		del c
# 	##########################################################################show square
# 	elif choice==6:
# 		for i in range(row):
# 			print(mainSquare[i])




# 	#########################################################exit	
# 	elif choice==7:
# 		break

# 	else:
# 		print("invalid choice")
# 		break
main_list = []
row_no = int(input('enter number of rows\n'))
for row in range(row_no):
	inp = list(map(int, input('input for row '+str(row+1)+'\n').strip().split()))
	main_list.append(inp)
	del inp

sum_should_be = row_no*((row_no**2)+1)//2

sum = [0, 0, 0, 0] 
for row_value in range(len(main_list)):
    row_sum = 0
    col_sum = 0
    row_no-= 1
    for col_value in range(len(main_list)):
        row_sum+= main_list[row_value][col_value]
        col_sum+= main_list[col_value][row_value]
    sum[2]+= main_list[row_value][row_value]
    sum[3]+= main_list[row_value][row_no]

    if col_sum == row_sum == sum_should_be:
        sum[0] = row_sum
        sum[1] = col_sum
    else:
        print('not a magic square')
        break

if sum[2] == sum[3] == sum_should_be:
    print('is a magic square')



