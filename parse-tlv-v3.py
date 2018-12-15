import codecs
with open('/Users/mayyanar/py/parser/v2-code/hex.tlv', 'r') as myfile:
    data = myfile.read().replace('\n', '').replace(" ", "")

print("Printing the SCF Header")
print('Printing only 60 bytes for brevity in the Values column')
print("------------------------------------------------------")
print('Tag/Type Name'+'\t'+'\t'+'Length'+'\t'+'Value')

while data != "":
    name = data[:2]
    data = data[2:] 			# Excluding first byte/two nibbles i.e name/tag from  data - This will be the Tag/type field
    if name == "0d":			# Check if the Tag value is 0d to flag End of Header and come out od SCF Header processing
        print(name+"   SCF Header Ends here - EOH")
        break
    length = data[:4].replace(" ", "")
    data = data[4:] 			# Excluding next two byte / 4 nibbles from  data - This will be the Length field
    # Reason for multiplying by 2 is because since each byte has two nibbles, when we slice character we need to double it (Ex: 0100 0201 02)
    value = data[:int(length, 16)*2]	# Slice 2* length from data - This will be the "Value"
    data = data[int(length, 16)*2:]
    if name == "04" or name == "06":
        ascii_value = str(codecs.decode(value, "hex"))
        print(name +'\t'+'\t'+'\t'+str(int(length, 16))+'\t'+':'+ascii_value[0:120])
    else:
        print(name+"\t"+'\t'+'\t'+str(int(length, 16))+": \t "+value[0:120])


print("Printing Certificate #1")
print('Printing only 60 bytes for brevity in the Values column')
print('-----------------------')
print('Tag/Type Name'+'\t'+'\t'+'Length'+'\t'+'Value')

while data != "":
    name = data[:2]
    data = data[2:] # Excluding first byte/name from my new data - Tag/type field
    length = data[:4].replace(" ", "")
    data = data[4:] # Excluding next two byte from my new data - Length field
    value = data[:int(length, 16)*2]
    data = data[int(length, 16)*2:]
    if name == "0a":
        print(name+"   EOR1")
        break
    elif name == "03" or name == "05":
        ascii_value = str(codecs.decode(value, "hex"))
        print(name +'\t'+'\t'+'\t'+str(int(length, 16))+'\t'+':'+ascii_value[0:120])
    else:
        print(name+"\t"+'\t'+'\t'+str(int(length, 16))+": \t "+value[0:120]) 

#print(name+"\t"+'\t'+'\t'+str(int(length, 16))+": \t "+value[0:120])

print("Printing Certificate #2")
print('Printing only 60 bytes for brevity in the Values column')
print('-----------------------')
print('Tag/Type Name'+'\t'+'\t'+'Length'+'\t'+'Value')

while data != "":
    name = data[:2]
    data = data[2:] # Excluding first byte/name from my new data - Tag/type field
    length = data[:4].replace(" ", "")
    data = data[4:] # Excluding next two byte from my new data - Length field
    value = data[:int(length, 16)*2]
    data = data[int(length, 16)*2:]
    if name == "0a":
        print(name+"   EOR2")
        break
    elif  name == "03" or name == "05":
        ascii_value = str(codecs.decode(value, "hex"))
        print(name +'\t'+'\t'+'\t'+str(int(length, 16))+'\t'+':'+ascii_value[0:120])
    else:
        print(name+"\t"+'\t'+'\t'+str(int(length, 16))+": \t "+value[0:120])
        
#print(name+"\t"+'\t'+'\t'+str(int(length, 16))+": \t "+value[0:120])

print("Printing Certificate #3")
print('Printing only 60 bytes for brevity in the Values column')
print('-----------------------')
print('Tag/Type Name'+'\t'+'\t'+'Length'+'\t'+'Value')

while data != "":
    name = data[:2]
    data = data[2:] # Excluding first byte/name from my new data - Tag/type field
    length = data[:4].replace(" ", "")
    data = data[4:] # Excluding next two byte from my new data - Length field
    value = data[:int(length, 16)*2]
    data = data[int(length, 16)*2:]
    if name == "0a":
        print(name+"   EOR3")
        break
    elif name == "03" or name == "05":
        ascii_value = str(codecs.decode(value, "hex"))
        print(name +'\t'+'\t'+'\t'+str(int(length, 16))+'\t'+':'+ascii_value[0:120])
    else:
        print(name+"\t"+'\t'+'\t'+str(int(length, 16))+": \t "+value[0:120])

# print(name+"   "+str(int(length, 16))+": "+value[0:120])

print("Printing Certificate #4")
print('Printing only 60 bytes for brevity in the Values column')
print('-----------------------')
print('Tag/Type Name'+'\t'+'\t'+'Length'+'\t'+'Value')

while data != "":
    name = data[:2]
    data = data[2:] # Excluding first byte/name from my new data - Tag/type field
    length = data[:4].replace(" ", "")
    data = data[4:] # Excluding next two byte from my new data - Length field
    value = data[:int(length, 16)*2]
    data = data[int(length, 16)*2:]
    if name == "0a":
        print(name+"   EOR4")
        break
    elif name == "03" or name == "05":
        ascii_value = str(codecs.decode(value, "hex"))
        print(name +'\t'+'\t'+'\t'+str(int(length, 16))+'\t'+':'+ascii_value[0:120])
    else:
        print(name+"\t"+'\t'+'\t'+str(int(length, 16))+": \t "+value[0:120])
 
#print(name+"\t"+'\t'+'\t'+str(int(length, 16))+": \t "+value[0:120])

print("Printing Certificate #5")
print('Printing only 60 bytes for brevity in the Values column')
print('-----------------------')
print('Tag/Type Name'+'\t'+'\t'+'Length'+'\t'+'Value')

while data != "":
    name = data[:2]
    data = data[2:] # Excluding first byte/name from my new data - Tag/type field
    length = data[:4].replace(" ", "")
    data = data[4:] # Excluding next two byte from my new data - Length field
    value = data[:int(length, 16)*2]
    data = data[int(length, 16)*2:]
    if name == "0a":
        print(name+"   EOR5")
        break
    elif name == "03" or name == "05":
        ascii_value = str(codecs.decode(value, "hex"))
        print(name +'\t'+'\t'+'\t'+str(int(length, 16))+'\t'+':'+ascii_value[0:120])
    else:
        print(name+"\t"+'\t'+'\t'+str(int(length, 16))+": \t "+value[0:120]) 

#print(name+"\t"+'\t'+'\t'+str(int(length, 16))+": \t "+value[0:120])

print("Printing Certificate #6")
print('Printing only 60 bytes for brevity in the Values column')
print('-----------------------')
print('Tag/Type Name'+'\t'+'\t'+'Length'+'\t'+'Value')

while data != "":
    name = data[:2]
    data = data[2:] # Excluding first byte/name from my new data - Tag/type field
    length = data[:4].replace(" ", "")
    data = data[4:] # Excluding next two byte from my new data - Length field
    value = data[:int(length, 16)*2]
    data = data[int(length, 16)*2:]
    if name == "0a":
        print(name+"   EOR6")
        break
    elif name == "03" or name == "05":
        ascii_value = str(codecs.decode(value, "hex"))
        print(name +'\t'+'\t'+'\t'+str(int(length, 16))+'\t'+':'+ascii_value[0:120])
    else:
        print(name+"\t"+'\t'+'\t'+str(int(length, 16))+": \t "+value[0:120]) 

#print(name+"\t"+'\t'+'\t'+str(int(length, 16))+": \t "+value[0:120])

