# https://www.codechef.com/problems/FLOW011
for _ in range(int(input())):
    basic_salary = int(input())
    if basic_salary < 1500:
        hra = (basic_salary*10)/100
        da = (basic_salary*90)/100
    else:
        hra = 500
        da = (basic_salary*98)/100
    print(basic_salary+hra+da)