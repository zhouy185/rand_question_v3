import random


def random_choice(n_list, q_list):
    name = random.choice(n_list)
    question = random.choice(q_list)
    return f"Question for **{name}**: {question}"