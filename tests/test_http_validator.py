import pytest

from src.mengine.exceptions.exceptions import ValidationError
from src.mengine.validtors.http_validator import HTTPValidator

@pytest.fixture(scope='class')
def http_validator():
    return HTTPValidator()

class TestHTTPValidator:
    # Define the parameter set once
    INVALID_VERSION_PARAMS = [
        (12, "Invalid version type. Expected a string."),
        (None, "Invalid version type. Expected a string."),
        ([], "Invalid version type. Expected a string."),
        ({}, "Invalid version type. Expected a string."),
        (123.456, "Invalid version type. Expected a string."),
        (True, "Invalid version type. Expected a string."),
    ]

    def test_validate_version(self, http_validator):
        valid_version = "HTTP/1.1"

        assert http_validator.validate_version(valid_version) == valid_version

    @pytest.mark.parametrize("invalid_input, expected_message", INVALID_VERSION_PARAMS)
    def test_validate_version_invalid_type(self, invalid_input, expected_message, http_validator):
        with pytest.raises(ValidationError) as res:
            http_validator.validate_version(invalid_input)

            assert str(res) == expected_message


    def test_validate_method(self, http_validator):
        valid = "GET"

        assert http_validator.validate_method(valid) == valid

    @pytest.mark.parametrize("invalid_input, expected_message", INVALID_VERSION_PARAMS)
    def test_validate_method_invalid_type(self, invalid_input, expected_message, http_validator):
        with pytest.raises(ValidationError) as result:
            http_validator.validate_method(invalid_input)

            assert str(result) == expected_message

    def test_validate_payload(self, http_validator):
        some_bytes = b"bytes"

        assert http_validator.validate_payload(some_bytes) == some_bytes

    def test_validate_payload_invalid_input(self, http_validator):
        not_bytes = 12

        with pytest.raises(ValidationError):
            http_validator.validate_payload(not_bytes)