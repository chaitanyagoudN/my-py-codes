# Assignment
# Author: Chaitanya Goud Nayanoola
# Global ID: 868158

age=int(input("Please enter age: "))
race_distance=0.0
max_hr=0.0

s_distance=int(input("Please select options \n1 for 1500\n2 for 5000\n3 for 10000\n4 for  13.1\n: "))
if s_distance==1:  
    race_distance=1500
elif s_distance==2: 
    race_distance=5000   
elif s_distance==3:
    race_distance=10000
elif s_distance==4:
    race_distance=13.1
else:
    print("Please select valid input value")
    exit()
#max heartrate 220-age

heart_rate=220-age
if race_distance==1500:
    max_hr=heart_rate*(95/100)
elif race_distance==5000:
    max_hr=heart_rate*(90/100)
elif race_distance==10000:
    max_hr=heart_rate*(85/100)
elif race_distance==13.1:
    max_hr=heart_rate*(75/100)

print("For a "+str(age)+" year old runner, targeting a "+str(race_distance)+" race, you should shoot for a heart rate of "+str(max_hr)+" during the race.")
