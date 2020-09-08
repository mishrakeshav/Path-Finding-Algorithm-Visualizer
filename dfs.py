import pygame 
import math 
from queue import deque
class DFS:
    @staticmethod
    def draw_path(end, start, draw):
        node = end 
        while node:
            node.make_path()
            draw()
            node = node.parent
    @staticmethod
    def dfs(draw, grid, start, end):
        nodes = deque()
        nodes.appendleft(start)
        visited = set()
        visited.add(start)
        start.parent = None 
        while nodes:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            current_node = nodes.popleft()
            if current_node is end:
                DFS.draw_path(end, start, draw)
                end.make_end()
                start.make_start()
                return True 
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    neighbor.parent = current_node
                    if neighbor == end:
                        DFS.draw_path(end, start, draw)
                        end.make_end()
                        start.make_start()
                        return True 
                    neighbor.make_open()
                    nodes.appendleft(neighbor)
                    draw()
            if current_node != start:
                current_node.make_closed()
                draw()
        return False 
            


