"""
AttendX Attendance Test
Demonstration test for attendance data validation.

Note:
This script does not connect to a real attendance application.
"""


def test_mark_attendance():
    student_id = "STU001"
    attendance_status = "Present"

    # Check that a student ID is provided.
    assert student_id != "", "Student ID must not be empty"

    # Check that the attendance status is valid.
    assert attendance_status in ["Present", "Absent"], (
        "Attendance status must be Present or Absent"
    )

    print("PASS: Attendance data is valid.")


def test_invalid_attendance_status():
    attendance_status = "Unknown"

    # Verify that an unsupported status is detected.
    assert attendance_status not in ["Present", "Absent"]

    print("PASS: Invalid attendance status detected.")


if __name__ == "__main__":
    test_mark_attendance()
    test_invalid_attendance_status()
    print("Attendance demonstration tests completed.")