from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
from random import randint

# OLED 
SCREEN_WIDTH = 127#128
SCREEN_HEIGHT = 63#64

# JoyStick引脚定义
j_x = machine.ADC(2)
j_y = machine.ADC(0)

# 初始化I2C总线和OLED显示屏
i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=400000)
oled = SSD1306_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, i2c)

# 游戏界面的参数
pixel_size = 2  # 像素大小
snake_size = 3  # 蛇的初始长度
food_pos = (0, 0)  # 食物的位置

# 初始化贪吃蛇的位置和速度
snake = [(SCREEN_WIDTH // (2 * pixel_size), SCREEN_HEIGHT // (2 * pixel_size))]
snake_direction = (1, 0)  # 贪吃蛇的初始方向

# 游戏状态
game_over = False


def draw_pixel(x, y, color):
    """在屏幕上绘制一个像素"""
    oled.fill_rect(x * pixel_size, y * pixel_size, pixel_size, pixel_size, color)

def generate_food():
    """生成食物的随机位置"""
    global food_pos

    # 在屏幕上随机选择一个位置作为食物的位置
    x = randint(0, SCREEN_WIDTH // pixel_size - 1)
    y = randint(0, SCREEN_HEIGHT // pixel_size - 1)
    food_pos = (x, y)

def move_snake():
    """移动贪吃蛇"""
    global snake_direction, game_over

    # 获取贪吃蛇头部的位置
    head = snake[0]
    x, y = head

    # 根据当前方向计算下一步的位置
    dx, dy = snake_direction
    new_head = (x + dx, y + dy)

    # 检查贪吃蛇是否撞到边界或自身
    if (
        new_head[0] < 0 or
        new_head[0] >= SCREEN_WIDTH // pixel_size or
        new_head[1] < 0 or
        new_head[1] >= SCREEN_HEIGHT // pixel_size or
        new_head in snake
    ):
        game_over = True
        return

    # 在贪吃蛇头部插入新的位置，并移除尾部
    snake.insert(0, new_head)
    if len(snake) > snake_size:
        snake.pop()


def handle_input():
    """处理用户输入"""
    global snake_direction

    # 获取JoyStick的X和Y轴数值
    x_value = j_x.read_u16()
    y_value = j_y.read_u16()

    # 根据JoyStick的数值确定方向
    if x_value < 1000:  # 向左
        snake_direction = (-1, 0)
    elif x_value > 3000:  # 向右
        snake_direction = (1, 0)
    elif y_value < 1000:  # 向上
        snake_direction = (0, -1)
    elif y_value > 3000:  # 向下
        snake_direction = (0, 1)

def draw_game():
    """绘制游戏界面"""
    # 清空屏幕
    oled.fill(0)

    # 绘制贪吃蛇
    for segment in snake:
        x, y = segment
        draw_pixel(x, y, 1)

    # 绘制食物
    food_x, food_y = food_pos
    draw_pixel(food_x, food_y, 1)

    # 更新显示屏
    oled.show()

# 游戏循环
while not game_over:
    handle_input()  # 处理用户输入
    move_snake()  # 移动贪吃蛇
    draw_game()  # 绘制游戏界面
    sleep(0.3)  # 稍微延迟一下，控制游戏速度

