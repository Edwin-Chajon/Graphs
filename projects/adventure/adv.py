from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

#bring in stack

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


# TRAVERSAL TEST
visited_rooms = set()
#player.current_room = world.starting_room
#visited_rooms.add(player.current_room)



all_exits = world.starting_room.get_exits()

the_stack = Stack()
the_stack.push([world.starting_room])

while the_stack.size():
    current = the_stack.pop()[-1]

    if current not in visited_rooms:
        visited_rooms.add(current)
        
        for exits in all_exits:
            if current.get_room_in_direction(exits):
                traversal_path.append(exits)
                next_room = current.get_room_in_direction(exits)
                new_path = [next_room]
                the_stack.push(new_path)


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(world.starting_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
