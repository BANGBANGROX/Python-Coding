def calculate_tax(income: float) -> float:
    if income <= 700000:
        return 0

    slabs = [5, 10, 15, 20]
    slab_size = 300000
    income -= slab_size
    final_tax = 0

    for slab in slabs:
        taxable_income = min(income, slab_size)
        final_tax += slab_size * slab / 100
        income -= taxable_income
        if income <= 0:
            break

    if income > 0:
        final_tax += income * 30 / 100

    return final_tax


if __name__ == "__main__":
    income = int(input())
    print(calculate_tax(income))
