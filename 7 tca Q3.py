print ("How many zones must I cross?")
zones = int(input())
print ("Crossing zones...")
for count in range (zones,0,-1):
    print ("…crossed zone " + str(count))
print ("Crossed all zones.  Jumanji!")