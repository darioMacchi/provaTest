from main import Product, calculate_order_total
from hypothesis import given, strategies as st

# Property Based Testing

products = st.builds(Product, st.text(), st.floats(min_value=0.01), st.integers(min_value=1))
@given(orders=st.lists(products, min_size=2, max_size=5))
def test_subtotal_not_zero(orders):
    '''
    Test case 1: Not empty order greater than zero property
    '''
    assert calculate_order_total(orders, "", False) > 0

products = st.builds(Product, st.text(), st.floats(min_value=50), st.integers(min_value=1))
@given(orders=st.lists(products, min_size=2, max_size=5))
def test_subtotal_greater_fifty(orders):
    '''
    Test case 2: Free shipping as subtotal greater than fifty property
    '''
    expected_value = 0
    for product in orders:
        expected_value += product.price * product.quantity

    assert calculate_order_total(orders, "", False) == expected_value
