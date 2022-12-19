n = int(input("Enter the tag size (multiplier) in bits : ")) # n = Tag Size
m = int(input("Enter the number to be multiplied (multiplicand) size in bits : ")) # m = Number to be multiplied

# LSB position of Tag
LSB_Tag = n-1
LSB_Num = n+m-1
LSB_Product = 2*(n+m)-1

# stimuli duration in ns
cycle_length =int((n * (2 + m*2))) 
single_op_cycle_length = 2+(m*2)
stim_length = int((n * (2 + m*2)) * 1.5)     # Each cycle is 1.5ns in length
vector_length = 3*stim_length           # Each 1.5ns is split as 3 * 0.5ns 

on_string = "100"
off_string = "000"
#The stimuli is generated from MSB

# LSB TAG Stimuli
vector = "0" + on_string + off_string *int(cycle_length-1)
src_num = 306
print("V"+str(src_num)+ " VWL"+ str(LSB_Tag) +" GND PATTERN (supply 0 0 tr tf 500p "+ vector +')')
src_num = src_num + 1

# Stimuli for Tag
for i in range(1,n):
    vector = (off_string)* (int((2 + m*2)) * i) + on_string +  (off_string)* (cycle_length -1 -(int((2 + m*2)) * i))
    print("V"+str(src_num)+ " VWL"+ str(LSB_Tag-i) +" GND PATTERN (supply 0 850p tr tf 500p "+ vector +')')
    src_num = src_num + 1
         


# Stimuli for Multiplicand
for i in range(m):
    vector = off_string + (off_string)*(i*2) + (on_string + ((2 + m*2) - 1)*off_string)*(n-1) + on_string+ off_string * (cycle_length - (1+(i*2)+((2 + m*2) * (n-1))+1))
    # V308 VWL3 GND PATTERN (supply 0 500p tr tf 500p 000100000000000000000100000000000000)
    print("V"+str(src_num)+ " VWL"+ str(LSB_Num-i) +" GND PATTERN (supply 0 500p tr tf 500p "+ vector +')')
    src_num = src_num + 1



# Stimuli for Product
pos_rep = [0]*(n+m-1)
temp = 1

if((n+m-1)%2 == 0):
    mid = (n+m-1)/2
else:
    mid = (n+m-2)/2
    mid = mid+1

for i in range(int(mid)):
    pos_rep[i] = temp
    pos_rep[-1-i] = temp
    temp = temp + 1
    

print(pos_rep)
carry_ct = 1
for i in range(n+m):
    if(i<m):
        vector = off_string + (off_string)*(i*2) + (on_string*2 + off_string*((m-1)*2))*(pos_rep[i]) + off_string * (cycle_length - (1 + (i*2) + (pos_rep[i]*(2+(m-1)*2))))    
    else:
        if((i) != (n+m-1)):
            vector = off_string * ((single_op_cycle_length*carry_ct)-1) + on_string + (off_string*((m-1)*2 + 1))+ on_string*2 + ((off_string*((m-1)*2) + on_string*2) * (pos_rep[i]-1)) + off_string * (cycle_length - (((single_op_cycle_length*carry_ct)-1) + 1 + ((m-1)*2 + 1) + 2 + (2*m*(pos_rep[i]-1))))
        else:
            vector = off_string * ((single_op_cycle_length*carry_ct)-1) + on_string
        carry_ct = carry_ct + 1
    #V312 VWL23 GND PATTERN (supply 0 500p tr tf 500p 000100100000000000000000000000000000)
    print("V"+str(src_num)+ " VWL"+ str(LSB_Product-i) +" GND PATTERN (supply 0 500p tr tf 500p "+ vector +')')
    src_num = src_num + 1