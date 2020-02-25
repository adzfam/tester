
#[nan '24â€“52 weeks' 'more than 1 Year' '>1 Year' '0â€“6 weeks'
# 'more than 1 year' '6â€“12 weeks' '12â€“24 weeks' '12-24'
# 'More than 1 year' '24-52' '0-6' '6-12']

#reorganising the data
problem = {
#   key  :  value
    'nan'  : 0,
    '24â€“52 weeks' : 4,
    'more than 1 Year' : 5,
    '>1 Year' : 5,
    '0â€“6 weeks': 1,
 'more than 1 year' : 5,
    '6â€“12 weeks' : 2,
    '12â€“24 weeks' : 3,
    '12-24' : 3,
 'More than 1 year' : 5,
    '24-52' :4,
    '0-6' :1,
    '6-12':2
}
#organisng the data
problem2 = {
#   key  :  value
    0: 'nan',
    1: '0 - 6 weeks',
    2: '6 - 12 weeks',
    3: '12 - 24 weeks',
    4: '24 - 52 weeks',
    5: '> 52 weeks',
}
print(problem2)
