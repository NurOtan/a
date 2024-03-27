import pygame as pg
pg.init()
screen=pg.display.set_mode((800,800))
window_title=pg.display.set_caption("Football")
center=(400,400)
cloclk=pg.time.Clock()
x,y=400,400
direction_x=1
direction_y=1

moving_up=False
moving_down=False
moving_right=False
moving_left=False

Moving_count_up=20
Moving_count_down=20
Moving_count_left=20
Moving_count_right=20
while True:
    for event in pg.event.get():
        if event.type ==pg.QUIT:
            quit()
    keys=pg.key.get_pressed()
    if not moving_up:
        if keys[pg.K_UP] and y>100:
            moving_up=True
    else:
        if Moving_count_up>=0:
            
            y-=1
            Moving_count_up-=1
        else:
            moving_up=False
            Moving_count_up=20
            
    if not moving_down:
        if keys[pg.K_DOWN] and y<700:
            moving_down=True
    else:
        if Moving_count_down>=0:
            
            y+=1
            Moving_count_down-=1
        else:
            moving_down=False
            Moving_count_down=20
            
    if not moving_left:
        if keys[pg.K_LEFT] and x>100:
            moving_left=True
    else:
        if Moving_count_left>=0:
            
            x-=1
            Moving_count_left-=1
        else:
            moving_left=False
            Moving_count_left=20
    if not moving_right:
        if keys[pg.K_RIGHT] and x<700:
            moving_right=True
    else:
        if Moving_count_right>=0:
            
            x+=1
            Moving_count_right-=1
        else:
            moving_right=False
            Moving_count_right=20
            

            
        
  
    screen.fill((255,255,255))
    red_ball=pg.draw.circle(screen,"red",(x,y),25)
    granisa=pg.draw.rect(screen,"red",(60,60,680,680),1)
    cloclk.tick(60)

    pg.display.update()
    