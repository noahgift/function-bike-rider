from click.testing import CliRunner
from hello import marco
from hellocli import callmarco

def test_marco():
    assert "Polo" == marco("Marco")

def test_search():
  runner = CliRunner()
  result = runner.invoke(callmarco, ['--name', 'Bob'])
  assert result.exit_code == 0
  assert 'No!' in result.output