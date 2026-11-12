
from hypothesis import given, strategies as st
from laundry_service import (
    parse_order,
    weight_average,
    payable_charge
)


# Test 1: parse_order
@given(st.one_of(st.text(), st.none()))
def test_parse_order_no_crash(value):
    try:
        parse_order(value)
    except ValueError:
        pass


@given(st.floats(
    min_value=0.01,
    max_value=1000,
    allow_nan=False,
    allow_infinity=False
))
def test_parse_order_valid_weight(weight):
    result = parse_order(f"regular:{weight}")
    assert result[0] == "Regular"
    assert result[1] == weight


# Test 2: weight_average
@given(st.one_of(st.text(), st.none()))
def test_weight_average_no_crash(value):
    try:
        weight_average(value)
    except ValueError:
        pass


@given(st.lists(
    st.floats(
        min_value=0.01,
        max_value=1000,
        allow_nan=False,
        allow_infinity=False
    ),
    min_size=1,
    max_size=20
))
def test_weight_average_valid_values(weights):
    text = ",".join(map(str, weights))
    result = weight_average(text)
    expected = sum(weights) / len(weights)
    assert abs(result - expected) < 1e-8


# Test 3: payable_charge
@given(st.one_of(st.text(), st.none()))
def test_payable_charge_no_crash(value):
    try:
        payable_charge(value)
    except ValueError:
        pass


@given(
    st.floats(
        min_value=0,
        max_value=100000,
        allow_nan=False,
        allow_infinity=False
    ),
    st.floats(
        min_value=0,
        max_value=100,
        allow_nan=False,
        allow_infinity=False
    )
)
def test_payable_charge_valid_values(charge, discount):
    result = payable_charge(f"{charge}|{discount}")
    expected = charge * (1 - discount / 100) * 1.18
    assert abs(result - expected) < 0.01
