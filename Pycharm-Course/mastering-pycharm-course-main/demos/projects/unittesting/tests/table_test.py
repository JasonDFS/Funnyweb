import pytest

from app import core


def test_there_are_tables_available():
    choice = 1
    tables = core.find_available(choice)

    assert len(tables) >= 1


def test_table_can_be_booked():
    tables = [t for t in core.all_tables() if not t.is_booked]
    table = tables[0]

    booked = core.book_table(table.table_id)

    assert booked
    assert booked.is_booked
    assert booked.table_id == table.table_id


def test_cannot_book_a_nonexistant_table():
    with pytest.raises(core.EntityNotFoundError):
        core.book_table("THIS IS NOT AN ID ;)")


def test_cannot_book_a_booked_table():
    table = [t for t in core.all_tables() if not t.is_booked][0]
    core.book_table(table.table_id)

    with pytest.raises(core.TableUnavailableError):
        core.book_table(table.table_id)
