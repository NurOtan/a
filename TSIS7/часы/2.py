import pygame
import math
from datetime import datetime
pygame.init()
size=(700,700)
width,hight=350,350
screen=pygame.display.set_mode(size)
font=pygame.font.SysFont("comicsansms",50)
clock60=dict(zip(range(60),range(0,360,6)))
clock12=dict(zip(range(1,13),range(30,390,30)))

def print_text(text,possition):
    surface=font.render(text,True,(255,0,0))
    screen.blit(surface,possition)
def get_cloack_pos(time,radius):
    x=(math.sin(math.radians(clock60[time])-math.pi/2)*radius)+width
    y=(math.cos(math.radians(clock60[time])-math.pi/2)*radius)+hight
    return y,x
def get_cloack_pos3(time,radius):
    x=(math.sin(math.radians(clock60[time])-math.pi/2)*radius)+width
    y=(math.cos(math.radians(clock60[time])-math.pi/2)*radius)+hight
    return y-5,x-55
def get_cloack_pos2(time,radius):
    x=math.sin(math.radians(clock12[time])-math.pi/2)*radius
    y=math.cos(math.radians(clock12[time])-math.pi/2)*radius
    return y+335,x+320
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            quit()
    t=datetime.now()
    
    hour,minute,sec=t.hour,t.minute,t.second
    
    time_now=font.render(f"{t:%H:%M:%S}",1,pygame.Color("red"),pygame.Color("green"))
    time12=font.render("12",1,pygame.Color("red"),pygame.Color("green"))
    screen.fill(pygame.Color('black'))
    for i in range(1,13):
        print_text(str(i),get_cloack_pos2(i,260))
    for i in range(60):
        if i%5!=0:
            print_text(".",get_cloack_pos3(i,270))
    circle=pygame.draw.circle(screen,(0,250,250),(350,350),300,4)
    pygame.draw.circle(screen,"white",(350,350),10,5)
    second_line=pygame.draw.line(screen,pygame.Color("white"),(width,hight),(get_cloack_pos(sec,250)),3)
    minute_line=pygame.draw.line(screen,pygame.Color("red"),(width,hight),(get_cloack_pos(minute,200)),5)
    hour_line=pygame.draw.line(screen,pygame.Color("green"),(width,hight),(get_cloack_pos(((hour%12)*5+minute//12)%60,150)),10)
    screen.blit(time_now,(10,10))
    
    
    
   
    
    pygame.display.update()
    