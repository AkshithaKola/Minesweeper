import pygame
import random
from pygame.locals import*

global grid_size,mines_count,width,height,cell_size
grid_size=10
width=600
height=600
cell_size=width//grid_size
mines_count=10

blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
gray=(200,200,200)
light_blue=(87, 87, 255)
gradient_blue=(99, 119, 243)
dark_gray=(180,180,180)
g=(150,150,150)


pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("MINESWEEPER")

mine_img=pygame.image.load("mine.png")
mine_img=pygame.transform.scale(mine_img,(cell_size-1,cell_size-1))
flag_img=pygame.image.load("flag.png")
flag_img=pygame.transform.scale(flag_img,(cell_size-1,cell_size-1))

font = pygame.font.Font(None, 30)

global grid
global flags
global opened
global mines 

game_over=False
game_running=True

def reset_game():
    global grid,flags,opened,mines,checking
    opened=[[False for _ in range(grid_size)] for _ in range(grid_size)]
    checking=[[False for _ in range(grid_size)] for _ in range(grid_size)]
    flags=[[False for _ in range(grid_size)] for _ in range(grid_size)]  
    for mine in mines:
      row=mine//grid_size
      col=mine%grid_size
      checking[row][col]=True
def new_game():
    global grid,flags,opened,mines,checking
    grid=[[0 for _ in range(grid_size)] for _ in range(grid_size)]
    flags=[[False for _ in range(grid_size)] for _ in range(grid_size)]
    opened=[[False for _ in range(grid_size)] for _ in range(grid_size)]
    checking=[[False for _ in range(grid_size)] for _ in range(grid_size)]
    mines=random.sample(range(grid_size*grid_size),mines_count)
    for mine in mines:
      row=mine//grid_size
      col=mine%grid_size
      grid[row][col]=-1
      checking[row][col]=True
    for row in range(grid_size):
        for col in range(grid_size):
            if grid[row][col] == -1:
                continue
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= row + i < grid_size and 0 <= col + j < grid_size:
                        if grid[row + i][col + j] == -1:
                            count += 1
            grid[row][col] = count

new_game()            
while game_running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if game_over:
                replay_rect = pygame.Rect(200,175,200,50)
                new_game_rect=pygame.Rect(200,250,200,50)
                exit_rect=pygame.Rect(200,325,200,50)
                if replay_rect.collidepoint(event.pos):
                    pygame.event.clear()
                    reset_game()
                    game_over=False
                if new_game_rect.collidepoint(event.pos):
                    pygame.event.clear()
                    new_game()
                    game_over=False
                if exit_rect.collidepoint(event.pos):
                    running=False
                    pygame.quit()
                    exit()
            elif all(checking[r][c] for r in range(grid_size) for c in range(grid_size)):
                new_game_rect=pygame.Rect(200,250,200,50)
                exit_rect=pygame.Rect(200,325,200,50)
                if new_game_rect.collidepoint(event.pos):
                    pygame.event.clear()
                    new_game()
                    game_over=False
                if exit_rect.collidepoint(event.pos):
                    running=False
                    pygame.quit()
                    exit()      
            else:
                mouse_x,mouse_y=event.pos
                row=mouse_y//cell_size
                col=mouse_x//cell_size
                if event.button==1:
                    if not flags[row][col]:
                        opened[row][col]=True
                        checking[row][col]=True
                        if grid[row][col]==-1:
                            game_over=True
                        elif grid[row][col]==0:
                            stack=[(row,col)]
                            while stack:
                                r,c=stack.pop()
                                count=0
                                for i in range(-1,2):
                                    for j in range(-1,2):
                                        if 0<=r+i<grid_size and 0<=c+j<grid_size and not opened[r+i][c+j]:
                                            opened[r+i][c+j]=True
                                            checking[r+i][c+j]=True
                                            if grid[r+i][c+j]==0:
                                                stack.append((r+i,c+j))
                elif event.button==3:
                    flags[row][col] = not flags[row][col]

    screen.fill(light_blue)
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, black, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, black, (0, y), (width, y))     

    for row in range(grid_size):
        for col in range(grid_size):
            if opened[row][col]:
                cell_value = grid[row][col]
                cell_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, gray, cell_rect)
                if cell_value == -1:
                    screen.blit(mine_img, cell_rect)
                elif cell_value > 0:
                    text = font.render(str(cell_value), True, black)
                    text_rect = text.get_rect(center=cell_rect.center)
                    screen.blit(text, text_rect)   
    for row in range(grid_size):
        for col in range(grid_size):
            if flags[row][col]:
                cell_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                screen.blit(flag_img, cell_rect)


    if game_over:
        background_copy = screen.copy()
        blur_multiplier = 0.1
        scaled_width = int(width * blur_multiplier)
        scaled_height = int(height * blur_multiplier)
        scaled_background = pygame.transform.smoothscale(background_copy, (scaled_width, scaled_height))
        blurred_background = pygame.transform.smoothscale(scaled_background, (width, height))
        screen.blit(blurred_background, (0, 0))
        text = font.render("You lost!", True, black)
        text_rect = text.get_rect(center=(width // 2,150))
        box_rect = pygame.Rect(150, 125, 300, 275)
        replay_text = font.render("Replay", True, black)
        replay_rect = pygame.Rect(200,175,200,50)
        replay_text_rect=text.get_rect(center=replay_rect.center)
        new_game_text = font.render("New Game", True, black)
        new_game_rect = pygame.Rect(200,250,200,50)
        new_game_text_rect=text.get_rect(center=new_game_rect.center)
        exit_game_text = font.render("Exit", True, black)
        exit_game_rect = pygame.Rect(200,325,200,50)
        exit_game_text_rect=text.get_rect(center=exit_game_rect.center)
        pygame.draw.rect(screen, dark_gray, box_rect)
        pygame.draw.rect(screen, black, box_rect, 2)
        screen.blit(text, text_rect)
        pygame.draw.rect(screen,g,replay_rect)
        pygame.draw.rect(screen, black, replay_rect, 2)
        screen.blit(replay_text, replay_text_rect)
        pygame.draw.rect(screen,g,new_game_rect)
        pygame.draw.rect(screen, black, new_game_rect, 2)
        screen.blit(new_game_text, new_game_text_rect)
        pygame.draw.rect(screen,g,exit_game_rect)
        pygame.draw.rect(screen, black, exit_game_rect, 2)
        screen.blit(exit_game_text, exit_game_text_rect)

    elif all(checking[r][c] for r in range(grid_size) for c in range(grid_size)):
        background_copy = screen.copy()
        blur_multiplier = 0.1
        scaled_width = int(width * blur_multiplier)
        scaled_height = int(height * blur_multiplier)
        scaled_background = pygame.transform.smoothscale(background_copy, (scaled_width, scaled_height))
        blurred_background = pygame.transform.smoothscale(scaled_background, (width, height))
        screen.blit(blurred_background, (0, 0))
        text = font.render("You Won!", True, black)
        text_rect = text.get_rect(center=(width // 2,225 ))
        box_rect = pygame.Rect(150, 200, 300, 200)
        new_game_text = font.render("New Game", True, black)
        new_game_rect = pygame.Rect(200,250,200,50)
        new_game_text_rect=text.get_rect(center=new_game_rect.center)
        exit_game_text = font.render("Exit", True, black)
        exit_game_rect = pygame.Rect(200,325,200,50)
        exit_game_text_rect=text.get_rect(center=exit_game_rect.center)
        pygame.draw.rect(screen, dark_gray, box_rect)
        pygame.draw.rect(screen, black, box_rect, 2)
        screen.blit(text, text_rect)
        pygame.draw.rect(screen,g,new_game_rect)
        pygame.draw.rect(screen, black, new_game_rect, 2)
        screen.blit(new_game_text, new_game_text_rect)
        pygame.draw.rect(screen,g,exit_game_rect)
        pygame.draw.rect(screen, black, exit_game_rect, 2)
        screen.blit(exit_game_text, exit_game_text_rect)
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()                    
                  
