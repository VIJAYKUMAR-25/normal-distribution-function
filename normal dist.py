print("**** INPUTS TO FIND PROBABILITY  DISTRIBUTION *******")

#user inputs for mean and sigma
MEAN=int(input("ENTER THE MEAN VALUE:"))
SIGMA=int(input("ENTER THE SIGMA VALUE:"))
SD=int(input("Enter the value:"))
DD=int(input("Enter the value:"))

from statistics import NormalDist
SM=NormalDist( mu = MEAN, sigma=SIGMA)
M=SM.cdf(SD)
D=SM.cdf(DD)
N=M-D

print("The Output is below \n")

if(N>0):
    print("The value will be",N)
elif(D>0):
    print("The value will be",D)
else:
    print("The value will be",M)
