import pytest
import includebeeredgeth



def test_main(capsys):
    includebeeredgeth
    print(dir(includebeeredgeth))
