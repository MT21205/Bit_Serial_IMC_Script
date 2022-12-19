Response = input("Do you want to perform multiplication? Y/N \n")
while(Response == 'Y'):
    # Accept the integer input
    multiplicand = bin(int(input("A = ")))
    multiplier = bin(int(input("B = ")))

    A = []
    B = []

    # extracted A and B
    for i in range(len(multiplicand)):
        if(i >= 2):
            A.append(int(multiplicand[i]))

    for i in range(len(multiplier)):
        if(i >= 2):
            B.append(int(multiplier[i]))


    A_len = len(A)
    B_len = len(B)

    # Reverse string for operation from LSB 
    A.reverse()
    B.reverse()

    # Product stored in reverse order
    P = [0]*(A_len + B_len)

    idx = 0     # index to track the tag bit used
    C_in = 0    # Carry in bit

    # Bit Serial Operation
    for tag in B:
        # Reset the Carry post copying Tag
        C_in = 0
        if(tag != 0):
            i = 0
            for ele in A:
                Sum = P[i+idx] ^ A[i] ^ C_in
                C_out = (((P[i+idx] ^ A[i]) & C_in) | (P[i+idx] & A[i]))
                P[i+idx] = Sum
                C_in = C_out
                i = i + 1
            P[i+idx] = C_out
            idx = idx + 1
        else:
            idx = idx + 1
    
    Product = 0
    idx = 0

    # Convert the product generated in binary to decimal value
    for val in P:
        Product = Product + val*(1<<idx)
        idx = idx + 1
    print(Product)
    Response = input("Do you want to perform multiplication? Y/N \n")
else:
    pass