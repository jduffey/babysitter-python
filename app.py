def calc_regular_paycheck(start_time, end_time):
    if end_time <= 4:
        end_time = 12
    hours_worked = end_time - start_time
    payrate = 12
    money_earned = hours_worked * payrate
    return money_earned


def calc_bedtime_paycheck(start_time, end_time):
    if end_time <= 4:
        end_time = 12
    if start_time <= 4:
        start_time = 12
    hours_worked = end_time - start_time
    payrate = 8
    money_earned = hours_worked * payrate
    return money_earned


def calc_midnight_paycheck(start_time, end_time):
    if start_time == 12:
        start_time = 0
    hours_worked = end_time - start_time
    payrate = 16
    money_earned = hours_worked * payrate
    return money_earned


def calc_total_paycheck(start_time, end_time, bedtime):
    regular_paycheck = calc_regular_paycheck(start_time, bedtime)
    bedtime_paycheck = calc_bedtime_paycheck(bedtime, end_time)
    if end_time <= 4:
        midnight_paycheck = calc_midnight_paycheck(12, end_time)
    else:
        midnight_paycheck = 0
    money_earned = regular_paycheck + bedtime_paycheck + midnight_paycheck
    return money_earned
