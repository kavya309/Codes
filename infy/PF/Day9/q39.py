#PF-Prac-39
def max_populated_state(cities_dict,state):
    max_populated_city={}
    #start writing your code here
    #for i in range(len(cities_dict)):
    #for i, state in enumerate(d['State'] for d in cities_dict): 
        #print (state)
    mx=0
    for i in cities_dict:
        for key,value in i.items():
            if(key=='State' and value=='WA'):
                if(mx<i['Population']):
                    mx=i['Population']
                    nm=i['Name']
    max_populated_city[nm]=mx
    return max_populated_city
    
cities_dict = [
 {'Name':'Vancouver','State':'WA','Population':161791},
 {'Name':'Salem','State':'OR','Population':154637},
 {'Name':'Seattle','State':'WA','Population':80885},
 {'Name':'Bellingham','State':'WA','Population':608660},
 {'Name':'Spokane','State':'WA','Population':208916},
 {'Name':'Bellevue','State':'WA','Population':608660},
 {'Name':'Portland','State':'OR','Population':583776}
 ]
state="WA"
print("The city details are:",cities_dict)
print("State:",state)
output=max_populated_state(cities_dict,state)
print("The highest populated city in the given state is:",output)
