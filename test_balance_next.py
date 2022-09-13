from main import balance_next, Stack
import pytest


FIXTURE_test_name_by_number = [
    ('(((([{}]))))', Stack([]), 'Сбалансированно'),
    ('[([])((([[[]]])))]{()}', Stack([]), 'Сбалансированно'),
    ('{{[()]}}', Stack([]),  'Сбалансированно'),
    ('}{}', Stack([]),  'Несбалансированно'),
    ('{{[(])]}}', Stack([]), 'Несбалансированно'),
    ('[[{())}]', Stack([]), 'Несбалансированно')
]


@pytest.mark.parametrize('sequence_brackets, s, result', FIXTURE_test_name_by_number)
def test_name_by_number(sequence_brackets, s, result):
    assert balance_next(sequence_brackets, s) == result
