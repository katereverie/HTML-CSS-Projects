import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for color, count in kwargs.items():
      self.contents.extend([color] * count)

  def draw(self, num_balls_to_draw):
    if num_balls_to_draw > len(self.contents):
      return self.contents
    balls_drawn = []
    for i in range(num_balls_to_draw):
      ball_index = random.randint(0, len(self.contents) - 1)
      balls_drawn.append(self.contents.pop(ball_index))
    return balls_drawn
      # 查阅一下这一块的functions

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  num_success = 0
  # 每抽到期待的颜色的球, 则加一.
  # 比如 期待抽到的球是: 至少两个红色球和一个绿色球
  # 那么每抽到一次红色球, 则在红色球的字典中加1, 同理绿色球.

  for i in range(num_experiments): 
    hat_copy = copy.deepcopy(hat)
    balls_drawn = hat_copy.draw(num_balls_drawn)
    success = True
    for color, count in expected_balls.items():
      if balls_drawn.count(color) < count:
        success = False
        break  
    if success:
      num_success += 1  
  return num_success / num_experiments