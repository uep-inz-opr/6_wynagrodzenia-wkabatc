class Pracownik:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

def wynagrodzenie(salary):
    insE = round(salary * 0.0976, 2)
    insR = round(salary * 0.015, 2)
    insC = round(salary * 0.0245, 2)
    c = round(insE + insR + insC, 2)
    d = salary - c
    e = round(d * 0.09, 2)
    f = round(d * 0.0775, 2)
    g = 111.25
    h = round(salary - g - c)
    i = round((h * 0.18) - 46.33, 2)
    j = round(i - f)
    k = round(salary - c - e - j, 2)
    return k

def skladki(salary):
    contrE = round(salary * 0.0976, 2)
    contrR = round(salary * 0.065, 2)
    contrW = round(salary * 0.0193, 2)
    contrFP = round(salary * 0.0245, 2)
    contrFGSP = round(salary * 0.001, 2)
    contrSum = contrE + contrR + contrW + contrFP + contrFGSP
    return contrSum

n = int(input())
emps = []
emp = Pracownik(name = 'Wojciech', salary = 7)

for num in range(n):
    empInput = list(map(str, input().split()))
    emps.append(Pracownik(name = empInput[0], salary = float(empInput[1])))

employerCost = 0

for e in emps:
    salNetto = wynagrodzenie(e.salary)
    contr = skladki(e.salary)
    totalCost = e.salary + contr
    employerCost += totalCost
    result = e.name + ' ' + '{:.2f}'.format(salNetto) + ' ' + '{:.2f}'.format(contr) + ' ' + '{:.2f}'.format(totalCost)
    print(result)

print(employerCost)