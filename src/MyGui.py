import pygame
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from pygame.constants import RESIZABLE
import math
pygame.font.init()
FONT=pygame.font.SysFont("Ariel",20)
pygame.init()
screen=pygame.display.set_mode((700,500),flags=pygame.constants.RESIZABLE)
def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """
    return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen
min_x=min_y=max_x=max_y=0
def min_max(g:DiGraph):
    global min_x,min_y,max_x,max_y
    min_x = min(list(g.listNode.values()), key=lambda n: n.pos[0]).pos[0]
    min_y = min(list(g.listNode.values()), key=lambda n: n.pos[1]).pos[1]
    max_x = max(list(g.listNode.values()), key=lambda n: n.pos[0]).pos[0]
    max_y = max(list(g.listNode.values()), key=lambda n: n.pos[1]).pos[1]
def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)

def draw(g:DiGraph):
     pygame.draw.rect(screen,button.color,button.rect)
     button_txt=FONT.render(button.txt,True,(0,0,0))
     screen.blit(button_txt,(button.rect.x,button.rect.y))
     for i in g.listNode.values():
         x = my_scale(i.pos[0], x=True)
         y = my_scale(i.pos[1], y=True)
         txt=FONT.render((str(i.id)),True,(0,0,255))
         if i.id in ans:
          pygame.draw.circle(screen,(150, 40, 150),(x,y),radius=8)
         else:
             pygame.draw.circle(screen, (200, 200, 0), (x, y), radius=8)
         screen.blit(txt, (x-10, y-10))
         for j in g.listNode[i.id].edgeout.keys():
              pp=g.listNode.get(j)
              xx = my_scale(pp.pos[0], x=True)
              yy = my_scale(pp.pos[1], y=True)
              arrow((x, y), (xx, yy), 17, 5, color=(0, 0, 0))

class Button:
    def __init__(self, rect: pygame.Rect, color,txt,fun=None):
        self.color = color
        self.txt = txt
        self.fun = fun
        self.rect = rect
        self.isClicked = False
    def press(self):
        self.isClicked = not self.isClicked

button = Button(pygame.Rect((0,0),(50,20)),(200,200,0),"center")

def shortP():
    a=g.shortest_path()
    return a
class NodeScr:
    def __init__(self,rect:pygame.Rect,id):
        self.id=id
        self.rect=rect


def arrow(start, end, d, h, color):
    dx = float(end[0] - start[0])
    dy = float(end[1] - start[1])
    D = float(math.sqrt(dx * dx + dy * dy))
    xm = float(D - d)
    xn = float(xm)
    ym = float(h)
    yn = -h
    sin = dy / D
    cos = dx / D
    x = xm * cos - ym * sin + start[0]
    ym = xm * sin + ym * cos + start[1]
    xm = x
    x = xn * cos - yn * sin + start[0]
    yn = xn * sin + yn * cos + start[1]
    xn = x
    points = [(end[0], end[1]), (int(xm), int(ym)), (int(xn), int(yn))]

    pygame.draw.line(screen, color, start, end, width=4)
    pygame.draw.polygon(screen, color, points)
ans=[]
def onClicked(b:Button):
    global  ans
    ans.append(b.fun()[0])

def display(g:GraphAlgo=None):
    button.fun = g.centerPoint
    min_max(g.Graph)
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):
                    button.press()
                    if button.isClicked:
                       onClicked(button)
                    else:
                        ans.clear()

        screen.fill((255,255,255))
        draw(g.Graph)
        pygame.display.update()

if __name__ == '__main__':
    g=GraphAlgo()
    #Enter the address of the e-file
    g.load_from_json("C:\\Users\\USER\\PycharmProjects\\Ex3M\\data\\A0.json")
    display(g)