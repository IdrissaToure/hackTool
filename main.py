#Genere une adrsse IP
part1=0
Max=255
listip =[]
while(part1<Max):
    part1+=1
    part2=0
    while(part2<Max):
        part2+=1
        ip="{}.{}.{}.{}".format(part1,part2,0,0)
        part3=0
        while(part3<Max):
            part3+=1
            ip="{}.{}.{}.{}".format(part1,part2,part3,0,0)
            print(ip)
            listip.append(ip)
              
 
