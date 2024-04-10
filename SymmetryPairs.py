pairs=[tuple(map(int,pair.split())) for pair in input().split(",")]
for (x,y) in pairs:
    if (y,x) in pairs:
        print((x,y))


#not solved completely

