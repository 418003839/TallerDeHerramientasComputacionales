def diana(x,y):
    if x<5 and y<10:
        return(3)
    if x>=5 and x<25 and y<10:
        return(7)
    if x>25 and y<10:
        return(10)
    if x<5 and y>=10 and y<30:
        return(5)
    if x<5 and y>30:
        return(3)
    if x<25 and y>=10 and y<30:
        return(10)
    if x<25 and y>30:
        return(7)
    if x>25 and y>=10 and y>30:
        return(5)
    if x>25 and y>30:
        return(30)
    
