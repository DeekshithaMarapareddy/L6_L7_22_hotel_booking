
import pytest
from hotel_booking import booking_cost, cancellation_refund, room_upgrade


# BOOKING COST TESTS

def test_standard_two_nights():
    assert booking_cost("standard", 2, 2, False) == 4000


def test_invalid_room():
    with pytest.raises(ValueError, match="unknown room"):
        booking_cost("premium", 2, 2, False)


def test_invalid_nights():
    with pytest.raises(ValueError, match="invalid nights"):
        booking_cost("standard", 0, 2, False)


def test_peak_season_extra_guest_weekly_discount():
    assert booking_cost("deluxe", 7, 3, True) == 30713


def test_extra_guest_without_weekly_discount():
    assert booking_cost("standard", 1, 3, False) == 2500


def test_weekly_discount_without_peak_season():
    assert booking_cost("standard", 7, 2, False) == 12600


# CANCELLATION REFUND TESTS

def test_full_refund():
    assert cancellation_refund(1000, 10, False) == 1000


def test_partial_refund_non_member():
    assert cancellation_refund(1000, 2, False) == 500


def test_zero_refund_non_member():
    assert cancellation_refund(1000, 1, False) == 0


def test_zero_refund_with_member_bonus():
    assert cancellation_refund(1000, 1, True) == 250


def test_partial_refund_with_member_bonus():
    assert cancellation_refund(1000, 2, True) == 750


# ROOM UPGRADE TESTS

def test_no_rooms_available():
    assert room_upgrade("standard", True, 0) == "standard"


def test_standard_member_upgrade():
    assert room_upgrade("standard", True, 1) == "deluxe"


def test_standard_non_member_no_upgrade():
    assert room_upgrade("standard", False, 1) == "standard"


def test_deluxe_member_upgrade():
    assert room_upgrade("deluxe", True, 1) == "suite"


def test_deluxe_non_member_no_upgrade():
    assert room_upgrade("deluxe", False, 1) == "deluxe"


def test_suite_member_no_upgrade():
    assert room_upgrade("suite", True, 1) == "suite"
