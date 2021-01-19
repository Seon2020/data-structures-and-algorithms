import pytest
from code_challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation as mbv


@pytest.mark.parametrize(
    "test_input, expected",
    [
      ('{}', True),
      ('{}(){}', True),
      ('()[[Extra Characters]]', True),
      ('(){}[[]]', True),
      ('{}{Code}[Fellows](())', True),
      ('[({}]', False),
      ('(](', False),
      ('{(})', False),
      ('{', False),
      (')', False),
      ('[}', False)
    ]
)
def test_bracket_validation(test_input, expected):
  actual = mbv(test_input)
  assert actual == expected

def testtesttest():
  actual = mbv('{}')
  expected = True
  assert actual == expected

