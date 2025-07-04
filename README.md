Bhagya's Sortmaster is a beautiful, interactive sorting algorithm visualizer developed in Python and Pygame. It features easy-to-understand, real-time visualization of top sorting algorithms such as Bubble Sort, Merge Sort, and Quick Sort. The project was intended to serve as an educational resource to enable learners, developers, and instructors to visually see how the algorithms work step by step. Each entry in the array is displayed as a stack bar of height equal to its value, and when sorting, bars toggle colors (green for an active comparison, yellow for unsorted data) and show their numeric values above them, for greater clarity. Users are able to interact through keyboard commands to choose an algorithm, randomly generate an array, input their own custom array values via terminal, or reset the same sort with fresh data. The application is run fullscreen to maximize visibility and immersion.

To run the project, ensure Python is installed on your system along with the pygame package (pip install pygame). When installed, simply go to the project directory and execute the main.py script using the python main.py command. The user interface will be launched and show messages what keys to press — i.e., B for Bubble Sort, M for Merge Sort, Q for Quick Sort, A to create a random array, C to enter a custom array, and R to start the current sort using a new random array.

The project is divided into two major files:
main.py deals with the application's main logic, such as the game loop, user input, and sort control.
functions.py has all the reusable elements like sorting algorithm functions, array drawing logic, custom input, and array generation.

Together, these files comprise a tidy, modular codebase that not only makes the visualizer simple to run but simple to modify or extend. You're a learning beginner with sorting, a teacher illustrating ideas in class, or a dev learning about Pygame; Bhagya's Sortmaster provides a colorful, interactive means of exploring algorithmic thinking.

It also contain output video of bubble,merge and quick  sort.
