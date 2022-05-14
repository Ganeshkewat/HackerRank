def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    for x in range(0,n,k):
     slicedstr = string[x : x+k]
     unic =[]
     for y in slicedstr:
        if y not in unic:
           unic.append(y)
     j = "".join(unic)
     print(j)
     
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)