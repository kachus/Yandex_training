task_completion_code=int(input())
inter_verdict=int(input())
check_verdict=int(input())
final_verd=''
if -128<=task_completion_code<=127 and 0<=inter_verdict<=7 and 0<=check_verdict<=7:
    if inter_verdict==0:
        if task_completion_code!=0:
            final_verd=3
        else:
            final_verd=check_verdict
    if inter_verdict==1:
        final_verd=check_verdict
    if inter_verdict==4:
        if task_completion_code!=0:
            final_verd=3
        else:
            final_verd=4
    if inter_verdict==6:
        final_verd=0
    if inter_verdict==7:
        final_verd=1
    if final_verd=='':
        final_verd=check_verdict
    print(final_verd)
