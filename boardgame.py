import pygame, sys, random, time

##class Arrow:
##    def __init__(self, dir, place):
##        self.dir = dir
##        self.place = place

##side = 110
##color = [[0 for i in range(7)] for j in range(7)]       # used for color of each grid 
##arrow = [[0 for i in range(7)] for j in range(7)]       # used for direction of arrow in each grid
#0 means red, 1 means blue
def paint():
    screen.fill([255, 255, 255])
##    global r, b
    r = 0
    b = 0
    for x in range(1,8):
        for y in range(1,8):
            squ = [x*side, y*side, side, side]
            pygame.draw.rect(screen, [0, 0, 0], squ, 2)
    pygame.draw.rect(screen, [0, 0, 0], [side, side, side * 7, side * 7], 3)
    for i in range(7):
        for j in range(7):
##            pygame.draw.rect(screen, [255, 255, 255], [(j + 1)*side+2, (i + 1)*side+2, side-3, side-3], 0)
##            pygame.display.flip()
            if color[i][j] == 'r':
                plot = [(j + 1)*side+2, (i + 1)*side+2, side-3, side-3]
                pygame.draw.rect(screen, [255, 0, 0], plot, 0)
                r += 1
            if color[i][j] == 'b':
                plot = [(j + 1)*side+2, (i + 1)*side+2, side-3, side-3]
                pygame.draw.rect(screen, [0, 0, 255], plot, 0)
                b += 1
            if arrow[i][j] == 'up':
                plot = [(j + 1)*side+15, (i + 1)*side+15]
                screen.blit(img_up, plot)
            if arrow[i][j] == 'dw':
                plot = [(j + 1)*side+15, (i + 1)*side+15]
                screen.blit(img_dw, plot)
            if arrow[i][j] == 'lf':
                plot = [(j + 1)*side+15, (i + 1)*side+15]
                screen.blit(img_lf, plot)
            if arrow[i][j] == 'rt':
                plot = [(j + 1)*side+15, (i + 1)*side+15]
                screen.blit(img_rt, plot)
    pygame.draw.rect(screen, [237,125,49], [990, 140, 110, 110], 0)
    pygame.draw.rect(screen, [237,125,49], [butx, buty, butl, buth], 0)
    write('confirm', 100, (0, 0, 0), [1020, 780])
##    write('P1(red)', 50, (0, 0, 0), [110, 50])
##    write('P2(blue)', 50, (0, 0, 0), [740, 50])
##    write('P1(red) score: ' + str(score1), 70, (0, 0, 0), [990, 400])
##    write('P2(blue) score: ' + str(score2), 70, (0, 0, 0), [990, 470])
    write('round    ' + str(round), 70, (0, 0, 0), [1000, 25])          
    write('red ' + str(r), 70, (0, 0, 0), [990, 530])
    write('blue ' + str(b), 70, (0, 0, 0), [990, 600])
    write(str(num), 70, (0, 0, 0), [1200, 160])
##    write('P1 score: ' + str(score1), 70, (0, 0, 0), [990, 400])
##    write('P2 score: ' + str(score2), 70, (0, 0, 0), [990, 470])
    if round + 1 >= end * 4:
        write('Game Over', 100, (255, 0, 0), [310, 20])
    if turn == 0:
        write('-->', 70, (237,125,49),[920, 295])
    else:
        write('-->', 70, (237,125,49),[920, 365])
    if score1 >= score2:
        write('P1(red) score: ' + str(score1), 70, (240, 0, 0), [990, 300])
        write('P2(blue) score: ' + str(score2), 70, (0, 0, 0), [990, 370])
    else:
        write('P1(red) score: ' + str(score1), 70, (0, 0, 0), [990, 300])
        write('P2(blue) score: ' + str(score2), 70, (240, 0, 0), [990, 370])
    pygame.display.flip()
    
##def clean():
##    for x in range(1,8):
##        for y in range(1,8):
##            squ = [x*side, y*side, side, side]
##            pygame.draw.rect(screen, [0, 0, 0], squ, 2)
##    pygame.draw.rect(screen, [0, 0, 0], [side, side, side * 7, side * 7], 3)
##    plot = [4*side+15, 4*side+15]
##    screen.blit(img_up, plot)
##    pygame.display.flip()

def write(text, size, rgb, pos):
    font = pygame.font.Font(None, size)
    surf = font.render(text, 1, rgb)
    screen.blit(surf, pos)
    
def visit(startx, starty, graph, v):
    v[(startx, starty)] = True
    for posx, posy in get_near(startx, starty, graph):
        if (posx, posy) in v: continue
        visit(posx, posy, graph, v)
        
def get_near(locx, locy, graph):
    ans = []
    if graph[locx][locy] == 'r':
        if locx - 1 >= 0:
            if graph[locx - 1][locy] == 'r':
                ans.append([locx - 1, locy])
        if locy - 1 >= 0:
            if graph[locx][locy - 1] == 'r':
                ans.append([locx, locy - 1])
        if locx + 1 <= 6:
            if graph[locx + 1][locy] == 'r':
                ans.append([locx + 1, locy])
        if locy + 1 <= 6:
            if graph[locx][locy + 1] == 'r':
                ans.append([locx, locy + 1])
    elif graph[locx][locy] == 'b':
        if locx - 1 >= 0:
            if graph[locx - 1][locy] == 'b':
                ans.append([locx - 1, locy])
        if locy - 1 >= 0:
            if graph[locx][locy - 1] == 'b':
                ans.append([locx, locy - 1])
        if locx + 1 <= 6:
            if graph[locx + 1][locy] == 'b':
                ans.append([locx + 1, locy])
        if locy + 1 <= 6:
            if graph[locx][locy + 1] == 'b':
                ans.append([locx, locy + 1])
    return ans
    
## 1 means red, 2 means blue
## 0 means up, 90 means right, 180 means down, -90 means left
side = 110
##color = [[0 for i in range(7)] for j in range(7)]       # used for color of each grid 
##arrow = [[0 for i in range(7)] for j in range(7)]       # used for direction of arrow in each grid
##color = [[' ', ' ', ' ', 'r', 'r', 'r', 'b'],
##         ['r', 'r', ' ', ' ', ' ', 'r', 'b'],
##         [' ', ' ', 'b', 'r', ' ', ' ', ' '],
##         ['b', 'b', 'b', 'r', ' ', 'r', 'r'],
##         [' ', ' ', ' ', ' ', 'b', 'w', 'w'],
##         ['r', 'r', ' ', ' ', 'b', ' ', 'r'],
##         [' ', ' ', ' ', 'b', 'b', ' ', 'r']]
##arrow = [['up', 'lf', 'dw','rt',' ',' ', ' '],
##         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
##         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
##         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
##         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
##         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
##         [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
color = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
arrow = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', 'up', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
aposx = 3
aposy = 3
img_up = pygame.image.load("up.png")
img_dw = pygame.image.load("down.png")
img_lf = pygame.image.load("left.png")
img_rt = pygame.image.load("right.png")
pygame.init()
screen = pygame.display.set_mode([1500,950])
screen.fill([255, 255, 255])
##p1_text = 'P1(red)'
##p1_font = pygame.font.Font(None, 50)
##p1_surf = p1_font.render(p1_text, 1, (0, 0, 0))
##p2_text = 'P2(blue)'
##p2_font = pygame.font.Font(None, 50)
##p2_surf = p2_font.render(p2_text, 1, (0, 0, 0))
##screen.blit(p1_surf, [110, 50])
##screen.blit(p2_surf, [740, 50])
dir = ['up', 'rt', 'dw', 'lf']
##squ = [990, 220, 110, 110]
rseq = ['r', ' ', 'b']
bseq = ['b', ' ', 'r']
##cnt = -1
round = 1
end = 15
score1 = 30
score2 = 30
num = random.randint(1,4)
turn = 0
butx = 990
buty = 770
butl = 300
buth = 110
rin = 0
bin = 0
p1prex = -1
p1prey = -1
p2prex = -1
p2prey = -1
paint()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x % side != 0 and y % side != 0 and x > side and x < side * 8 and y > side and y < side * 8:
                row = int(x / side) - 1
                col = int(y / side) - 1
                plot = [(row + 1)*side+2, (col + 1)*side+2, side-3, side-3]
                if arrow[col][row] != ' ':
                    arrow[col][row] = dir[(dir.index(arrow[col][row]) + 1) % 4]
                    paint()
                else:
##                    round += 1
##                    if round + 1 == end * 4:
##                        write('Game Over', 100, (255, 0, 0), [320, 20])
##                        end_text = 'Game Over'
##                        end_font = pygame.font.Font(None, 100)
##                        end_surf = end_font.render(end_text, 1, (255, 0, 0))
##                        screen.blit(end_surf, [320, 20])
##                    cnt += 1
##                    cnt %= 4
##                    paint()
##                    pygame.draw.rect(screen, [255, 255, 255], [980, 25, 100, 100], 0)
##                    write(str(round / 4 + 1), 50, (0, 0, 0), [1000, 50])
##                    r_font = pygame.font.Font(None, 50)
##                    r_surf = r_font.render(str(round / 4 + 1), 1, (0, 0, 0))
##                    screen.blit(r_surf, [1000, 50])
##                    pygame.display.flip()
##                    if cnt <= 1:
##                        color[col][row] = 'r'
##                    else:
##                        color[col][row] = 'b'
                    if turn == 0 :
                        if p1prex == col and p1prey == row:
                            rin += 1
                            rin %= 3
                        else:
                            if color[col][row] == ' ':
                                rin = 0
                            else:
                                rin = (rseq.index(color[col][row]) + 1) % 3
                        color[col][row] = rseq[rin]
                        p1prex = col
                        p1prey = row
                    else:
                        if p2prex == col and p2prey == row:
                            bin += 1
                            bin %= 3
                        else:
                            if color[col][row] == ' ':
                                bin = 0
                            else:
                                bin = (bseq.index(color[col][row]) + 1) % 3
                        color[col][row] = bseq[bin]
                        p2prex = col
                        p2prey = row
                    paint()
##                    pygame.draw.rect(screen, [255, 255, 255], [970, 580, 200, 200], 0)                    
##                    write('red ' + str(r), 70, (0, 0, 0), [990, 600])
##                    write('blue ' + str(b), 70, (0, 0, 0), [990, 670])
                    pygame.display.flip()
                    
            elif x > 990 and x < 1100 and y > 140 and y < 250:
                num = random.randint(1,4)
##                plot_num = [11*side, 2*side, side, side]
                paint()
##                pygame.draw.rect(screen, [255, 255, 255], plot_num, 0)
##                write(str(num), 50, (0, 0, 0), [11 * side, 2 * side + 25])
##                num_font = pygame.font.Font(None, 50)
##                num_surf = num_font.render(str(num), 1, (0, 0, 0))
##                screen.blit(num_surf, [11 * side, 2 * side + 25])
                pygame.display.flip()
##                for i in range(num):
##                    plot_arrow = [(aposy + 1)*side+5, (aposx + 1)*side+5, 100, 100]
##                    pygame.draw.rect(screen, [255, 255, 255], plot_arrow, 0)
##                    pygame.display.flip()
                if arrow[aposx][aposy] == 'up':
                    arrow[aposx][aposy] = ' '
                    if aposx - num >= 0:  aposx -= num
                    else: aposx = aposx + 7 - num
                    arrow[aposx][aposy] = 'up'
##                    paint(color, arrow)
                if arrow[aposx][aposy] == 'rt':
                    arrow[aposx][aposy] = ' '
                    if aposy + num <= 6:  aposy += num
                    else: aposy = aposy - 7 + num
                    arrow[aposx][aposy] = 'rt'
##                    paint(color, arrow)
                if arrow[aposx][aposy] == 'dw':
                    arrow[aposx][aposy] = ' '
                    if aposx + num <= 6:  aposx += num
                    else: aposx = aposx - 7 + num
                    arrow[aposx][aposy] = 'dw'
##                    paint(color, arrow)
                if arrow[aposx][aposy] == 'lf':
                    arrow[aposx][aposy] = ' '
                    if aposy - num >= 0:  aposy -= num
                    else: aposy = aposy + 7 - num
                    arrow[aposx][aposy] = 'lf'
##                    paint(color, arrow)
##                paint()
                if color[aposx][aposy] == 'r':
                    v = {}
                    visit(aposx, aposy, color, v)
                    score1 += len(v)
                    score2 -= len(v)
##                    pygame.draw.rect(screen, [255, 255, 255], [970, 380, 400, 400], 0)
##                    write('P1 score: ' + str(score1), 70, (0, 0, 0), [990, 400])
##                    write('P2 score: ' + str(score2), 70, (0, 0, 0), [990, 470])
##                    pygame.display.flip()
                if color[aposx][aposy] == 'b':
                    v = {}
                    visit(aposx, aposy, color, v)
                    score1 -= len(v)
                    score2 += len(v)
##                    pygame.draw.rect(screen, [255, 255, 255], [970, 380, 400, 400], 0)
##                    write('P1 score: ' + str(score1), 70, (0, 0, 0), [990, 400])
##                    write('P2 score: ' + str(score2), 70, (0, 0, 0), [990, 470])
                paint()
                pygame.display.flip()
            elif x > butx and x < butx + butl and y > buty and y < buty + buth:
                turn += 1
                turn %= 2
                round += 1
                paint()
                
                
