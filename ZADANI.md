# 🎬 Zadání: Movie Explorer — Python Flask & SQLite

**Předmět:** Python · SQLite · Flask · Jinja2  
**Úroveň:** Začátečník (se základní znalostí CRUD operací)  
**Odhadovaný čas:** 3–4 hodiny

---

## 📋 Přehled

Vytvoříte aplikaci **Movie Explorer** — jednoduchou webovou aplikaci, kde uživatelé mohou procházet a filtrovat katalog filmů uložený v databázi SQLite. Aplikace využívá backendový framework **Flask** a zobrazuje výsledky pomocí **Jinja2 HTML šablon** se stylingem **Bootstrap**.

Většina struktury je již připravena. Vaším úkolem je doplnit chybějící části, které jsou jasně označeny komentáři `TODO`.

---

## 📁 Struktura projektu

```
movie_explorer/
│
├── setup_db.py          ← Spusťte jednou pro vytvoření a naplnění movies.db
├── app.py               ← Flask aplikace  (hlavní část vašeho kódu)
├── movies.db            ← Vytvořeno skriptem setup_db.py (NEUPRAVUJTE přímo)
│
└── templates/
    ├── base.html        ← Sdílené rozložení stránky s Bootstrapem  (připraveno)
    └── index.html       ← Formulář filtrů + tabulka výsledků   (vaše šablona)
```

---

## 🗄️ Schéma databáze

Tabulka `movies` obsahuje tyto sloupce:

| Sloupec    | Typ     | Popis                           |
|------------|---------|---------------------------------|
| `id`       | INTEGER | Primární klíč (automatický)     |
| `title`    | TEXT    | Název filmu                     |
| `genre`    | TEXT    | např. Drama, Sci-Fi, Horror …   |
| `year`     | INTEGER | Rok vydání (1970 – 2024)        |
| `rating`   | REAL    | Hodnocení ve stylu IMDb (6.5 – 9.3) |
| `director` | TEXT    | Jméno režiséra                  |
| `duration` | INTEGER | Délka v minutách                |
| `country`  | TEXT    | Země původu                     |
| `language` | TEXT    | Hlavní jazyk                    |

Před spuštěním aplikace jednou spusťte `setup_db.py`:

```bash
python setup_db.py
python app.py
```

Poté otevřete **http://127.0.0.1:5000** v prohlížeči.

---

## 🔧 Vaše úkoly

Procházejte TODOs postupně. V souboru `app.py` je **7 TODOs** a v `index.html` jsou **4 TODOs**.

---

### `app.py` — Backend TODOs

#### TODO 1 — Načtení unikátních žánrů

Uvnitř funkce `get_filter_options()` napište SELECT dotaz, který vrátí všechny unikátní hodnoty žánru z tabulky `movies`, seřazené **abecedně**.

```python
# Očekávaný výsledek (seznam objektů Row):
# ["Action", "Animation", "Comedy", "Crime", ...]
```

#### TODO 2 — Načtení unikátních režisérů

Stejně jako TODO 1, ale pro sloupec `director`.

#### TODO 3 — Vyhledávání podle názvu

Pokud proměnná `search` není prázdná, přidejte podmínku tak, aby dotaz vrátil pouze filmy, jejichž **název obsahuje** hledaný text. Shoda musí být **bez rozlišení velikosti písmen** — hledání `"dark"` musí najít `"The Dark Knight"`.

```python
# Nápověda: UPPER(title) LIKE UPPER(?)   s hodnotou parametru  "%" + search + "%"
```

#### TODO 4 — Filtr žánru

Pokud `genre` není prázdné, přidejte podmínku, která vrátí pouze filmy odpovídající danému žánru přesně (bez rozlišení velikosti písmen).

#### TODO 5 — Filtr režiséra

Stejně jako TODO 4, ale pro sloupec `director`.

#### TODO 6 — Rozsah roku a hodnocení

Přidejte čtyři podmínky tak, aby výsledky respektovaly hodnoty `year_min`, `year_max`, `rating_min` a `rating_max`.

#### TODO 7 — Spuštění dotazu a načtení výsledků

Spusťte sestavený dotaz se seznamem `params`, načtěte všechny řádky a uložte je do proměnné `movies`.

---

### `index.html` — TODOs v šabloně

#### TODO A — Rozbalovací seznam žánrů

Nahraďte komentář `<!-- your loop goes here -->` Jinja2 smyčkou `{% for %}`, která pro každý žánr vygeneruje tag `<option>`. Možnost odpovídající `selected_genre` musí mít HTML atribut `selected`.

```html
<!-- Příklad výstupu, když je vybrán žánr "Drama": -->
<option value="Action">Action</option>
<option value="Drama" selected>Drama</option>
...
```

#### TODO B — Rozbalovací seznam režisérů

Stejně jako TODO A, ale pro seznam režisérů a proměnnou `selected_director`.

#### TODO C — Prázdný stav

Obalte kontejner tabulky `<div class="card ...">` blokem `{% if movies %}` / `{% else %}`. Když je seznam `movies` prázdný, zobrazte místo tabulky přívětivé Bootstrap upozornění:

```html
<div class="alert alert-warning">Žádné filmy neodpovídají zadaným filtrům. Zkuste rozšířit vyhledávání.</div>
```

#### TODO D — Smyčka řádků filmů

Nahraďte dva statické ukázkové řádky `<tr>` smyčkou `{% for %}` přes proměnnou `movies`. Zobrazte každý sloupec v příslušné buňce tabulky. Pro buňku **hodnocení** použijte správnou CSS třídu podle hodnoty:

| Hodnocení    | CSS třída                 |
|--------------|---------------------------|
| ≥ 8.5        | `rating-pill rating-high` |
| ≥ 7.0        | `rating-pill rating-mid`  |
| < 7.0        | `rating-pill rating-low`  |

Pro **délku** převeďte minuty do formátu `XhYm` pomocí Jinja2 výrazů:

```
{{ movie["duration"] // 60 }}h {{ movie["duration"] % 60 }}m
```

---

## 🎬 Scénáře filtrování

Jakmile aplikace funguje, otestujte ji pomocí těchto konkrétních scénářů. Každý by měl vrátit uvedené výsledky.

### Scénář 1 — Filmografie Christophera Nolana
**Režisér:** Christopher Nolan · ostatní filtry ve výchozím nastavení

| Název                    | Rok  | Hodnocení |
|--------------------------|------|-----------|
| Oppenheimer              | 2023 | 8.3       |
| The Dark Knight          | 2008 | 9.0       |
| Inception                | 2010 | 8.8       |
| Interstellar             | 2014 | 8.7       |

> ✅ **Kontrola:** Přesně 4 filmy. Seřazeno podle hodnocení sestupně.

---

### Scénář 2 — Moderní Sci-Fi (2015 – 2024)
**Žánr:** Sci-Fi · **Rok:** 2015 – 2024 · ostatní filtry ve výchozím nastavení

| Název                    | Rok  | Hodnocení |
|--------------------------|------|-----------|
| Dune: Part Two           | 2024 | 8.5       |
| Everything Everywhere    | 2022 | 7.8       |
| Arrival                  | 2016 | 7.9       |

> ✅ **Kontrola:** Přesně 3 filmy. Interstellar (2014) se NESMÍ zobrazit.

---

### Scénář 3 — Vysoce hodnocené kriminální filmy a thrillery
**Žánr:** Crime · **Hodnocení:** 8.5 – 10.0

| Název              | Rok  | Hodnocení |
|--------------------|------|-----------|
| The Godfather      | 1972 | 9.2       |
| Pulp Fiction       | 1994 | 8.9       |
| Goodfellas         | 1990 | 8.7       |
| City of God        | 2002 | 8.6       |

> ✅ **Kontrola:** Přepněte žánr na Thriller — měli byste dostat Parasite a Silence of the Lambs.

---

### Scénář 4 — Krátké filmy do 110 minut (bonusová kontrola)
**Hledání názvu:** _(prázdné)_ · **Délka:** Pomocí tabulky vizuálně identifikujte filmy ≤ 110 min.  
V nefiltrovaném seznamu by měly být viditelné tyto filmy:

| Název                    | Délka  |
|--------------------------|--------|
| The Grand Budapest Hotel | 1h 40m |
| Coco                     | 1h 45m |
| Whiplash                 | 1h 47m |

> ✅ **Kontrola:** Sloupec délky zobrazuje formát `XhYm` správně pro všechny řádky.

---

### Scénář 5 — Cizojazyčné klenoty
**Hledání názvu:** `"a"` · **Hodnocení:** 8.0 – 10.0 · **Rok:** 1990 – 2010

Výsledky by měly obsahovat: `Amélie`, `Spirited Away`, `City of God`

> ✅ **Kontrola:** Vyhledávání nerozlišuje velikost písmen — `"A"` a `"a"` vrátí stejné výsledky.

---

### Scénář 6 — Prázdný stav
Nastavte **Žánr** na `Horror` a **Hodnocení** na `9.0 – 10.0`.

> ✅ **Kontrola:** Žádný horor v databázi nemá hodnocení ≥ 9.0. Místo prázdné tabulky by se měla zobrazit vaše hláška „žádné výsledky".

---

## 💡 Klíčové nápovědy

- `conn.row_factory = sqlite3.Row` umožňuje psát `movie["title"]` místo `movie[0]`
- V Jinja2 přistupujte k řádkům slovníkovým způsobem: `movie["column"]` nebo tečkovou notací `movie.column`
- Formulář používá `method="GET"` — hodnoty filtrů se zobrazují v adresním řádku prohlížeče, což je skvělé pro ladění
- Chcete-li zkontrolovat, co formulář odesílá, podívejte se na URL po kliknutí na **Použít filtry**
- Nikdy nespojujte uživatelský vstup přímo do SQL řetězce. Vždy používejte zástupné znaky `?` se seznamem `params`

---

## ✅ Bonusové výzvy

1. **Řazení** — přidejte `<select>`, který umožní uživateli zvolit řazení: podle hodnocení (sestupně), podle roku (nejnovější) nebo podle názvu (A→Z)
2. **Filtr jazyka** — přidejte rozbalovací seznam jazyka vedle filtrů žánru a režiséra
3. **Počet filmů podle žánru** — u každé možnosti žánru v rozbalovacím seznamu zobrazte počet filmů, např. `Drama (8)`
4. **Zvýraznění hledaného výrazu** — v tabulce výsledků zvýrazněte tučně odpovídající část názvu pomocí Jinja2 filtru `replace()`

---

## 📤 Kontrolní seznam odevzdání

- [ ] `setup_db.py` proběhne bez chyb
- [ ] `app.py` se spustí a stránka se načte na `http://127.0.0.1:5000`
- [ ] Všech 6 scénářů filtrování vrátí očekávané výsledky
- [ ] Hláška prázdného stavu se zobrazí pro Scénář 6
- [ ] Délka je ve všech řádcích zobrazena ve formátu `XhYm`
- [ ] Štítky hodnocení používají správnou barvu pro vysoké / střední / nízké hodnocení
- [ ] Žádný uživatelský vstup není přímo spojen do SQL řetězce

---

*Hodně štěstí — a užijte si filmy! 🍿*
