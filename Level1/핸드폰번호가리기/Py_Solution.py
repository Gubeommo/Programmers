def solution(phone_number):
    temp=''
    for i in range(len(phone_number)-4):
        temp +='*'
    temp += phone_number[-4:]     
    return temp