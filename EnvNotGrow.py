"""
Snake Eater Environment
Made with PyGame
Last modification in April 2024 by José Luis Perán
Machine Learning Classes - University Carlos III of Madrid
"""
import numpy as np
import random

class SnakeGameEnv:
    def __init__(self, frame_size_x=150, frame_size_y=150, growing_body=True):
        # Initializes the environment with default values
        self.frame_size_x = frame_size_x
        self.frame_size_y = frame_size_y
        self.growing_body = growing_body
        self.reset()

    def reset(self):
        # Resets the environment with default values
        self.snake_pos = [50, 50]
        self.snake_body = [[50, 50], [60, 50], [70, 50]]
        self.food_pos = [random.randrange(1, (self.frame_size_x // 10)) * 10, random.randrange(1, (self.frame_size_y // 10)) * 10]
        self.food_spawn = True
        self.direction = 'RIGHT'
        self.score = 0
        self.game_over = False
        return self.get_state()

    def step(self, action):
        # Implements the logic to change the snake's direction based on action
        # Update the snake's head position based on the direction
        # Check for collision with food, walls, or self
        # Update the score and reset food as necessary
        # Determine if the game is over
        self.update_snake_position(action)
        reward = self.calculate_reward()
        self.update_food_position()
        state = self.get_state()
        self.game_over = self.check_game_over()
        return state, reward, self.game_over

    def collision(self, direction):

        head_x, head_y = self.snake_pos
        next_move = [head_x, head_y]

        # To do so we need to know the next position in which the head will be to avoid it
        if direction == "RIGHT":
            next_move = [head_x + 10, head_y]
        elif direction == "LEFT":
            next_move = [head_x - 10, head_y]
        elif direction == "DOWN":
            next_move = [head_x, head_y + 10]
        elif direction == "UP":
            next_move = [head_x, head_y - 10]

        # Once having calculated the next move we need to check collision with border
        if (next_move[0] == 0) or (next_move[0] == self.frame_size_x) or (next_move[1] == 0) or (
                next_move[1] == self.frame_size_y):
            return True

        # Now check collision with itself
        elif next_move in self.snake_body:
            return True

        return False

    def get_state(self):
        dx = abs(self.food_pos[0] - self.snake_pos[0])
        dy = abs(self.food_pos[1] - self.snake_pos[1])
        state = 0
        if self.direction == "RIGHT":
                if self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx > dy:
                    state = 0
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx > dy:
                    state = 1
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx > dy:
                    state = 2
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx > dy:
                    state = 3
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] == self.food_pos[1] and dx > dy:
                    state = 4
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] == self.food_pos[1] and dx > dy:
                    state = 5
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                    state = 6
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                    state = 7
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                    state = 8
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                    state = 9
                elif self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                    state = 10
                elif self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                    state = 11
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx == dy:
                    state = 12
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx == dy:
                    state = 13
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx == dy:
                    state = 14
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx == dy:
                    state = 15
        elif self.direction == "LEFT":
                if self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx > dy:
                    state = 16
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx > dy:
                    state = 17
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx > dy:
                    state = 18
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx > dy:
                    state = 19
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] == self.food_pos[1] and dx > dy:
                    state = 20
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] == self.food_pos[1] and dx > dy:
                    state = 21
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                    state = 22
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                    state = 23
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                    state = 24
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                    state = 25
                if self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                    state = 26
                elif self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                    state = 27
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx == dy:
                    state = 28
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx == dy:
                    state = 29
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx == dy:
                    state = 30
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx == dy:
                    state = 31
        elif self.direction == "DOWN":
                if self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx > dy:
                    state = 32
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx > dy:
                    state = 33
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx > dy:
                    state = 34
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx > dy:
                    state = 35
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] == self.food_pos[1] and dx > dy:
                    state = 36
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] == self.food_pos[1] and dx > dy:
                    state = 37
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                    state = 38
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                    state = 39
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                    state = 40
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                    state = 41
                elif self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                    state = 42
                elif self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                    state = 43
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx == dy:
                    state = 44
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx == dy:
                    state = 45
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx == dy:
                    state = 46
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx == dy:
                    state = 47
        elif self.direction == "UP":
                if self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx > dy:
                    state = 48
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx > dy:
                    state = 49
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx > dy:
                    state = 50
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx > dy:
                    state = 51
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] == self.food_pos[1] and dx > dy:
                    state = 52
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] == self.food_pos[1] and dx > dy:
                    state = 53
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                    state = 54
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                    state = 55
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                    state = 56
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                    state = 57
                elif self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                    state = 58
                elif self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                    state = 59
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx == dy:
                    state = 60
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx == dy:
                    state = 61
                elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx == dy:
                    state = 62
                elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx == dy:
                    state = 63
        return state

    def get_body(self):
        return self.snake_body

    def get_food(self):
        return self.food_pos

    def calculate_reward(self):

        if self.check_game_over():
            reward = -200
        elif self.snake_pos == self.food_pos:
            reward = 300
        elif self.direction == "UP" and self.food_pos[1] > self.snake_pos[1]:
            reward = -5
        elif self.direction == "DOWN" and self.food_pos[1] < self.snake_pos[1]:
            reward = -5
        elif self.direction == "RIGHT" and self.food_pos[0] < self.snake_pos[0]:
            reward = -5
        elif self.direction == "LEFT" and self.food_pos[0] > self.snake_pos[0]:
            reward = -5
        else:
            reward = -2
        return reward
        
    def check_game_over(self):
        # Return True if the game is over, else False
        if self.snake_pos[0] < 0 or self.snake_pos[0] > self.frame_size_x-10:
            return True
        if self.snake_pos[1] < 0 or self.snake_pos[1] > self.frame_size_y-10:
            return True
        for block in self.snake_body[1:]:
            if self.snake_pos[0] == block[0] and self.snake_pos[1] == block[1]:
                return True
                
        return False

    def update_snake_position(self, action):
        # Updates the snake's position based on the action
        # Map action to direction
        change_to = ''
        direction = self.direction
        if action == 0:
            change_to = 'UP'
        elif action == 1:
            change_to = 'DOWN'
        elif action == 2:
            change_to = 'LEFT'
        elif action == 3:
            change_to = 'RIGHT'
    
        # Move the snake
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
    
        if direction == 'UP':
            self.snake_pos[1] -= 10
        elif direction == 'DOWN':
            self.snake_pos[1] += 10
        elif direction == 'LEFT':
            self.snake_pos[0] -= 10
        elif direction == 'RIGHT':
            self.snake_pos[0] += 10
            
        self.direction = direction
        
        
        self.snake_body.insert(0, list(self.snake_pos))
        
        if self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] == self.food_pos[1]:
            self.score += 10
            self.food_spawn = False
            # If the snake is not growing
            if not self.growing_body:
                self.snake_body.pop()
        else:
            self.snake_body.pop()
    
    def update_food_position(self):
        if not self.food_spawn:
            self.food_pos = [random.randrange(1, (self.frame_size_x//10)) * 10, random.randrange(1, (self.frame_size_x//10)) * 10]
        self.food_spawn = True


        
