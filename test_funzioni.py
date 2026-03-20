from main import Product, calculate_order_total

# Direct test

def test_order_none():
    '''
    Test case 1: Empty order - None
    '''
    order_list = None
    promo_code = "SAVE10"
    is_vip = False
    attended_result = 0.0

    assert calculate_order_total(order_list, promo_code, is_vip) == attended_result

def test_order_list():
    '''
    Test case 2: Empty order - empty list
    '''
    order_list = []
    promo_code = "SAVE10"
    is_vip = False
    attended_result = 0.0

    assert calculate_order_total(order_list, promo_code, is_vip) == attended_result

def test_discount():
    '''
    Test case 3: Discount promo code
    '''
    p1 = Product(name="Scarpe", price=25.0, quantity=3)
    p2 = Product(name="Cappello", price=15.0, quantity=2)
    order_list = [p1,p2]
    promo_code = "SAVE10"
    is_vip = False
    attended_result = (25.0*3 + 15.0*2) - 10

    assert calculate_order_total(order_list, promo_code, is_vip) == attended_result

def test_free_shipping():
    '''
    Test case 4: Free shipping
    '''
    p1 = Product(name="Scarpe", price=25.0, quantity=3)
    p2 = Product(name="Cappello", price=15.0, quantity=2)
    order_list = [p1,p2]
    promo_code = ""
    is_vip = False
    attended_result = (25.0*3 + 15.0*2)

    assert calculate_order_total(order_list, promo_code, is_vip) == attended_result

def test_normal_shipping():
    '''
    Test case 5: No VIP shipping to apply
    '''
    p1 = Product(name="Scarpe", price=25.0, quantity=1)
    p2 = Product(name="Cappello", price=15.0, quantity=1)
    order_list = [p1,p2]
    promo_code = ""
    is_vip = False
    attended_result = (25.0 + 15.0) + 5

    assert calculate_order_total(order_list, promo_code, is_vip) == attended_result

def test_vip_shipping():
    '''
    Test case 6: VIP shipping to apply
    '''
    p1 = Product(name="Scarpe", price=25.0, quantity=1)
    p2 = Product(name="Cappello", price=15.0, quantity=1)
    order_list = [p1,p2]
    promo_code = ""
    is_vip = True
    attended_result = (25.0 + 15.0) + 2

    assert calculate_order_total(order_list, promo_code, is_vip) == attended_result

# Indirect test

def test_discount_less():
    '''
    Test case 7: Discount promo code with greater attended result
    '''
    p1 = Product(name="Scarpe", price=25.0, quantity=3)
    p2 = Product(name="Cappello", price=15.0, quantity=2)
    order_list = [p1,p2]
    promo_code = "SAVE10"
    is_vip = False
    attended_result = (25.0*3 + 15.0*2)

    assert calculate_order_total(order_list, promo_code, is_vip) < attended_result

def test_free_shipping_not_equal():
    '''
    Test case 8: Free shipping effective verification
    '''
    p1 = Product(name="Scarpe", price=25.0, quantity=3)
    p2 = Product(name="Cappello", price=15.0, quantity=2)
    order_list = [p1,p2]
    promo_code = ""
    is_vip = False
    attended_result = (25.0*3 + 15.0*2) + 5

    assert calculate_order_total(order_list, promo_code, is_vip) != attended_result

def test_normal_shipping_not_equal():
    '''
    Test case 9: VIP shipping negative verification
    '''
    p1 = Product(name="Scarpe", price=25.0, quantity=1)
    p2 = Product(name="Cappello", price=15.0, quantity=1)
    order_list = [p1,p2]
    promo_code = ""
    is_vip = False
    attended_result = (25.0 + 15.0) + 2

    assert calculate_order_total(order_list, promo_code, is_vip) != attended_result

def test_vip_shipping_not_equal():
    '''
    Test case 10: VIP shipping effective verification
    '''
    p1 = Product(name="Scarpe", price=25.0, quantity=1)
    p2 = Product(name="Cappello", price=15.0, quantity=1)
    order_list = [p1,p2]
    promo_code = ""
    is_vip = True
    attended_result = (25.0 + 15.0) + 5

    assert calculate_order_total(order_list, promo_code, is_vip) != attended_result

# Fail test

def test_promo_code():
    '''
    Test case 11: Promo code SAVE10 lower case
    '''
    p1 = Product(name="Scarpe", price=25.0, quantity=3)
    p2 = Product(name="Cappello", price=15.0, quantity=2)
    order_list = [p1,p2]
    promo_code = "save10"
    is_vip = False
    attended_result = (25.0*3 + 15.0*2) - 10

    assert calculate_order_total(order_list, promo_code, is_vip) == attended_result
