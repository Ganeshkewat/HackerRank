def count_substring(string, sub_string):
    count= 0
    s_len=len(string)
    sub_len=len(sub_string)
    for i in range(0 , s_len):
     if string[i:].startswith(sub_string):
        
    # for i in range(len(string) - len(sub_string) + 1):
    #  if string[i:i+len(sub_string)] == sub_string:
        count += 1
        
    return count
   
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)