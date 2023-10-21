import pygame
import random
import map

#初始化地图数据
map.create_map_queue()

#方块的数据
data=[]
def main():
    # 初始化 Pygame
    pygame.init()

    # 游戏区域的大小
    WIDTH, HEIGHT = 300, 300
    GAME_AREA = pygame.Rect(50, 0, WIDTH, HEIGHT)

    # 方块大小和颜色
    BLOCK_SIZE = 30
    BG_COLOR = (40, 40, 60)  # 背景色
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLACK=(0,0,0)

    # 定义俄罗斯方块的形状
    SHAPES = [
        [[1, 1, 1, 1]],
        [[1, 1], [1, 1]],
        [[1, 1, 0], [0, 1, 1]],
        [[0, 1, 1], [1, 1, 0]],
        [[1, 1, 1], [0, 1, 0]],
        [[1, 1, 1], [1, 0, 0]],
        [[1, 1, 1], [0, 0, 1]]
    ]



    # 初始化 Pygame 窗口
    screen = pygame.display.set_mode((WIDTH + 150, HEIGHT))
    pygame.display.set_caption("Tetris Game")

    # 创建一个时钟对象来控制游戏速度
    clock = pygame.time.Clock()

    # 初始化游戏区域
    #game_area = [[0] * (WIDTH // BLOCK_SIZE) for _ in range(HEIGHT // BLOCK_SIZE)]
    game_area = map.map_queue[0]
    # 初始化当前方块的位置和形状
    current_shape = random.choice(SHAPES)
    current_row = 0
    current_col = (len(game_area[0]) - len(current_shape[0])) // 2

    # 游戏循环
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_col -= 1
                elif event.key == pygame.K_RIGHT:
                    current_col += 1
                elif event.key == pygame.K_DOWN:
                    current_row += 1
                elif event.key == pygame.K_UP:
                    current_row -= 1
                elif event.key == pygame.K_SPACE:
                    current_shape = rotate(current_shape)
                elif event.key == pygame.K_RETURN:
                    flag=1
                    for x,y in data:
                        if game_area[x][y]==-1:
                            flag=0
                    if flag==1:
                        for x,y in data:
                            game_area[x][y]+=1
                        # 生成新的方块
                        current_shape = random.choice(SHAPES)
                        current_row = 0
                        current_col = (len(game_area[0]) - len(current_shape[0])) // 2

        # 绘制游戏区域
        for r, row in enumerate(game_area):
            for c, val in enumerate(row):
                if val == -1:
                    pygame.draw.rect(screen, BG_COLOR,
                                     pygame.Rect(c * BLOCK_SIZE, r * BLOCK_SIZE,
                                                 BLOCK_SIZE,
                                                 BLOCK_SIZE))
                if val == 0:
                    pygame.draw.rect(screen, BLACK,
                                     pygame.Rect(c * BLOCK_SIZE, r * BLOCK_SIZE,
                                                 BLOCK_SIZE,
                                                 BLOCK_SIZE))
                if val >0:
                    pygame.draw.rect(screen, BLUE,
                                     pygame.Rect(c * BLOCK_SIZE, r * BLOCK_SIZE,
                                                 BLOCK_SIZE,
                                                 BLOCK_SIZE))



        data.clear()
        # 绘制当前方块
        for r, row in enumerate(current_shape):
            for c,val in enumerate(row):
                if val:
                    pygame.draw.rect(screen,BLUE,
                                     pygame.Rect((current_col+c)*BLOCK_SIZE,(current_row+r)*BLOCK_SIZE,
                                                 BLOCK_SIZE,
                                                 BLOCK_SIZE))
                    if len(data)<=4:
                        data.append((current_row+r,current_col+c))

        # 画网格线 竖线
        for x in range(WIDTH//BLOCK_SIZE):
            pygame.draw.line(screen, (0, 0, 0), (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, HEIGHT), 1)

        # 画网格线 横线
        for y in range(HEIGHT//BLOCK_SIZE):
            pygame.draw.line(screen, (0, 0, 0), (0, y * BLOCK_SIZE), (WIDTH//BLOCK_SIZE * BLOCK_SIZE, y * BLOCK_SIZE), 1)
        # 更新屏幕
        pygame.display.flip()

        # 控制游戏速度
        clock.tick(5)

    # 关闭 Pygame
    pygame.quit()

def rotate(shape):
    return [list(row) for row in zip(*shape[::-1])]

if __name__ == "__main__":
    main()