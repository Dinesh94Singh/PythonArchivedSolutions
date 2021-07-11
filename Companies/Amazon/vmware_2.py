"""
There is a csv file that keeps a record of n order details for orders made at an online shopping website. The file has a .csv extension.



Each line contains a single record with the following columns, in order:

Id of the order placed
Area where the order was delivered
Name of the product
Quantity of the product delivered in that order
Brand of the ordered product


Create two csv files named 0_input_file_name and 1_input_file_name where input_file_name is the name of the input file given in the input including the .csv extension. Each file must contain r rows where r is the number of distinct products. Data should be comma delimited, and the row order does not matter.



The structure of each file is as follows:

0_input_file_name - In the first column, list the product Name.  The second column should contain the average quantity of the product purchased per order.
1_input_file_name -  In the first column, list the product Name. The second column should be the most popular Brand for that product. Most popular is defined as the brand with the most total orders for the item, not the quantity purchased. If two or more brands have the same popularity for a product, include any one.


The value of the average quantity will be considered correct if the absolute difference between your answer and the jury's answer is less than 1e-3 (0.001)



Example:

There are four total orders in input_example.csv:

ID1,Minneapolis,shoes,2,Air
ID2,Chicago,shoes,1,Air
ID3,Central Department Store,shoes,5,BonPied
ID4,Quail Hollow,forks,3,Pfitzcraft


The orders for shoes are 2 pairs of Air brand, 1 pair of Air, and 5 pairs of BonPied. The most popular shoe brand is Air because there were two orders versus one for BonPied. The total shoes sold is 2 + 1 + 5 = 8, and there are 4 total orders. The average shoes per order is 8/4 = 2. There is one order for 3 forks made for Pfitzcraft. The average number of forks per order is 3/4 = 0.75. The files should each contain two lines:

0_input_example.csv:
shoes,2
forks,0.75

1_input_example.csv:
shoes,BonPied
forks,Pfitzcraft


Function Description

Complete the generateFiles function in the editor below. It must create the two files described above.



generateFiles has the following parameter(s):

    input_file  a string input_file_name representing the name of the input file.



Constraints

1 ≤ n ≤ 104


Input Format For Custom Testing
Sample Case 0
Sample Input 0

order_log00.csv
Sample Output 0

0_order_log00.csv
Intelligent Copper Knife,2.4
Small Granite Shoes,0.8
1_order_log00.csv
Intelligent Copper Knife,Hilll-Gorczany
Small Granite Shoes,Rowe and Legros


Sample Explanation 0

The order_log00.csv file contains the following records.
ID944806,Willard Vista,Intelligent Copper Knife,3,Hilll-Gorczany
ID644525,Roger Centers,Intelligent Copper Knife,1,Kunze-Bernhard
ID348204,Roger Centers,Small Granite Shoes,4,Rowe and Legros
ID710139,Roger Centers,Intelligent Copper Knife,4,Hilll-Gorczany
ID426632,Willa Hollow,Intelligent Copper Knife,4,Hilll-Gorczany
File 0_order_log00.csv is created based on the following:

There are 4 orders for Intelligent Copper Knife products that total 12 items.
There is 1 order for Small Granite Shoes totaling 4 items.


There are 5 total orders, so the average per order is 12/5 = 2.4 for Intelligent Copper Knife, and 4/5 = 0.8 for Small Granite Shoes.



File 1_order_log00.csv is created based on the following:

There are  4 orders for Intelligent Copper Knife,
3 branded Hilll-Gorczany and
1 branded Kunze-Bernhard.
There is 1 order for Small Granite Shoes made by Rowe and Legros.


Hilll-Gorczany and Rowe and Legros are the most popular brands for each item.
"""