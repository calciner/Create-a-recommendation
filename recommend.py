#set up course
#refer Number : [is two Type of class , how many class , prefix name    , postfix name]
#0            : [1 or 0  (bool)       , 1 - 5 (int)    , Astro (string) , s (string)  ]
Astronomy = 0
BasicsOfCoding = 1
Biochemistry = 2
Chemistry = 3
Circuits = 4
EnvironmentalScience = 5
Psychology = 6
Zoology = 7
Statistics = 8


groupOfSience = [Astronomy,BasicsOfCoding,Chemistry,Circuits,EnvironmentalScience] 
groupOfLife = [Biochemistry,Zoology,EnvironmentalScience,Chemistry]
groupOfData = [BasicsOfCoding,Statistics,Psychology,EnvironmentalScience]

data = {0:[1,4,"Astrovid",""], # Astronomy
        1:[1,4,"Bc",""], # BasicsOfCoding
        2:[0,2,"Bio",""], # Biochemistry
        3:[0,4,"Chem",""], # Chemistry
        4:[1,3,"Circuit",""], # Circuits
        5:[0,4,"Es","s"], # EnvironmentalScience ***only have student version
        6:[1,4,"Psych",""], # Psychology
        7:[1,5,"Zoo",""], # Zoology
        8:[1,5,"Stat",""] # Statistics
        }

#set up group
#exaple:
# group of Data (stastic, coding)
# groupData = [4,5]  (a list)




def addCourseToSet(rSet,group,courseNum):
    if courseNum in group:
        for k in group:
            if k != courseNum:
                rSet.add(k)


relation = {}
for i in data:
    relationSet = set()
    addCourseToSet(relationSet,groupOfSience,i)
    addCourseToSet(relationSet,groupOfLife,i)
    addCourseToSet(relationSet,groupOfData,i)
    relation[i] = relationSet
print(relation)


def getReactCourseName(data,course,lesson,postfix):
    if data[course][0] == 1:
        return data[course][2] + str(lesson) + postfix
    else:
        return data[course][2] + str(lesson) + data[course][3]

for course in data:
    recomandList = []
    #print(data[course][2])
    for lesson in range(1,data[course][1]+1):
        #generate 5 recommand course
        if data[course][0] == 1:
            print(getReactCourseName(data,course,lesson,"s"))
            print(getReactCourseName(data,course,lesson,"p"))
        else:
            print(getReactCourseName(data,course,lesson,"s"))