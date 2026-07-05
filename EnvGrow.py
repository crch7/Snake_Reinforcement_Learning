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
        self.food_pos = [random.randrange(1, (self.frame_size_x // 10)) * 10,
                         random.randrange(1, (self.frame_size_y // 10)) * 10]
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
                if not self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 0
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 1
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 2
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 3
                elif self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 4
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 5
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 6
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 7
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx > dy:
                if not self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 8
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 9
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 10
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 11
                elif self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 12
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 13
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 14
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 15
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx > dy:
                if not self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 16
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 17
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 18
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 19
                elif self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 20
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 21
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 22
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 23
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx > dy:
                if not self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 24
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 25
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 26
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 27
                elif self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 28
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 29
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 30
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 31
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] == self.food_pos[1] and dx > dy:
                if not self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 32
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 33
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 34
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 35
                elif self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 36
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 37
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 38
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 39
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] == self.food_pos[1] and dx > dy:
                if not self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 40
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 41
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 42
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 43
                elif self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 44
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 45
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 46
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 47
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                if not self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 48
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 49
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 50
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 51
                elif self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 52
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 53
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 54
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 55
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                if not self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 56
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 57
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 58
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 59
                elif self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 60
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 61
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 62
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 63
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                if not self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 64
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 65
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 66
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 67
                elif self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 68
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 69
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 70
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 71
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                if not self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 72
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 73
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 74
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 75
                elif self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 76
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 77
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 78
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 79
            elif self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                if not self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 80
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 81
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 82
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 83
                elif self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 84
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 85
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 86
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 87
            elif self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                if not self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 88
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 89
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 90
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 91
                elif self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 92
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 93
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 94
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 95
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx == dy:
                if not self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 96
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 97
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 98
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 99
                elif self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 100
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 101
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 102
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 103
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx == dy:
                if not self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 104
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 105
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 106
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 107
                elif self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 108
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 109
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 110
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 111
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx == dy:
                if not self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 112
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 113
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 114
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 115
                elif self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 116
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 117
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 118
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 119
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx == dy:
                if not self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 120
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 121
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 122
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 123
                elif self.collision("RIGHT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 124
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 125
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 126
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 127

        elif self.direction == "LEFT":

            if self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx > dy:
                if not self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 128
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 129
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 130
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 131
                elif self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 132
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 133
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 134
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 135
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx > dy:
                if not self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 136
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 137
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 138
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 139
                elif self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 140
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 141
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 142
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 143
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx > dy:
                if not self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 144
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 145
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 146
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 147
                elif self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 148
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 149
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 150
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 151
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx > dy:
                if not self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 152
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 153
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 154
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 155
                elif self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 156
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 157
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 158
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 159
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] == self.food_pos[1] and dx > dy:
                if not self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 160
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 161
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 162
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 163
                elif self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 164
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 165
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 166
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 167
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] == self.food_pos[1] and dx > dy:
                if not self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 168
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 169
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 170
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 171
                elif self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 172
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 173
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 174
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 175
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                if not self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 176
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 177
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 178
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 179
                elif self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 180
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 181
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 182
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 183
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                if not self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 184
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 185
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 186
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 187
                elif self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 188
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 189
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 190
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 191
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                if not self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 192
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 193
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 194
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 195
                elif self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 196
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 197
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 198
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 199
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                if not self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 200
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 201
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 202
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 203
                elif self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 204
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 205
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 206
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 207
            if self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                if not self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 208
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 209
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 210
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 211
                elif self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 212
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 213
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 214
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 215
            elif self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                if not self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 216
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 217
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 218
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 219
                elif self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 220
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 221
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 222
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 223
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx == dy:
                if not self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 224
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 225
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 226
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 227
                elif self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 228
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 229
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 230
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 231
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx == dy:
                if not self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 232
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 233
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 234
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 235
                elif self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 236
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 237
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 238
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 239
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx == dy:
                if not self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 240
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 241
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 242
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 243
                elif self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 244
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 245
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 246
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 247
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx == dy:
                if not self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 248
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 249
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 250
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 251
                elif self.collision("LEFT"):
                    if self.collision("UP") and not self.collision("DOWN"):
                        state = 252
                    elif self.collision("DOWN") and not self.collision("UP"):
                        state = 253
                    elif self.collision("UP") and self.collision("DOWN"):
                        state = 254
                    elif not self.collision("DOWN") and not self.collision("UP"):
                        state = 255

        elif self.direction == "DOWN":

            if self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx > dy:
                if not self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 256
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 257
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 258
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 259
                elif self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 260
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 261
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 262
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 263
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx > dy:
                if not self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 264
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 265
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 266
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 267
                elif self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 268
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 269
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 270
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 271
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx > dy:
                if not self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 272
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 273
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 274
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 275
                elif self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 276
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 277
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 278
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 279
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx > dy:
                if not self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 280
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 281
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 282
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 283
                elif self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 284
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 285
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 286
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 287
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] == self.food_pos[1] and dx > dy:
                if not self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 288
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 289
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 290
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 291
                elif self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 292
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 293
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 294
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 295
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] == self.food_pos[1] and dx > dy:
                if not self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 296
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 297
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 298
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 299
                elif self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 300
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 301
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 302
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 303
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                if not self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 304
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 305
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 306
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 307
                elif self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 308
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 309
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 310
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 311
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                if not self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 312
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 313
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 314
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 315
                elif self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 316
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 317
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 318
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 319
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                if not self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 320
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 321
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 322
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 323
                elif self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 324
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 325
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 326
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 327
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                if not self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 328
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 329
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 330
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 331
                elif self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 332
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 333
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 334
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 335
            elif self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                if not self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 336
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 337
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 338
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 339
                elif self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 340
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 341
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 342
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 343
            elif self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                if not self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 344
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 345
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 346
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 347
                elif self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 348
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 349
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 350
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 351
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx == dy:
                if not self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 352
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 353
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 354
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 355
                elif self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 356
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 357
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 368
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 359
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx == dy:
                if not self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 360
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 361
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 362
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 363
                elif self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 364
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 365
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 366
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 367
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx == dy:
                if not self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 368
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 369
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 370
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 371
                elif self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 372
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 373
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 374
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 375
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx == dy:
                if not self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 376
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 377
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 378
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 379
                elif self.collision("DOWN"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 380
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 381
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 382
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 383

        elif self.direction == "UP":

            if self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx > dy:
                if not self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 384
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 385
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 386
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 387
                elif self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 388
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 389
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 390
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 391
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx > dy:
                if not self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 392
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 393
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 394
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 395
                elif self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 396
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 397
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 398
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 399
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx > dy:
                if not self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 400
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 401
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 402
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 403
                elif self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 404
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 405
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 406
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 407
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx > dy:
                if not self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 408
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 409
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 410
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 411
                elif self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 412
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 413
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 414
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 415
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] == self.food_pos[1] and dx > dy:
                if not self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 416
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 417
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 418
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 419
                elif self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 420
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 421
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 422
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 423
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] == self.food_pos[1] and dx > dy:
                if not self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 424
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 425
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 426
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 427
                elif self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 428
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 429
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 430
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 431
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                if not self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 432
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 433
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 434
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 435
                elif self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 436
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 437
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 438
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 439
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                if not self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 440
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 441
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 442
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 443
                elif self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 444
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 445
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 446
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 447
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                if not self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 448
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 449
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 450
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 451
                elif self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 452
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 453
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 454
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 455
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                if not self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 456
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 457
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 458
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 459
                elif self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 460
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 461
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 462
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 463
            elif self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx < dy:
                if not self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 464
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 465
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 466
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 467
                elif self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 468
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 469
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 470
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 471
            elif self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx < dy:
                if not self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 472
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 473
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 474
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 475
                elif self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 476
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 477
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 478
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 479
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx == dy:
                if not self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 480
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 481
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 482
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 483
                elif self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 484
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 485
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 486
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 487
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] < self.food_pos[1] and dx == dy:
                if not self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 488
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 489
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 490
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 491
                elif self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 492
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 493
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 494
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 495
            elif self.snake_pos[0] > self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx == dy:
                if not self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 496
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 497
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 498
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 499
                elif self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 500
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 501
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 502
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 503
            elif self.snake_pos[0] < self.food_pos[0] and self.snake_pos[1] > self.food_pos[1] and dx == dy:
                if not self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 504
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 505
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 506
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 507
                elif self.collision("UP"):
                    if self.collision("RIGHT") and not self.collision("LEFT"):
                        state = 508
                    elif self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 509
                    elif self.collision("RIGHT") and self.collision("LEFT"):
                        state = 510
                    elif not self.collision("LEFT") and not self.collision("RIGHT"):
                        state = 511

        return state

    def get_body(self):
        return self.snake_body

    def get_food(self):
        return self.food_pos

    def avaliableOptions(self):
        avaliable = 0
        if self.direction == "RIGHT":
            if not self.collision("RIGHT") and not self.collision("DOWN") and not self.collision("UP"):
                avaliable = 3
            elif self.collision("RIGHT") and not self.collision("DOWN") and not self.collision("UP"):
                avaliable = 2
            elif not self.collision("RIGHT") and self.collision("DOWN") and not self.collision("UP"):
                avaliable = 2
            elif not self.collision("RIGHT") and not self.collision("DOWN") and self.collision("UP"):
                avaliable = 2
            elif self.collision("RIGHT") and self.collision("DOWN") and not self.collision("UP"):
                avaliable = 1
            elif self.collision("RIGHT") and not self.collision("DOWN") and self.collision("UP"):
                avaliable = 1
            elif self.collision("RIGHT") and not self.collision("DOWN") and  self.collision("UP"):
                avaliable = 0

        if self.direction == "LEFT":
            if not self.collision("LEFT") and not self.collision("DOWN") and not self.collision("UP"):
                avaliable = 3
            elif self.collision("LEFT") and not self.collision("DOWN") and not self.collision("UP"):
                avaliable = 2
            elif not self.collision("LEFT") and self.collision("DOWN") and not self.collision("UP"):
                avaliable = 2
            elif not self.collision("LEFT") and not self.collision("DOWN") and self.collision("UP"):
                avaliable = 2
            elif self.collision("LEFT") and self.collision("DOWN") and not self.collision("UP"):
                avaliable = 1
            elif self.collision("LEFT") and not self.collision("DOWN") and self.collision("UP"):
                avaliable = 1
            elif self.collision("LEFT") and not self.collision("DOWN") and  self.collision("UP"):
                avaliable = 0

        if self.direction == "UP":
            if not self.collision("UP") and not self.collision("RIGHT") and not self.collision("LEFT"):
                avaliable = 3
            elif self.collision("UP") and not self.collision("RIGHT") and not self.collision("LEFT"):
                avaliable = 2
            elif not self.collision("UP") and self.collision("RIGHT") and not self.collision("LEFT"):
                avaliable = 2
            elif not self.collision("UP") and not self.collision("RIGHT") and self.collision("LEFT"):
                avaliable = 2
            elif self.collision("UP") and self.collision("RIGHT") and not self.collision("LEFT"):
                avaliable = 1
            elif self.collision("UP") and not self.collision("RIGHT") and self.collision("LEFT"):
                avaliable = 1
            elif self.collision("UP") and not self.collision("RIGHT") and  self.collision("LEFT"):
                avaliable = 0

        if self.direction == "DOWN":
            if not self.collision("DOWN") and not self.collision("RIGHT") and not self.collision("LEFT"):
                avaliable = 3
            elif self.collision("DOWN") and not self.collision("RIGHT") and not self.collision("LEFT"):
                avaliable = 2
            elif not self.collision("DOWN") and self.collision("RIGHT") and not self.collision("LEFT"):
                avaliable = 2
            elif not self.collision("DOWN") and not self.collision("RIGHT") and self.collision("LEFT"):
                avaliable = 2
            elif self.collision("DOWN") and self.collision("RIGHT") and not self.collision("LEFT"):
                avaliable = 1
            elif self.collision("DOWN") and not self.collision("RIGHT") and self.collision("LEFT"):
                avaliable = 1
            elif self.collision("DOWN") and not self.collision("RIGHT") and self.collision("LEFT"):
                avaliable = 0

        return avaliable

    def print_state(self):
        print("--------GAME STATE--------")
        print("Direction:", self.direction)
        print("Next position :", self.nextPos())
        print("Snake Body:", self.snake_body)
        print("head X :", self.snake_pos[0], ", head Y:", self.snake_pos[1])
        print("Score:", self.avaliableOptions())
        print("collisonRight", self.collision("RIGHT"))
        print("collisonLeft", self.collision("LEFT"))
        print("collisonUp", self.collision("UP"))
        print("collisonUp", self.collision("DOWN"))
        print("gameover",self.check_game_over())
        print("state ", self.get_state())

    def calculate_reward(self):
        if self.check_game_over() and self.avaliableOptions() == 0:
            reward = -3000
        elif self.check_game_over() and self.avaliableOptions() == 1:
            reward = -2500
        elif self.check_game_over() and self.avaliableOptions() == 2:
            reward = -2000
        elif self.check_game_over() and self.avaliableOptions() == 3:
            reward = -1500
        elif self.snake_pos == self.food_pos and self.avaliableOptions() == 3:
            reward = +500
        elif self.snake_pos == self.food_pos and self.avaliableOptions() == 2:
            reward = +300
        elif self.snake_pos == self.food_pos and self.avaliableOptions() == 1:
            reward = +200
        elif self.snake_pos == self.food_pos and self.avaliableOptions() == 0:
            reward = -100
        else:
            reward = -10
        return reward

    def check_game_over(self):
        # Return True if the game is over, else False
        if self.snake_pos[0] < 0 or self.snake_pos[0] > self.frame_size_x - 10:
            return True
        if self.snake_pos[1] < 0 or self.snake_pos[1] > self.frame_size_y - 10:
            return True
        for block in self.snake_body[1:]:
            if self.snake_pos[0] == block[0] and self.snake_pos[1] == block[1]:
                return True

        return False





    def nextPos(self):
        head_x, head_y = self.snake_pos
        next_move = [head_x, head_y]
        direction = self.direction
        # To do so we need to know the next position in which the head will be to avoid it
        if direction == "RIGHT":
            next_move = [head_x + 10, head_y]
        elif direction == "LEFT":
            next_move = [head_x - 10, head_y]
        elif direction == "DOWN":
            next_move = [head_x, head_y + 10]
        elif direction == "UP":
            next_move = [head_x, head_y - 10]

        return next_move

    def collisionWall(self):
        # Return True if the game is over, else False
        if self.snake_pos[0] < 0 or self.snake_pos[0] > self.frame_size_x - 10:
            return True
        if self.snake_pos[1] < 0 or self.snake_pos[1] > self.frame_size_y - 10:
            return True
        return False

    def collisionBody(self):
        # To do so we need to know the next position in which the head will be to avoid it
        next_move = self.nextPos()

        if next_move in self.snake_body:
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
            self.food_pos = [random.randrange(1, (self.frame_size_x // 10)) * 10,
                             random.randrange(1, (self.frame_size_x // 10)) * 10]
        self.food_spawn = True
