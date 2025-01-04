import sqlite3
import pytest
from project import set_new_category, delete_category, reset_expenses, get_total_value, update_category


@pytest.fixture()
def setup_db():
    con = sqlite3.connect(":memory:")
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL UNIQUE,
        money REAL NOT NULL,
        date TEXT NOT NULL
    )
    """)
    con.commit()

    yield con, cur

    cur.close()
    con.close()


def test_set_new_category(setup_db):
    con, cur = setup_db

    result = set_new_category(con, cur, "test_category", 100.0, "2024-10-02")
    assert result == "test_category was added successfully with amount $100.00"

    cur.execute("SELECT * FROM expenses WHERE category = 'test_category'")
    row = cur.fetchone()
    assert row is not None
    assert row[1] == "test_category"
    assert row[2] == 100.0


def test_delete_category(setup_db):
    con, cur = setup_db

    set_new_category(con, cur, "delete_category", 50.0, "2024-10-02")

    result = delete_category(con, cur, "delete_category")
    assert result == "delete_category was successfully deleted."

    cur.execute("SELECT * FROM expenses WHERE category = 'delete_category'")
    row = cur.fetchone()
    assert row is None


def test_reset_expenses(setup_db):
    con, cur = setup_db

    set_new_category(con, cur, "reset_category", 50.0, "2024-10-02")

    result = reset_expenses(con, cur, "yes")
    assert result == "Your expenses tracker buddy has been successfully reset"

    cur.execute("SELECT * FROM expenses")
    rows = cur.fetchall()
    assert len(rows) == 0


def test_get_total_value(setup_db):
    con, cur = setup_db

    set_new_category(con, cur, "category_1", 100.0, "2024-10-02")
    set_new_category(con, cur, "category_2", 200.0, "2024-10-02")

    result = get_total_value(cur)
    assert result == "Total: $300.00"


def test_update_category(setup_db):
    con, cur = setup_db

    set_new_category(con, cur, "update_category", 100.0, "2024-10-02")

    result = update_category(con, cur, 150.0, "2024-10-02", "update_category")
    assert result == "update_category was updated with amount $150.00"

    cur.execute("SELECT * FROM expenses WHERE category = 'update_category'")
    row = cur.fetchone()
    assert row is not None
    assert row[2] == 150.0


if __name__ == "__main__":
    pytest.main()
