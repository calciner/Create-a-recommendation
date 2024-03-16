#set up course
#refer Number : [is two Type of class , how many class , class name in react]
#0            : [1 or 0  (bool)       , 1 - 5 (int)    , Astro (string)     ]
data = {0:[1,4,"Astrovid"], #
        1:[1,4,"Bc"], #
        2:[0,2,"Bio"], #
        3:[0,4,"Chem"], #
        4:[1,3,"Circuit"], #
        5:[0,4,"Es"], #
        6:[1,4,"Psych"], #
        7:[1,5,"Zoo"], #
        8:[1,5,"Stat"] #

        }

#set up group
#exaple:
# group of Data (stastic, coding)
# groupData = [4,5]  (a list)

groupData = [1,4,5] 
groupSience = [0,1,3,4]

def addCourseToSet(rSet,group,courseNum):
    if courseNum in group:
        for k in group:
            if k != courseNum:
                rSet.add(k)


relation = {}
for i in data:
    relationSet = set()
    addCourseToSet(relationSet,groupData,i)
    addCourseToSet(relationSet,groupSience,i)
    relation[i] = relationSet
print(relation)


def getReactCourseName(data,courseNum,isStudent):
    if data[courseNum][0] == 1:
        if isStudent is True:
            return data[courseNum][2] + courseNum + "s"
        else:
            return data[courseNum][2] + courseNum + "p"
    else:
        return data[courseNum][2] + courseNum

for course in data:
    recomandList = []
    for lesson in range(data[i][1]):
        #generate 5 recommand course
        print(lesson)