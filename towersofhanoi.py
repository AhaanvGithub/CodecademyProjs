# Using computer science course inbuilt classes
from stack import Stack

print("\nLet's play Towers of Hanoi!!")

stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

num_disk = int(input("\nHow many disks do you want to play with?\n"))

while num_disk <= 2:
    num_disk = int(input("Enter a number greater than or equal to 3\n"))

for i in range(num_disk, 0, -1):
    left_stack.push(i)

num_optimal_moves = (2 ** (num_disk + 1)) - 1
print("\nThe fastest you can solve this game is in " + str(num_optimal_moves) + " moves")


def get_input():
    choices = [i.get_name()[0] for i in stacks]

    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter", letter, "for", name)

        user_input = input("")

        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]


num_user_moves = 0

while right_stack.get_size() != num_disk:
    print("\n\n\n... Current Stacks ...")

    for i in stacks:
        i.print_items()

    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        if from_stack.get_size() == 0:
            print("\n\nInvalid Move. Try Again")
        elif (to_stack.get_size() == 0) or (from_stack.peek() < to_stack.peek()):
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again")

print("\n\nYou completed the game in", num_user_moves, "moves, and the optimal number of moves is", num_optimal_moves)

