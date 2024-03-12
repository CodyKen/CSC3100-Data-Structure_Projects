data = input()    
data = data.split()   # Transfer the data into a list
n = int(data[0])
a = int(data[1])
b = int(data[2])
f0 = int(data[3])
f1 = int(data[4])
m = int(data[5])
coe = [[a,b],[1,0]]


def matrix_multiply_2by2 (A, B, mod):
    # Perform matrix multiplication
    ele1 = (A[0][0] * B[0][0]) + (A[0][1] * B[1][0])
    ele2 = (A[0][0] * B[0][1]) + (A[0][1] * B[1][1])
    ele3 = (A[1][0] * B[0][0]) + (A[1][1] * B[1][0])
    ele4 = (A[1][0] * B[0][1]) + (A[1][1] * B[1][1])
    
    result = [[ele1, ele2], [ele3, ele4]]

    return result

def matrix_power_2by2 (A, x, mod):
    if x == 0:
        return [[1,0],[0,1]]
    elif x == 1:
        return A
    else:
        B = A
        n = 2
        while n <= x:
            B = matrix_multiply_2by2 (B, B, mod)
            n *= 2
        
        n = n//2
        Remainder = matrix_power_2by2 (A, x-n, mod)
        return matrix_multiply_2by2 (B, Remainder, mod)
    
def coe_multiply(x, mod):
    return matrix_power_2by2 (coe, x-1, mod)

def cal_mod(x, mod):
    new_coe = coe_multiply(x, mod)
    fn = (new_coe[0][0] * f1) + (new_coe[0][1] * f0)
    ans = fn % mod
    return ans

print(cal_mod(n, m))

