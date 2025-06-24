import pygame
import random

WIDTH, HEIGHT = 1200, 900
YELLOW = (255, 255, 0)    # Bars
GREEN = (0, 255, 0)      # Highlight
BLUE = (0, 0, 255)       # Background
CYAN = (0, 255, 255)     # Text

win = pygame.display.set_mode((WIDTH, HEIGHT))

array = []

# Draw array bars with numbers
def draw_array(arr, highlight=[]):
    win.fill(BLUE)
    bar_width = WIDTH // len(arr)
    font = pygame.font.SysFont("Arial", 14)
    max_val = max(arr)
    scale = (HEIGHT - 100) / max_val

    for i, val in enumerate(arr):
        scaled_val = int(val * scale)
        color = GREEN if i in highlight else YELLOW
        pygame.draw.rect(win, color, (i * bar_width, HEIGHT - scaled_val, bar_width - 1, scaled_val))
        label = font.render(str(val), True, (255, 255, 255))
        label_x = i * bar_width + (bar_width // 2 - label.get_width() // 2)
        label_y = HEIGHT - scaled_val - 20
        win.blit(label, (label_x, max(label_y, 5)))
    pygame.display.update()


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            draw_array(arr, [j, j+1])
            pygame.time.delay(10)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    draw_array(arr)


def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


def merge(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    i = j = 0
    k = l

    while i < len(left) and j < len(right):
        draw_array(arr, [k])
        pygame.time.delay(10)
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        draw_array(arr, [k])
        pygame.time.delay(10)
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        draw_array(arr, [k])
        pygame.time.delay(10)
        arr[k] = right[j]
        j += 1
        k += 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        draw_array(arr, [j, high])
        pygame.time.delay(10)
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def show_instructions():
    font = pygame.font.SysFont("Comic Sans", 20)
    texts = [
        "Press B: Bubble Sort | M: Merge Sort | Q: Quick Sort",
        "Press A: Random Array | C: Custom Array | R: restart "
    ]
    for idx, txt in enumerate(texts):
        render = font.render(txt, True, CYAN)
        win.blit(render, (20, 20 + idx * 30))
    pygame.display.update()


def get_custom_array():
    input_str = input("Enter comma-separated integers (e.g., 50,100,30,...): ")
    try:
        values = [int(x.strip()) for x in input_str.split(',')]
        if len(values) < 2:
            raise ValueError("Array too small")
        return values
    except:
        print("Invalid input. Falling back to random array.")
        return generate_random_array()


def generate_random_array(size=100):
    return [random.randint(10, HEIGHT - 10) for _ in range(size)]