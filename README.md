# Unit Tesztelési Feladat - NumberValidator

## 📋 Feladat leírása

A feladat során egy `NumberValidator` osztályhoz kell unit teszteket írnod. Az osztály különböző matematikai műveleteket és ellenőrzéseket végez számokkal.


## ✅ Tesztelendő metódusok

### 1. `is_even(number)` - Páros szám ellenőrzés
- **Bemenet:** Egy szám
- **Kimenet:** `True`, ha páros, `False` ha páratlan
- **Tesztelendő esetek:**
  - Páros szám
  - Páratlan szám
  - `None` érték kezelése

`1.1 test_is_even_equal()`

`1.2 test_is_even_not_equal()`

`1.3 test_is_even_with_zero()`

### 2. `is_positive(number)` - Pozitív szám ellenőrzés
- **Bemenet:** Egy szám
- **Kimenet:** `True`, ha pozitív, `False` ha nem pozitív
- **Tesztelendő esetek:**
  - Pozitív szám
  - Negatív szám
  - Nulla
  - `None` érték kezelése
  
  `2.1 test_is_positive_greater_than()`
  
  `2.2 test_is_positive_with_negative()`

### 3. `is_in_range(number, min_val, max_val)` - Tartomány ellenőrzés
- **Bemenet:** Egy szám, minimum érték, maximum érték
- **Kimenet:** `True`, ha a szám a tartományban van, `False` ha nincs
- **Tesztelendő esetek:**
  - Szám a tartományban
  - Szám a tartományon kívül
  - Szám a határon (pl. 1 vagy 10, 1, 10)
  - `None` érték kezelése

`3.1 test_is_in_range_less_than()`

`3.2 test_is_in_range_out_of_range()`

### 4. `get_absolute_value(number)` - Abszolút érték
- **Bemenet:** Egy szám
- **Kimenet:** A szám abszolút értéke
- **Tesztelendő esetek:**
  - Pozitív szám (pl. 5 → 5)
  - Negatív szám (pl. -5 → 5)
  - Nulla (0 → 0)
  - `None` érték kezelése (0-t ad vissza)

### 5. `is_divisible_by(number, divisor)` - Oszthatóság ellenőrzés
- **Bemenet:** Egy szám és egy osztó
- **Kimenet:** `True`, ha osztható, `False` ha nem
- **Tesztelendő esetek:**
  - Osztható szám
  - Nem osztható szám
  - Nullával való osztás (`False`-t ad vissza)
  - `None` érték kezelése

### 6. `square(number)` - Négyzetre emelés
- **Bemenet:** Egy szám
- **Kimenet:** A szám négyzete
- **Tesztelendő esetek:**
  - Pozitív szám (pl. 5 → 25)
  - Negatív szám (pl. -5 → 25)
  - Nulla (0 → 0)
  - `None` érték kezelése (0-t ad vissza)

### 7. `is_prime(number)` - Prímszám ellenőrzés
- **Bemenet:** Egy szám
- **Kimenet:** `True`, ha prímszám, `False` ha nem
- **Tesztelendő esetek:**
  - Prímszám (pl. 2, 3, 5, 7, 11, 13)
  - Nem prímszám (pl. 4, 6, 8, 9, 10)
  - 1 vagy kisebb szám (`False`)
  - `None` érték kezelése

## 📝 Assert típusok, amiket használnod kell

1. **`assert ==`** - Egyenlőség ellenőrzés
2. **`assert !=`** - Nem egyenlő ellenőrzés
3. **`assert >, <, >=, <=`** - Összehasonlítás
4. **`assert is True/False`** - Boolean érték ellenőrzés
5. **`assert is None / is not None`** - None ellenőrzés
6. **`assert isinstance()`** - Típus ellenőrzés
7. **Több assert egy tesztben** - Komplex ellenőrzések

## 💡 Tippek

- Minden tesztfüggvényt `test_` prefixszel kezdj!
- Használj beszédes függvényneveket (pl. `test_is_even_with_zero`)
- Minden tesztben hozz létre egy új `NumberValidator()` példányt
- Ne feledd a szélsőséges eseteket (0, negatív számok, `None`)

## 🔧 Telepítés és futtatás

1. Telepítsd a pytest-et (ha még nincs):
   ```bash
   pip install pytest
   ```

2. Futtasd a teszteket:
   ```bash
   python -m pytest test_number_validator.py -v
   ```