from pygame import*
window = display.set_mode((700, 500))
display.set_caption("First project")
height = 60
width = 40
x = 5
y = 500 - height - 5
draw.rect(window, (0,0,255), (x, y, width, height))

run = True
while run:
    #loop runs every 0.1 second
    time.delay(50)
    for e in event.get():
        if e.type == KEYDOWN:
        #check which button is pressed
            if e.key == K_LEFT:
                print("left")
            elif e.key == K_RIGHT:
                print("right")
            elif e.key == K_UP:
                print("up")
            elif e.key == K_DOWN:
                print("down")
        if e.type == QUIT:
            quit()
display.update()
time.delay(5000)