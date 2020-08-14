import pandas as pd
import warnings

from tac.date_cleaner import tidy_time_string


def test_tidy_time_string():
    """
    Tests edge-cases for tidy_time_string.
    """
    # TODO - add more test strings (both expected passes and fails).
    # TODO - run test functions through pytest/github actions
    # TODO - test this test

    test_strings = {
        '29 Feb 1957': (pd.NaT, 'not_converted'),  # There was no 29th Feb this year
        '25-27 june': (pd.NaT, 'not_converted'),  # Pandas converts this str by default, but it has no year.
        '03 03 1920': (pd.to_datetime('03-03-1920'), 'exact'),
        '01 01 1920': (pd.to_datetime('02-01-1920'), 'exact'),  # EXPECTED TO FAIL # TODO: remove, and instead, check it raises a warning https://docs.pytest.org/en/6.0.1/warnings.html#warns
        # '1-3 March 1920': (pd.to_datetime('02-03-1920', dayfirst=True), 'centered')

    }

    for string_key in test_strings.keys():
        (a_date, a_date_status) = test_strings[string_key]
        date_info = tidy_time_string(string_key)
        try:
            assert (date_info == (a_date, a_date_status))
        except AssertionError:
            warnings.warn(f"`{string_key}` was converted to {date_info}, not {(a_date, a_date_status)} as was expected.")

    return


if __name__ == "__main__":
    test_tidy_time_string()
