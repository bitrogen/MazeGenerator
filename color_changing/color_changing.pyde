    
xaxis = 0
yaxis = 0
changex = 1
changey = 1
c = 0
frame = 0
def setup():
    fullScreen()
    background(20,25,33)
    colorMode(HSB, 360, 100, 100)
    

def draw():
    global xaxis, yaxis, changex, changey, c, frame 
    
    stroke(c,80,100)
    fill(c, 85, 70)
    c += 1
    frame += 1
    c = c % 360
    square(xaxis,yaxis, 30)
    saveFrame("frames/frame-{}.png".format(frame))
    xaxis += changex
    yaxis += changey
    if xaxis + 30  == width or xaxis == 0:
        changex = -changex
        
    if yaxis + 30  == height or yaxis == 0:
        changey = -changey
        
    
