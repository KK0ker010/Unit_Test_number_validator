"""
TESZTELENDŐ FELADAT - NumberValidator osztály unit tesztek

A feladat: Írj unit teszteket a NumberValidator osztály metódusaihoz!
Használd a különböző assert típusokat!
"""

# import modul
# from file import ClassName


# ============================================================================
# FELADAT: Írd meg az alábbi teszteket!
# ============================================================================

def test_is_even_equal():
    """1.1 Assert equal - páros szám ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_even metódust páros számmal
    # TODO: Ellenőrizd, hogy az eredmény True
    pass


def test_is_even_not_equal():
    """1.2 Assert not equal - páratlan szám ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_even metódust páratlan számmal
    # TODO: Ellenőrizd, hogy az eredmény NEM egyenlő True-val
    pass


def test_is_even_with_zero():
    """1.3 Speciális eset - nulla kezelése"""
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_even metódust 0-val
    # TODO: Ellenőrizd, hogy az eredmény True-e?
    pass


def test_is_positive_greater_than():
    """2.1 Assert > - pozitív szám ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_positive metódust pozitív számmal
    # TODO: Ellenőrizd, hogy az eredmény True-e?
    pass


def test_is_positive_with_negative():
    """2.2 Negatív szám ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_positive metódust pozitív számmal
    # TODO: Hívd meg az is_positive metódust negatív számmal
    # TODO: Ellenőrizd, hogy az eredmény True vagy False?
    pass


def test_is_in_range_less_than():
    """3.1 Assert <, <= - tartományon belüli ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_in_range metódust egy számmal, ami a tartományban van
    # TODO: Ellenőrizd, hogy az eredmény True
    pass


def test_is_in_range_out_of_range():
    """3.2 Assert <, <= - tartományon kívüli ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_in_range metódust egy számmal, ami a tartományon kívül van
    # TODO: Ellenőrizd, hogy az eredmény True
    pass


def test_get_absolute_value_isinstance():
    """4. Assert isinstance - típus ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg a get_absolute_value metódust negatív számmal (pl. -5)
    # TODO: Ellenőrizd, hogy az eredmény integer típusú
    # TODO: Ellenőrizd, hogy az eredmény NEM string típusú
    pass


def test_is_divisible_by_true_false():
    """5. Assert True/False - oszthatóság ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_divisible_by metódust olyan számmal, ami osztható egymással
    # TODO: Ellenőrizd, hogy az eredmény True
    # TODO: Hívd meg olyan számmal, ami NEM osztható (maradékos osztás)
    # TODO: Ellenőrizd, hogy az eredmény False
    pass


def test_square_none():
    """6. Assert None - None ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg a square metódust None értékkel
    # TODO: Ellenőrizd, hogy az eredmény NEM None
    # TODO: Ellenőrizd, hogy az eredmény 0-e?
    pass


def test_is_prime_multiple_asserts():
    """7. Több assert egy tesztben - prímszám ellenőrzés"""
    # TODO: Hozz létre egy NumberValidator példányt
    # TODO: Hívd meg az is_prime metódust prímszámmal
    # TODO: Ellenőrizd több assert-tel:
    #      - Az eredmény True
    #      - Az eredmény boolean típusú
    #      - Az eredmény nem egyenlő False-szal
    pass

