
xpos=0
ypos=0
xpos=0
xVers=+1
yVers=+1
xrac=0
def setup():
    global xpos,ypos
    xpos=10
    ypos=100
    size(800,600)
    background( 5, 5, 5)
    fill(0,255,0)
    rect(20, 20, 100, 200)
    fill(255,255,255)
    rect(120,20,100,200)
    fill(255,000,000)
    rect(220,20,100,200)
    
def draw():
    global xpos,ypos,xVers,yVers, xrac
    background( 5, 5, 5)

    ellipse(xpos,ypos,50,50)
    xpos=xpos+10*xVers
    ypos=ypos+10*yVers
    
    if xpos>width or xpos<0:
        xVers=xVers*(-1)
        fill(random(0,255),random(0,255),random(0,255))

    if ypos>height or ypos<0:
        yVers*=-1
        fill(random(0,255),random(0,255),random(0,255))
        
    rect(xrac,height-25,100,25)
    
def keyPressed():
    global xrac
    if (keyCode==RIGHT and xrac<width-80):
        xrac+=10
    elif (keyCode==LEFT and xrac>0):
        xrac-=10
    

    
    
