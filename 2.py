from math import sqrt, floor
def prime_nums(r):
    output = []
    for i in range(2,r):
        prime = True
        for j in range(2,floor(sqrt(i) + 1)):
            if (i%j==0):
                prime = False
        if prime:
            output.append(i)
    return output

def write_in_file(a):
    file = open("prime.txt", 'w')
    for i in a:
        file.write(f'{i}\n')

def main():
    n = 10000
    write_in_file(prime_nums(n))

if __name__ == '__main__':
    main()
