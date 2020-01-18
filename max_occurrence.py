def most_occurrence(string_ip):
    count={}
    max_count=0
    max_item=None

    for i in string_ip:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
        
        if count[i]>max_count:
            max_count=count[i] 
            max_item=i
    
    return max_item,max_count

string_ip=input("Enter a string")
print(most_occurrence(string_ip))