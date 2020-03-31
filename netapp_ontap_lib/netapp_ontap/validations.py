"""

Copyright &copy; 2019 NetApp Inc.
All rights reserved.

This module holds validation functions that can be used for field level validation

"""

from typing import Callable, List, TypeVar

from marshmallow import ValidationError  # type: ignore


T = TypeVar("T")  # pylint: disable=invalid-name


def enum_validation(choices: List[T]) -> Callable[[T], None]:
    """Verifies that the provided value is one of the possible choices

    Args:
        choices: The list of choices

    Returns:
        A callable function which validates its input value as being part of the set of choices.
    """

    def _validate(value: T) -> None:
        lower_choices = [str(c).lower() for c in choices]
        lower_value = str(value).lower()
        if lower_value not in lower_choices:
            raise ValidationError('"%s" is not one of %s' % (lower_value, lower_choices))

    return _validate


def len_validation(minimum: int = 0, maximum: int = None) -> Callable[[str], None]:
    """Verify the given string is within the acceptable length limits

    Args:
        minimum: The minimum length the string can be
        maximum: The maximum length the string can be. If unset, maximum is not checked.

    Returns:
        A callable function which validates its input as being between minimum and maximum.
    """

    def _validate(value: str) -> None:
        if not minimum <= len(value):
            raise ValidationError(
                '"%s" must be greater than or equal to %s characters.'
                % (value, minimum)
            )
        if maximum:
            if not len(value) <= maximum:
                raise ValidationError(
                    '"%s" must be less than or equal to %s characters.'
                    % (value, maximum)
                )

    return _validate

def integer_validation(minimum: int = None, maximum: int = None) -> Callable[[int], None]:
    """Verify that the given value is within the acceptable range

    Args:
        minimum: The minimum value the integer can be
        maximum: The maximum value the integer can be

    Returns:
        A callable function which validates its inputs as being between minimum and maximum.
    """

    def _validate(value: int) -> None:
        if minimum:
            if not minimum <= value:
                raise ValidationError(
                    '"%d" must be greater than or equal to %d.'
                    % (value, minimum)
                )
        if maximum:
            if not value <= maximum:
                raise ValidationError(
                    '"%d" must be less than or equal to %d.'
                    % (value, maximum)
                )

    return _validate
