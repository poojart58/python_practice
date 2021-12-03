#This is unpacking touple and returning the employee which has maximum number of work hours

work_hours = [('Abby',100),('Billy',200),('Cassie',500),('howie',1000)]

def emp_check(work_hours):
    current_max=0
    emp_of_month=''
    for employee,hours in work_hours:
        if hours > current_max:
            current_max=hours
            emp_of_month=employee
        else:
            pass
    return (emp_of_month,current_max)
  
  emp_check(work_hours)
