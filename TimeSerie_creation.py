"""
You get 5 useful outputs:
    Population is a dictionary with the abbreviation of state as key and the population of the state as value
    Confirmed and Deaths are dictionary with the abbreviation of state as key and the array with total amount of confirmed/death date by date
    Confirmed_dates and Death_dates are arrays with the dates corresponding to what is in the corresponding dictionary

    If you need it, Name2ab is a dictionary with the name of a state as key and its abbgreviation as value

"""

# Creates the dictionary that link the name to its abbreviation
with open("Abbreviation.csv", "r") as file_abb:
    LINES = file_abb.readlines()
    a = 2

Name2ab = dict()

for LINE in LINES:
    LINE = LINE.strip()
    res = LINE.split(sep=',')
    Name2ab[res[0]]=res[1]

#Sum field by field of a list
def merge(l1, l2):
    N = len(l1)
    l=list()
    for i in range(0, N):
        l.append(l1[i]+l2[i])
    return l

#Initialization
Deaths = dict()
Confirmed = dict()
Population = dict()

# Process for death
with open("TimeSerie_death.csv", "r") as file_death:
    head = file_death.readline()

    head = head.strip()
    head = head.split(sep=',')
    num_tot = len(head)
    num_date = num_tot -12
    
    Death_dates = head[12:num_tot]

    #Creation of keys and empty fields
    for name in Name2ab:
        Population[Name2ab[name]] = 0;
        Deaths[Name2ab[name]] = [0]*num_date;

    #Filling for each line
    for line in file_death:
        temp = line.split(sep="\"")
        line = temp[0]+temp[2]     #We avoid the comma inside of a field
        line = line.split(sep=',')
        ab = Name2ab.get(line[6])
        if ab is None:
            continue
        
        Population[ab] = Population[ab]+int(line[11])
        Deaths[ab] = merge(Deaths[ab], [int(x) for x in line[12:num_tot]])

# Process for confirmed         
with open("TimeSerie_confirmed.csv", "r") as file_conf:
    head = file_conf.readline()

    head = head.strip()
    head = head.split(sep=',')
    num_tot = len(head)
    num_date = num_tot -11
    
    Confirmed_dates = head[11:num_tot]

    #Creation of keys and empty fields
    for name in Name2ab:
        Confirmed[Name2ab[name]] = [0]*num_date;
    
    #Filling for each line
    for line in file_conf:
        temp = line.split(sep="\"")
        line = temp[0]+temp[2]     #We avoid the comma inside of a field
        line = line.split(sep=',')
        ab = Name2ab.get(line[6])
        if ab is None:
            continue
        Confirmed[ab] = merge(Confirmed[ab], [int(x) for x in line[11:num_tot]])














