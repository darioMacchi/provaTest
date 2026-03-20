class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """
        Classe che contiene un prodotto.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

def calculate_order_total(
        order: 'list[Product]',
        promo_code : str,
        is_vip : bool
    ) -> float:
    """
    Il seguente codice calcola il prezzo di un ordine date alcune regole di business
    - se l'ordine è vuoto, il totale è 0
    - il codice promo code "SAVE10" sconta 10 euro, ma solo se il subtotale è almeno 100 euro
    - spedizione gratuita per tutti sopra i 50 euro
    - i clienti VIP pagano 2 euro di spedizione se spendono meno di 50 euro mentre tutti gli altri 5 euro
    """
    if not order:
        return 0.0

    # compute total
    subtotal = sum(item.price * item.quantity for item in order)

    # discount if applicable
    if promo_code == "SAVE10" and subtotal >= 100.0:
        subtotal -= 10.0

    # shipping cost
    shipping = 0.0
    if subtotal < 50.0:
        if is_vip:
            shipping = 2.0
        else:
            shipping = 5.0

    return subtotal + shipping


def main():
    order : 'list[Product]' = [
        Product("Scarpe", 25.0, 3),
        Product("Cappello", 15.0, 2)
    ]
    total = calculate_order_total(order, promo_code="SAVE10", is_vip=True)
    print(f"Total order cost: {total:.2f} euro")

if __name__ == "__main__":
    main()
