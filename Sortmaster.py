# main.py
import pygame
import sys
from functions import (
    bubble_sort, merge_sort, quick_sort,
    draw_array, show_instructions,
    generate_random_array, get_custom_array,
    WIDTH, HEIGHT, win, BLUE
)

pygame.init()
clock = pygame.time.Clock()
FPS = 60

def main():
    global win
    print("Sorting Visualizer running...")

    running = True
    sorted = False
    sort_started = False
    algorithm = None
    array = generate_random_array()

    while running:
        clock.tick(FPS)
        win.fill(BLUE)
        draw_array(array)
        show_instructions()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if not sort_started and not sorted:
                    if event.key == pygame.K_b:
                        algorithm = "bubble"
                        sort_started = True
                    elif event.key == pygame.K_m:
                        algorithm = "merge"
                        sort_started = True
                    elif event.key == pygame.K_q:
                        algorithm = "quick"
                        sort_started = True
                    elif event.key == pygame.K_a:
                        array = generate_random_array()
                        sorted = False
                        sort_started = False
                    elif event.key == pygame.K_c:
                        pygame.quit()
                        array = get_custom_array()
                        pygame.init()
                        win = pygame.display.set_mode((WIDTH, HEIGHT))
                        pygame.display.set_caption("Bhagya's Sortmaster🔃")
                        sort_started = False
                        sorted = False

                # Allow restart after sort completes
                if event.key == pygame.K_r and sorted and algorithm:
                    array = generate_random_array()
                    sort_started = True
                    sorted = False

        if sort_started and not sorted:
            if algorithm == "bubble":
                bubble_sort(array)
            elif algorithm == "merge":
                merge_sort(array, 0, len(array) - 1)
                draw_array(array)
            elif algorithm == "quick":
                quick_sort(array, 0, len(array) - 1)
                draw_array(array)
            sorted = True

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\n❌ ERROR:", e)
        input("\nPress Enter to exit...")