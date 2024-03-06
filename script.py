import random
from datetime import datetime, timedelta


def generate_question() -> str:
    len1 = random.randint(1, 9)
    len2 = random.randint(1, 2)
    operator = random.choice("+-*/")
    num1 = str(random.randint(1, 9)) * len1
    num2 = str(random.randint(1, 9)) * len2
    return f"{num1} {operator} {num2}"


def evaluate_expression(expression: str) -> int | float:
    return eval(expression)


def generate_course_title() -> str:
    course_code = random.randint(1000, 9999)
    num = random.randint(1, 9)
    items = [
        "Assignment",
        "Quiz",
        "Mock",
        "Homework",
        "Self Study",
        "Notes",
        "Cheatsheet",
        "Classwork",
    ]
    item = random.choice(items)
    return f"MATH{course_code} {item} {num} Answer"


def generate_date() -> str:
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 12, 31)

    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)

    formatted_date = random_date.strftime("%A %d %B %Y")
    return formatted_date


def generate_question_template(q: int) -> str:
    question = generate_question()
    answer = evaluate_expression(question)
    return f"Q{q}: {question} = ?\nA{q} {question} = {answer}\n\n"


def generate_document() -> None:
    course_title = generate_course_title()
    date = generate_date()
    with open(f"files/{course_title}.doc", "x") as f:
        f.write(f"{course_title}\n")
        f.write(f"Date: {date}\n")
        f.write("Name: __________\n")
        f.write("Class: _____\n")
        f.write("Class No.: ___\n")
        f.write("\n")

        for i in range(1, 51):
            f.write(generate_question_template(i))


if __name__ == "__main__":
    print("Welcome to CHeroUnlocker!")
    while True:
        n = input("How many documents would you like to generate? > ")
        if not n.isdigit():
            print("Please enter a positive integer!")
        else:
            break
    n = int(n)
    for i in range(1, n + 1):
        generate_document()
        print(f"Generating Document #{i}")

    print(f"Sucessfully generated {n} documents!")
    print("They are located in the files folder.")
    print("Enjoy!")
    print("You can safely this program now.")
