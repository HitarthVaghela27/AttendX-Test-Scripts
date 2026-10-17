"""
AttendX Login Test
Demonstration test for login input validation.

Note:
This is a standalone demonstration. It does not connect
to a real AttendX application or authenticate a user.
"""


def test_login_with_valid_credentials():
    username = "student001"
    password = "ValidPassword123"

    # Check that the required login inputs are present.
    assert username != "", "Username must not be empty"
    assert password != "", "Password must not be empty"

    print("PASS: Username and password inputs are present.")


def test_login_with_empty_username():
    username = ""
    password = "ValidPassword123"

    # An empty username should be detected.
    assert username == "", "Username should be empty for this test"

    print("PASS: Empty username test input detected.")
    

if __name__ == "__main__":
    test_login_with_valid_credentials()
    test_login_with_empty_username()
    print("Login demonstration tests completed.")
    print("PASS: Login input validation completed.")