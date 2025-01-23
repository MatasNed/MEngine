import pytest

from src.mengine.validtors.http_validator import HTTPValidator

@pytest.fixture(scope='class')
def mock_validator():
    return HTTPValidator()

class TestHTTPValidator:

    def test_validate_version(self, mock_validator):
        valid_version = "HTTP/1.1"
        assert mock_validator.validate_version(valid_version) == valid_version

    def test_validate_version_invalid_type(self, mock_validator):
        invalid_input = 12
        # Read this https://docs.pytest.org/en/stable/how-to/usage.html

        #assert