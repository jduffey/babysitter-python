from app import calc_regular_paycheck
from app import calc_bedtime_paycheck
from app import calc_midnight_paycheck
from app import calc_total_paycheck


def test_calc_regular_paycheck_returns_money_earned():
    actual = calc_regular_paycheck(6, 10)
    expected = 48

    assert expected == actual


def test_calc_bedtime_paycheck_returns_money_earned():
    actual = calc_bedtime_paycheck(10, 12)
    expected = 16

    assert expected == actual


def test_calc_midnight_paycheck_returns_money_earned():
    actual = calc_midnight_paycheck(2, 4)
    expected = 32

    assert expected == actual


def test_calc_total_paycheck_returns_money_earned():
    actual = calc_total_paycheck(5, 11, 8)
    expected = 60

    assert expected == actual


def test_calc_midnight_paycheck_starting_at_midnight_returns_money_earned():
    actual = calc_midnight_paycheck(12, 2)
    expected = 32

    assert expected == actual


def test_calc_total_paycheck_ending_after_midnight_returns_money_earned():
    actual = calc_total_paycheck(9, 2, 10)
    expected = 60

    assert expected == actual


def test_calc_total_paycheck_bedtime_after_midnight_returns_money_earned():
    actual = calc_total_paycheck(5, 4, 1)
    expected = 84 + 0 + 64

    assert expected == actual
