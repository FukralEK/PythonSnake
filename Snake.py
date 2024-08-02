import pygame
import sys
import random

class Vector:
  def __init__(self, x,y):
    self.x = x
    self.y = y
  def __add__(self, other):
    if isinstance(other, Vector):
        return Vector(self.x + other.x, self.y + other.y)
    return NotImplemented
  def __eq__(self, other):
    if self.x == other.x and self.y == other.y:
      return True
    return False
  def __ne__(self, other):
    if self.x == other.x and self.y == other.y:
      return False
    return True

class PressedKeys:
  def __init__(self):
    self.isUp = False
    self.isDown = False
    self.isRight = False
    self.isLeft = False

pressedKeys = PressedKeys()

screenWidth = 1280
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))

clock = pygame.time.Clock()

snake = []

fruit = Vector(0,0)
direction = Vector(0,0)

def repositionFruit():
  fruit.x = random.randint(0, 48)
  fruit.y = random.randint(0, 23)

def renderSnake():
  for snakePosition in snake:
    pygame.draw.rect(screen, (0,255,0),(snakePosition.x*25,snakePosition.y*25,25,25))

def moveSnake():
  if pressedKeys.isUp:
    if direction != Vector(0,1):
      direction.x = 0
      direction.y = -1
  elif pressedKeys.isDown:
    if direction != Vector(0,-1):
      direction.x = 0
      direction.y = 1
  elif pressedKeys.isLeft:
    if direction != Vector(1, 0):
      direction.x = -1
      direction.y = 0
  elif pressedKeys.isRight:
    if direction != Vector(-1, 0):
      direction.x = 1
      direction.y = 0

  for index in range(len(snake) - 1, 0, -1):
    snake[index] = snake[index - 1]

  snake[0] = snake[0] + direction
  
def renderFruit():
  pygame.draw.rect(screen, (255,0,0), (fruit.x*25, fruit.y*25, 25, 25))

def restart():
  repositionFruit()
  snake.clear()
  snake.append(Vector(25, 12))
  pressedKeys.isUp = False
  pressedKeys.isDown = False
  pressedKeys.isRight = False
  pressedKeys.isLeft = False

def setInput(event):
  if event.type == pygame.KEYUP:
    if event.key == pygame.K_F2:
      restart()
    elif event.key == pygame.K_w:
      pressedKeys.isUp = False
    elif event.key == pygame.K_s:
      pressedKeys.isDown = False
    elif event.key == pygame.K_a:
      pressedKeys.isLeft = False
    elif event.key == pygame.K_d:
      pressedKeys.isRight = False
  elif event.type == pygame.KEYDOWN:
    if event.key == pygame.K_w:
      pressedKeys.isUp = True
    elif event.key == pygame.K_s:
      pressedKeys.isDown = True
    elif event.key == pygame.K_a:
      pressedKeys.isLeft = True
    elif event.key == pygame.K_d:
      pressedKeys.isRight = True

def checkFruitAndSnake(lastSnakePosition):
  if snake[0] == fruit:
    repositionFruit()
    snake.append(lastSnakePosition)

def checkIfTheMotherfuckersDead():
  for index in range(1, len(snake), +1):
    if snake[0] == snake[index]:
      restart()

restart()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    else: setInput(event)

  screen.fill((0,0,0))

  lastSnakePosition = snake[0]

  moveSnake()

  checkFruitAndSnake(lastSnakePosition)

  renderSnake()

  renderFruit()

  checkIfTheMotherfuckersDead()

  pygame.display.flip()

  clock.tick(10)

pygame.quit()
sys.exit()
