
from hypothesis import given, strategies as st
from hotel_booking import nights_stayed, room_floor, booking_label


# 1. Fuzz testing: nights_stayed()
@given(st.text() | st.none() | st.integers())
def test_nights_stayed_no_crash(s):
    nights_stayed(s)


@given(
    st.integers(min_value=1, max_value=30),
    st.integers(min_value=1, max_value=31)
)
def test_nights_stayed_valid(check_in, check_out):
    if check_out > check_in:
        assert nights_stayed(f"{check_in}-{check_out}") == check_out - check_in


# 2. Fuzz testing: room_floor()
@given(st.text() | st.none() | st.integers())
def test_room_floor_no_crash(s):
    room_floor(s)


@given(
    st.integers(min_value=1, max_value=9),
    st.integers(min_value=0, max_value=99)
)
def test_room_floor_valid(floor, room):
    room_code = f"D-{floor}{room:02d}"
    assert room_floor(room_code) == floor


# 3. Fuzz testing: booking_label()
@given(st.text() | st.none() | st.integers())
def test_booking_label_no_crash(s):
    booking_label(s)


@given(
    st.lists(
        st.text(
            alphabet="abcdefghijklmnopqrstuvwxyz",
            min_size=1,
            max_size=15
        ),
        min_size=1,
        max_size=5
    )
)
def test_booking_label_valid(names):
    names_csv = ", ".join(names)
    expected = names[0][0].upper() + names[0][1:] + " +" + str(len(names) - 1)

    assert booking_label(names_csv) == expected
