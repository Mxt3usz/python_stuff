#student_points = {"Adam": 63, "John": 112, "Donald": 43}
#changes = {"Adam": 3, "John": -7}

def update_points(student_points, changes):
    result = {}
    for key,value in student_points.items():
        for key2,value2 in changes.items():
            if key == key2:
                value += value2
                if value > 120 or value < 0:
                    raise ValueError("Die Gesamtpunktzahlt ist ungültig")
                else:
                    student_points[key] = value
            if key2 not in student_points:
                raise KeyError(key,"wurde nicht gefunden")
                #result.__setitem__(key,value)
            #else:
                #result.__setitem__(key,value)
    return student_points
#print(update_points(student_points,changes))

def compute_grade(student_points,max_points:int,name:str):
    pass_points = max_points/2
    failed = 0
    for key,val in student_points.items():
        if val < pass_points:
            failed += 1
    quote = failed / len(student_points)
    if quote >= 0.3: # reducing pass_points to a level where the person also
                     # passes
        for key,val in student_points.items():
            if val < pass_points:
                failed_val = val
                while failed_val < pass_points:
                    pass_points -= 1
                    if val >= pass_points:
                        break

    quarter =  pass_points * 0.25
    grade_4 = pass_points + quarter
    grade_3 = grade_4 + quarter
    grade_2 = grade_3 + quarter
    for key,value in student_points.items():
        if key == name:
            if value < pass_points:
                return 5
            if value < grade_4 and value >= pass_points:
                return 4
            if value < grade_3 and value >=  grade_4:
                return 3
            if value < grade_2 and value >= grade_3:
                return 2
            if value > grade_2:
                return 1

#print(compute_grade(student_points,120,"Adam"))

student_points = {"Mira": 80, "Olivia": 95, "Emily": 83}
def cluster_by_grade(student_points,max_points):
    result = {}
    grades = [] # stores grades so the keys that arent double
    for key,val in student_points.items():
        if  compute_grade(student_points,max_points,key) not in grades:
            grades.append(compute_grade(student_points,max_points,key))#grade,name
            result.__setitem__(compute_grade(student_points,max_points,key),[key])
        else: # if there is a double grade it will be inserted into value of key
              # as list
            result[compute_grade(student_points,max_points,key)] += [key]
    return result

print(cluster_by_grade(student_points,120))



