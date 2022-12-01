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
    while True:
        render.render_frame(screen, worldmap, player)
        handle_events()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.move_relative_fwd(5)
        if keys[pygame.K_a]:
            player.rotate(0.04 * player.rotation_speed)
        if keys[pygame.K_s]:
            player.move_relative_fwd(-5)
        if keys[pygame.K_d]:
            player.rotate(-0.04 * player.rotation_speed)

if __name__ == "__main__":
    global screen
    screen = render.init(400, 300)
    #profile.run("main()")
    main()
