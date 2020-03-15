import pytest
import find_single_letter


class testing_data:
    ligal_test_data = [
        # alpha_str , expected
        ('aabcc', 'b'),
        ('aabbcddee', 'c'),
        ('xjieiaajx', 'e'),
        ('AaABbBb', 'a'),
        ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', 'b'),
        ('aabbccddeeffgghhiijjkkllmmnnooAppqqrrssttuuvvwwxxyyzzBBCCDDEEFFGGHHIIJJKKLLMMOOPPQQRRSSTTUUVVWWXXYY', 'A')
    ]
    format_error_test_data = [
        # alpha_str , expected
        ('*aabbB', 'The input format error!'),
        ('AA&BBC', 'The input format error!'),
        ('aabbc^', 'The input format error!'),
        ('!aabbB', 'The input format error!'),
        ('AA@BBC', 'The input format error!'),
        ('aabbc#', 'The input format error!'),
        ('$aabbB', 'The input format error!'),
        ('AA%BBC', 'The input format error!'),
        ('aabbc_', 'The input format error!'),
    ]
    too_more_test_data = [
        # alpha_str , expected
        ('abccddee', 'More than one single letter!'),
        ('AjiiooIJIJ', 'More than one single letter!'),
        ('asdfijiewr', 'More than one single letter!'),
        ('ASDFOIJIdsjfiooi', 'More than one single letter!')
    ]
    no_single_letter_test_data = [
        # alpha_str , expected
        ('aabbiikkjjddooee', 'No single letter in input string!'),
        ('aabbiikkjjddooeeaabbiikkjjddooeeaabbiikkjjddooeeaabbiikkjjddooeebbiikkjjddooeeaabbiikkjjddooeeUUII',
         'No single letter in input string!')
    ]


@pytest.mark.parametrize('alpha_str , expected', testing_data.ligal_test_data)
def test_ligal_parameter(alpha_str, expected):
    # arrage

    # act
    result = find_single_letter.find_single_letter(alpha_str)

    # assert
    assert result == expected


@pytest.mark.parametrize('alpha_str , expected', testing_data.format_error_test_data)
def test_input_format_error_parameter(alpha_str, expected):
    # arrage

    # act
    result = find_single_letter.find_single_letter(alpha_str)

    # assert
    assert result == expected


@pytest.mark.parametrize('alpha_str , expected', testing_data.too_more_test_data)
def test_too_more_single_letter_parameter(alpha_str, expected):
    # arrage

    # act
    result = find_single_letter.find_single_letter(alpha_str)

    # assert
    assert result == expected


@pytest.mark.parametrize('alpha_str , expected', testing_data.no_single_letter_test_data)
def test_no_single_letter_parameter(alpha_str, expected):
    # arrage

    # act
    result = find_single_letter.find_single_letter(alpha_str)

    # assert
    assert result == expected
