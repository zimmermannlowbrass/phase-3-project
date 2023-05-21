#!/usr/bin/env python3

def choose_a_table(seated_customers):
    possible_choices = ['1', '2', '3', '4', '5']
    customer_choices = ''
    for x in range(len(seated_customers)):
        customer_choices += (str(seated_customers[x].table))
        customer_choices += f'. {seated_customers[x].name} \n'
    customer_choice = input(f'\nWhich table would you like to go to?\n{customer_choices}')
    while customer_choice not in possible_choices:
        customer_choice = input(f'\nOOPS! That\'s not a table. Here are the tables:\n{customer_choices}')
    customer = None
    for choices in seated_customers:
        if choices.table == int(customer_choice):
            customer = choices
    return customer


def add_to_customer_database(customer):
    customer_info = f"""
        Name: {customer.name}
        Age: {customer.age}
        Email Address: {customer.email}
        Phone Number: {customer.phone}\n
    """
    with open('customers_served.txt', mode='a', encoding='utf-8') as database:
        database.write(customer_info)


def take_down_data(user_name, total_money, stress, choice):
    if choice == 1:
        choice = 'Talk to/get to know the customer.'
    elif choice == 2:
        choice = 'Takee an order from a customer.'
    elif choice == 3:
        choice = 'Give a receipt to a customer.'
    text = f"""
        Username : {user_name}
        Choice : {choice}
        Current : {stress}
        Money : {total_money}
    """
    with open(f'{user_name}_gameplay.txt', mode='a', encoding='utf-8') as database:
        database.write(text)