from src.mengine.exceptions.exceptions import ValidationError

class HTTPValidator:

    VALID_METHODS = {"GET", "POST"}
    VALID_VERSIONS = {"HTTP/1.0", "HTTP/1.1"}

    @staticmethod
    def validate_method(method: str) -> str:
        """
        Validates the HTTP method

        Args:
            method (str): The http method to validate

        Returns:
            str: The validated HTTP method in uppercase

        Raises:
            ValidatorError: if invalid
        """
        if not isinstance(method, str):
            raise ValidationError(field="method", message="Method must be a string")
        method = method.upper()
        if method not in HTTPValidator.VALID_METHODS:
            raise ValidationError(field="method", message=f"unsupported method type {method}")
        return method

    @staticmethod
    def validate_version(version: str) -> str:
        """
        Validates HTTP version

        Args:
            version (str): the version of http

        Returns:
            str: the validated HTTP version

        Raises:
            ValidatorError: if invalid
        """
        if not isinstance(version, str):
            raise ValidationError(field="version", message="Version be of type string")
        if version not in HTTPValidator.VALID_VERSIONS:
            raise ValidationError(field="version", message="Version must be 1.0 or 1.1")
        return version

    @staticmethod
    def validate_payload(payload: bytes) -> bytes:
        """
        Validate the payload.

        Args:
            payload (bytes): The payload to validate.

        Returns:
            bytes: The validated payload.

        Raises:
            ValidationError: If the payload is invalid.
        """
        if not isinstance(payload, bytes):
            raise ValidationError(field="payload", message="Payload must be bytes")
        return payload
