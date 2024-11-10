import random


def genrate_random_int(min: int, max: int) -> int:
    """
    Function to generate a random integer between min and max.

    :param min: Minimum value of the random integer.
    :param max: Maximum value of the random integer.

    :return: Random integer between min and max.
    """
    return random.randint(min, max)


def genrate_random_operation() -> str:
    """
    Function to generate a random operation (addition, subtraction, multiplication).

    :return: Random operation.
    """
    return random.choice(['+', '-', '*'])


def generate_problem(num1: int, num2: int, op: str) -> tuple:
    """
    Function to generate a math problem.

    :param num1: First operand.
    :param num2: Second operand.
    :param op: Operation.

    :return: Tuple containing the math problem and the answer.
    """
    problem = f"{num1} {op} {num2}"
    if op == '+':
        answer = num1 + num2
    elif op == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer


def math_quiz():
    # Score of the user depending on the number of correct answers
    score = 0 
    # Total number of questions (this has to be an integer as we are using it in a loop)
    number_of_questions = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(number_of_questions)):
        # Generate random numbers and operation
        operant_one = genrate_random_int(1, 10)
        operant_two = genrate_random_int(1, 5)
        operation = genrate_random_operation()

        # Generate the problem and the answer
        PROBLEM, ANSWER = generate_problem(operant_one, operant_two, operation)
        # Print the question
        print(f"\nQuestion: {PROBLEM}")
        while True:
            try:
                # Attempt to convert to an integer
                useranswer = int(input("Your answer: "))
                # Exit the loop if the input is valid
                break
            except ValueError:
                print("Please enter a valid integer.") 

        # Check if the user's answer is correct
        if useranswer == ANSWER: # If the user's answer is correct
            # Increase the score by 1
            score += 1
            print("Correct! You earned a point.")
        else:                   # If the user's answer is wrong
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    # Print the final score per total number of questions
    print(f"\nGame over! Your score is: {score}/{int(number_of_questions)}")


if __name__ == "__main__":
    math_quiz()
