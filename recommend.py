import random

# map course to a number.
Astronomy = 0
BasicsOfCoding = 1
Biochemistry = 2
Chemistry = 3
Circuits = 4
EnvironmentalScience = 5
Psychology = 6
Zoology = 7
Statistics = 8


#set up group
groupOfSience = [Astronomy,BasicsOfCoding,Chemistry,Circuits,EnvironmentalScience] 
groupOfLife = [Biochemistry,Zoology,EnvironmentalScience,Chemistry]
groupOfData = [BasicsOfCoding,Statistics,Psychology,EnvironmentalScience]

#set up course
#refer Number : [is two Type of class , how many class , prefix name    , postfix name]
#0            : [1 or 0  (bool)       , 1 - 5 (int)    , Astro (string) , s (string)  ]
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



#add one course to the relationship set to make sure they a not repeat.
def addCourseToSet(rSet,group,courseNum):
    if courseNum in group:
        for k in group:
            if k != courseNum:
                rSet.add(k)


#collect all the courese have the relationship with target course.
relation = {}
for i in data:
    relationSet = set()
    addCourseToSet(relationSet,groupOfSience,i)
    addCourseToSet(relationSet,groupOfLife,i)
    addCourseToSet(relationSet,groupOfData,i)
    relation[i] = relationSet
print(relation)

#format relation with 3 course in the relation, 1 course pick from other that not in the relation set.
for i in relation:
    NotInRelation = []
    for k in data:
        if k == i:
            continue;
        if k not in relation[i]:
            NotInRelation.append(k)
    if(len(NotInRelation) == 0):
        relation[i] = random.sample(list(relation[i]),4)
    else:
        relation[i] = random.sample(list(relation[i]),3)
        relation[i].extend(random.sample(NotInRelation,1))


print(relation)

def getReactCourseNameP(data,course,lesson):
    return data[course][2] + str(lesson) + "p"

def getReactCourseNameS(data,course,lesson):
    return data[course][2] + str(lesson) + "s"

def getReactCourseName(data,course,lesson):
    return data[course][2] + str(lesson) + data[course][3]


# def getLessonFromCourseP(data,course):
#     lesson = random.randint(1,data[course][1])
#     return data[course][2]+str(lesson) + "p"

# def getLessonFromCourseS(data,course):
#     lesson = random.randint(1,data[course][1])
#     return data[course][2]+str(lesson) + "s"

def getLessonFromCourse(data,course,postfix):
    if data[course][0] == 1:
        lesson = random.randint(1,data[course][1])
        return data[course][2]+str(lesson) + postfix
    else:
        lesson = random.randint(1,data[course][1])
        return data[course][2]+str(lesson) + data[course][3]


#base on the relation, create the recommendation for every single course.
stemZRecommendList = {}
for course in data:
    for lesson in range(1,data[course][1]+1):
        #generate 5 recommand course
        if data[course][0] == 1:
            #parent course
            currentCourse = getReactCourseNameS(data,course,lesson)
            recommendList = {}
            count = 0
            if lesson < data[course][1]:
                recommendList[count] = getReactCourseNameS(data,course,lesson + 1)
            else:
                recommendList[count] = getReactCourseNameS(data,course,lesson - 1)
            for l in relation[course]:
                count = count +1
                recommendList[count] = getLessonFromCourse(data,l,"s")
            
            stemZRecommendList[currentCourse] = recommendList

            #student course
            currentCourse = getReactCourseNameP(data,course,lesson)
            recommendList = {}
            count = 0
            if lesson < data[course][1]:
                recommendList[count] = getReactCourseNameP(data,course,lesson + 1)
            else:
                recommendList[count] = getReactCourseNameP(data,course,lesson - 1)
            for l in relation[course]:
                count = count +1
                recommendList[count] = getLessonFromCourse(data,l,"p")
            
            stemZRecommendList[currentCourse] = recommendList
        else:
            #course without mark of student or parent.
            currentCourse = getReactCourseName(data,course,lesson)
            recommendList = {}
            count = 0
            if lesson < data[course][1]:
                recommendList[count] = getReactCourseName(data,course,lesson + 1)
            else:
                recommendList[count] = getReactCourseName(data,course,lesson - 1)
            for l in relation[course]:
                count = count +1
                recommendList[count] = getLessonFromCourse(data,l,"s")
            
            stemZRecommendList[currentCourse] = recommendList

print(stemZRecommendList)

import json

#out put result as json file.
filename = "data.json"
with open(filename, "w") as json_file:
    json.dump(stemZRecommendList, json_file,indent=4)

print("JSON file has been generated.")