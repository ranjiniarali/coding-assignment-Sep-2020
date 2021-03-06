def a(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

def b(array_val,n,k,l):
    result = +2147483647 
    final_output.clear()
    array_val.sort() 
    for i in range(n-k+1): 
        result = int(min(result, array_val[i+k-1] - array_val[i])) 
    for j in range(0,l):
        for name,value in input_goodies.items():
            if(int(value)==array_val[k+j]):
                val = a([name,value])
                final_output.update(val)
    return result



input_file = open(r"C:/Users/RANJINI/Deskstop/sample_inut.txt.py",'r')
global input_goodies, final_output 
input_goodies = {}
final_output = {}

for line in input_file:
    lines = line.split(":")
    val = a(lines)
    input_goodies.update(val)

val = (input_goodies.values())
actual = []
for n in val:
    actual.append(int(n))

arr= actual 
n =len(arr) 
input_file.close()
while(True):
    f = open("output.txt", "a")
    k = int(input("Number of employees : ")) 
    f.write("Number of employees : "+str(k))
    f.write("\n")
    f.write("Here the input_items that are selected for distribution are:")
    f.write("\n")
    result = b(arr, n, k,k)
    for name,value in final_output.items():
        f.write(name+" : "+value)
    f.write("\n")
    print("Output File Written")
    f.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(result))
    f.write("\n")
    f.close()
