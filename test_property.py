from main import Product, calculate_order_total
from hypothesis import given, strategies as st

# Property Based Testing

@given(
        orders=st.lists(st.builds(Product, st.text(), st.floats(min_value=0.01), st.integers(min_value=1)), min_size=2, max_size=5),
        promo_code=st.text(),
        is_vip=st.booleans()
        )
def test_subtotal_not_zero(orders, promo_code, is_vip):
    '''
    Test case 1: Not empty order greater than zero property
    '''
    assert calculate_order_total(orders, promo_code, is_vip) > 0

@given(
        orders=st.lists(st.builds(Product, st.text(), st.floats(min_value=50), st.integers(min_value=1)), min_size=2, max_size=5),
        promo_code=st.text(),
        is_vip=st.booleans()
        )
def test_subtotal_greater_fifty(orders, promo_code, is_vip):
    '''
    Test case 2: Free shipping as subtotal greater than fifty property
    '''
    expected_value = 0
    for product in orders:
        expected_value += product.price * product.quantity

    assert calculate_order_total(orders, promo_code, is_vip) == expected_value

@given(
        orders=st.lists(st.builds(Product, st.text(), st.floats(min_value=0.01, max_value=9.99), st.integers(min_value=1, max_value=1)), min_size=2, max_size=5),
        promo_code=st.text(),
        is_vip=st.booleans())
def test_subtotal_smaller_fifty(orders, promo_code, is_vip):
    '''
    Test case 3: Shipping fee as subtotal smaller than fifty property
    '''
    expected_value = 0
    for product in orders:
        expected_value += product.price * product.quantity

    if is_vip:
        expected_value += 2
    else:
        expected_value += 5

    assert calculate_order_total(orders, promo_code, is_vip) == expected_value
