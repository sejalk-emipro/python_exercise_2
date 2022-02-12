import functools

from gevent.corecext import fork

emp_dict =  {
            101:{'name': 'Anupriya Roy','depart_id':1,
                    'attendances':[{'date':1, 'hours':[3.5,4.5]},{'date':2, 'hours':[3.2,4.5]},{'date':3, 'hours':[3.2,4.6]},
                                 {'date':4, 'hours':[3.0,4.5]},{'date':5, 'hours':[2.5,4.5]},{'date':6, 'hours':[1.5,4.5]},
                                 {'date':7, 'hours':[2,3]},{'date':8, 'hours':[0,4.5]},{'date':9, 'hours':[2,3.5]},
                                 {'date':10, 'hours':[4,3.5]}],
                    'leaves':[{'date':7, 'no_of_hours':1.5},{'date':7, 'no_of_hours':1.5},{'date':8, 'no_of_hours':3}]
                },
            102:{'name': 'Kadambari Sharma','depart_id':1,
                 'attendances':[{'date':1, 'hours': [0,4.5]},{'date':2, 'hours':[3.2,0]},{'date':3, 'hours':[3.2,4.6]},
                                {'date':4, 'hours':[1,4.5]},{'date':5, 'hours':[2.5,2]},{'date':6, 'hours':[1.5,1]},
                                {'date':7, 'hours':[2,4]},{'date':8, 'hours':[1,4.5]},{'date':9, 'hours':[2,2]},
                                {'date':10, 'hours':[2,3.5]}],
                 'leaves':[{'date':1, 'no_of_hours':3.5},{'date':2, 'no_of_hours':2},{'date':2, 'no_of_hours':2}]
                },
            103:{'name': 'Abhishek Verma','depart_id':1,
                'attendances':[{'date':3, 'hours':[3.2,4.6]},{'date':4, 'hours':[1,4.5]},{'date':5, 'hours':[2.5,2]},
                            {'date':6, 'hours':[1.5,1]},{'date':7, 'hours':[2,4]},{'date':8, 'hours':[1,4.5]},
                            {'date':9, 'hours':[2,2]},{'date':10, 'hours':[2,3.5]}],
                'leaves':[{'date':1, 'no_of_hours':3},{'date':2, 'no_of_hours':2},{'date':2, 'no_of_hours':3}]
            }}

emp_Attendance_leave_data=[]
emp_attendance_leave_date_lessthen_7=[]
total_working_hours=8
# all_value_sum=sum(functools.reduce(lambda a, b:a+b,l))
# even_list=list(filter(lambda x: (x % 2 == 0), (functools.reduce(lambda a, b:a+b,l))))
# print(reduce(lambda x,y: x+y, map(lambda s: s['grade'], grades)))
# print(reduce(lambda acc,y: acc+y['grade'], grades, 0))
# sum([val for sublist in l for val in sublist if val%2==0])
for key,value in emp_dict.items():
    attendance_sum = sum(functools.reduce(lambda x, y: x+y, map(lambda s: s['hours'], value.get('attendances'))))
    leave_sum=functools.reduce(lambda x, y: x+y, map(lambda s: s['no_of_hours'], value.get('leaves')))
    emp_Attendance_leave_data.append({'employee_id': key, 'employee_name':value.get('name'),'total_attendance_hours': attendance_sum, 'total_leave_days': leave_sum})

    date=functools.reduce(lambda x, y: y+y, map(lambda y: y['hours'], value.get('attendances')) )
    all_data=[{date:[{'total_hrs':sum(hours),'remaining_hrs':total_working_hours-sum(hours)}]} for lst in value.get('attendances') for key,date in lst.items() if key=='date' for key,hours in lst.items() if key=='hours' and sum(hours)<7 ]

    date=[date for values in all_data for date in values.keys()]
    total_hrs=[value for values in all_data for key,value in values.items()]
    # emp_attendance_leave_date_lessthen_7.append({key:{'date':date,'total_hrs':,'remaining_hrs':}})
    # print(total_hrs)

print(emp_Attendance_leave_data)
