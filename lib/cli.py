#!/usr/bin/env python3

from helpers_mid import (
    customer_incoming, take_an_order,
    give_the_check, go_hang_out_with_a_customer
)

from helpers_begin_end import (
    enter_name_ready, choose_a_task, game_over
)


if __name__ == '__main__':
    open_tables = [1, 2, 3, 4, 5]
    seated_customers = []
    stress = 0
    total_money = 0

    user_name = enter_name_ready()
    while stress < 50 and len(seated_customers) < 5:
        print(f'\n\t********** CURRENT STRESS LEVEL: {stress} **********\n')
        open_tables, added_stress = customer_incoming(open_tables, seated_customers)
        stress += added_stress
        choice = choose_a_task()
        if (choice == 1):
            go_hang_out_with_a_customer(seated_customers)
        elif (choice == 2):
            destress, order = take_an_order(seated_customers)
            stress -= destress
        elif (choice == 3):
            earned_money, destress = give_the_check(open_tables, seated_customers)
            total_money += earned_money
            stress -= destress
    game_over(user_name, total_money)
        

    
    