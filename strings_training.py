

full_name = "Leo Messi"
len_full_name= len(full_name)
print (len_full_name)

full_name_new = full_name.replace("Leo","Leonid")

full_name_new_2 = "Eli      Cohen"
print(full_name_new_2)

index=full_name.index(" ")  #cutts the name from the beggining till the brake

first_name=full_name[0:index]
last_name=full_name[index+1:len_full_name] # index+1 the space before the last name is not included

print(f'First name is: {first_name}')
print (f'Last name is: {last_name}')
print(index)