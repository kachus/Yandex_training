max_number=int(input())
set_numbers=set()

guess=input()
for i in range(1,max_number+1):
    set_numbers.add(i)
while guess!='HELP':
    answer=input()
    if answer=='YES':
        guess=set(list(map(int,guess.split())))
        set_numbers=set_numbers.intersection(guess)
        guess=input()
    if answer=='NO':
        guess=set(list(map(int,guess.split())))
        set_numbers.difference_update(guess)
        guess=input()

print(*set_numbers)