import pytest

from absence import can_sit_exam, status


@pytest.mark.parametrize(
    "absences, expected",
    [
        (0, True),
        (5, True),
        (9, False),
    ],
)
def test_can_sit_exam(absences, expected):
    assert can_sit_exam(absences) == expected


@pytest.mark.parametrize(
    "absences, expected",
    [
        (0, "Allowed"),
        (3, "Allowed"),
        (9, "Blocked"),
    ],
)
def test_status(absences, expected):
    assert status(absences) == expected
