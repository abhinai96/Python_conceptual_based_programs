old_dict={"name":"abhinai","age":24}
print(old_dict)

new_dict=dict([(value,key) for key,value in old_dict.items()])

#after swapping
for i in new_dict:
        print(i,":",new_dict[i])


