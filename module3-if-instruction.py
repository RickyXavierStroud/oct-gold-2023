user_age = int(input('What is your age?'))
if user_age > 30:
    print('You are over 30 years old')
    print('Sorry,you do not qualify')
elif user_age ==30:
    print('You are exactly 30 years old')
    print('You will need to meet additional conditions to qualify')
else:
    print('You are 30 years old or younger')
    print('Congratulations, you qualify!')
    
if condion_a_met:
    do_scenario_a()
elif condion_b_met:
    do_scenario_b()
elif condition_c_met:
    do_scenario_c()
else:
    do_scenario_d()