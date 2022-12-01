import render as render
import map as map
import actors as actors
import pygame
import sys
import cProfile as profile


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def main():
    player = actors.Player((150, 150), (0, -1), 1, 1, 500)
    # Not done for this map, but all corners should be solid to prevent their becoming invisble
    worldmap = map.Map("0121212120\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n1000000002\n0121212120", 32)
    for i in range(200):
        render.render_frame(screen, worldmap, player)
        handle_events()
        player.rotate(0.01 * player.rotation_speed)

if __name__ == "__main__":
    global screen
    screen = render.init(400, 300)
    profile.run("main()")

