import tkinter as tk
from tkinter import messagebox
import random
from queue import Queue

# 迷宫大小
MAZE_SIZE = 30  # 增大迷宫尺寸以增加复杂性

# 定义迷宫格子类型
EMPTY = 0
WALL = 1
START = 2
END = 3

# 定义方向
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上

class MazeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("迷宫游戏")
        
        # 创建迷宫
        self.maze = self.generate_maze_dfs(MAZE_SIZE)
        self.player_pos = self.find_start()
        self.end_pos = self.find_end()
        
        # 创建画布
        self.cell_size = 20  # 减小每个格子的大小以适应更大的迷宫
        self.canvas = tk.Canvas(root, width=MAZE_SIZE * self.cell_size, height=MAZE_SIZE * self.cell_size)
        self.canvas.pack()
        
        # 绘制迷宫
        self.draw_maze()
        
        # 创建按钮
        self.mode_frame = tk.Frame(root)
        self.mode_frame.pack()
        
        self.player_button = tk.Button(self.mode_frame, text="玩家游玩", command=self.start_player_mode)
        self.player_button.pack(side=tk.LEFT)
        
        self.ai_button = tk.Button(self.mode_frame, text="AI自动游戏", command=self.start_ai_mode)
        self.ai_button.pack(side=tk.LEFT)
        
        # 绑定键盘事件
        self.root.bind("<KeyPress>", self.key_press)
        
        # 游戏状态
        self.game_mode = None
    
    def generate_maze_dfs(self, size):
        """使用深度优先搜索（DFS）生成迷宫"""
        maze = [[WALL for _ in range(size)] for _ in range(size)]
        
        def dfs(x, y):
            maze[x][y] = EMPTY
            directions = DIRECTIONS[:]
            random.shuffle(directions)
            
            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2
                if 0 <= nx < size and 0 <= ny < size and maze[nx][ny] == WALL:
                    maze[x + dx][y + dy] = EMPTY
                    dfs(nx, ny)
        
        # 从起点开始生成迷宫
        dfs(1, 1)
        
        # 设置起点和终点
        maze[1][1] = START
        maze[size-2][size-2] = END
        
        return maze
    
    def add_gaps_around_start_end(self):
        """在入口和出口周围增加缺口"""
        start_x, start_y = self.start_pos
        end_x, end_y = self.end_pos
        
        # 在入口周围增加缺口
        for dx, dy in DIRECTIONS:
            nx, ny = start_x + dx, start_y + dy
            if 0 <= nx < MAZE_SIZE and 0 <= ny < MAZE_SIZE and self.maze[nx][ny] == WALL:
                if random.random() < 1.0:  # 100%的概率将墙壁变为缺口
                    self.maze[nx][ny] = EMPTY
        
        # 在出口周围增加缺口
        for dx, dy in DIRECTIONS:
            nx, ny = end_x + dx, end_y + dy
            if 0 <= nx < MAZE_SIZE and 0 <= ny < MAZE_SIZE and self.maze[nx][ny] == WALL:
                if random.random() < 0.9:  # 70%的概率将墙壁变为缺口
                    self.maze[nx][ny] = EMPTY
    
    def find_start(self):
        """找到起点位置"""
        for i in range(MAZE_SIZE):
            for j in range(MAZE_SIZE):
                if self.maze[i][j] == START:
                    return (i, j)
        return None
    
    def find_end(self):
        """找到终点位置"""
        for i in range(MAZE_SIZE):
            for j in range(MAZE_SIZE):
                if self.maze[i][j] == END:
                    return (i, j)
        return None
    
    def draw_maze(self):
        """绘制迷宫"""
        self.canvas.delete("all")
        for i in range(MAZE_SIZE):
            for j in range(MAZE_SIZE):
                x1, y1 = j * self.cell_size, i * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                if self.maze[i][j] == WALL:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                elif self.maze[i][j] == START:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")
                elif self.maze[i][j] == END:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
        
        # 绘制玩家位置
        if self.player_pos:
            x, y = self.player_pos
            x1, y1 = y * self.cell_size, x * self.cell_size
            x2, y2 = x1 + self.cell_size, y1 + self.cell_size
            self.canvas.create_oval(x1+5, y1+5, x2-5, y2-5, fill="blue")
    
    def start_player_mode(self):
        """开始玩家游玩模式"""
        self.game_mode = "player"
        self.player_pos = self.find_start()
        self.draw_maze()
        messagebox.showinfo("提示", "玩家模式已启动！使用方向键移动。")
    
    def start_ai_mode(self):
        """开始AI自动游戏模式"""
        self.game_mode = "ai"
        self.player_pos = self.find_start()
        self.draw_maze()
        self.ai_solve()
    
    def key_press(self, event):
        """处理键盘事件"""
        if self.game_mode != "player":
            return
        
        x, y = self.player_pos
        if event.keysym == "Up":
            new_x, new_y = x - 1, y
        elif event.keysym == "Down":
            new_x, new_y = x + 1, y
        elif event.keysym == "Left":
            new_x, new_y = x, y - 1
        elif event.keysym == "Right":
            new_x, new_y = x, y + 1
        else:
            return
        
        # 检查是否可以移动
        if 0 <= new_x < MAZE_SIZE and 0 <= new_y < MAZE_SIZE and self.maze[new_x][new_y] != WALL:
            self.player_pos = (new_x, new_y)
            self.draw_maze()
            
            # 检查是否到达终点
            if self.player_pos == self.end_pos:
                messagebox.showinfo("Congratulations", "You managed to get out of the maze！")
                self.game_mode = None
    
    def ai_solve(self):
        """AI自动解决迷宫"""
        start = self.find_start()
        end = self.find_end()
        path = self.bfs(start, end)
        
        if not path:
            messagebox.showinfo("提示", "AI can't find the path！")
            return
        
        # AI按照路径移动
        for pos in path:
            self.player_pos = pos
            self.draw_maze()
            self.root.update()
            self.root.after(70)  # 每次移动间隔200ms
        
        messagebox.showinfo("提示", "AI made it.！")
    
    def bfs(self, start, end):
        """广度优先搜索寻找路径"""
        queue = Queue()
        queue.put((start, [start]))
        visited = set()
        visited.add(start)
        
        while not queue.empty():
            (x, y), path = queue.get()
            
            if (x, y) == end:
                return path
            
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < MAZE_SIZE and 0 <= new_y < MAZE_SIZE and self.maze[new_x][new_y] != WALL and (new_x, new_y) not in visited:
                    queue.put(((new_x, new_y), path + [(new_x, new_y)]))
                    visited.add((new_x, new_y))
        
        return None

if __name__ == "__main__":
    root = tk.Tk()
    game = MazeGame(root)
    root.mainloop()