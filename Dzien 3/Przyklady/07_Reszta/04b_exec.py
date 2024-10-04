""" 
exec
"""
import os
os.system("cls")

war1 = 5
kod1 = "war2=10"
exec(kod1)
print(war2)

kod2 = """
lst1=[i*i for i in range(8)]
dic1=dict(enumerate(lst1))
"""
exec(kod2)

print(lst1)
print(dic1)
