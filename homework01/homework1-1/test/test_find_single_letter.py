import pytest
import findSingle as findSingle


class testingData:
    ligalTestData = [
        # string , expected
        ('aabcc', 'b'),
        ('aabbcddee', 'c'),
        ('xjieiaajx', 'e'),
        ('AaABbBb', 'a'),
        ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', 'b'),
        ('aabbccddeeffgghhiijjkkllmmnnooAppqqrrssttuuvvwwxxyyzzBBCCDDEEFFGGHHIIJJKKLLMMOOPPQQRRSSTTUUVVWWXXYY', 'A')
    ]
    illigalTestData = [
        # string , expected
    ]


@pytest.mark.parametrize("string, expected", testingData.ligalTestData)
def testLigalParameter(string, expected):
    # arrage

    # act
    result = findSingle.findSingle_by52(string)

    # assert
    assert result == expected
