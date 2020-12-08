from click.testing import CliRunner
from hello import marco
from hellocli import callmarco

def test_marco():
    assert "Polo" == marco("Marco")

def test_not_marco():
    assert "No!" == marco("Bobo")

def test_not_marco_cli():
  runner = CliRunner()
  result = runner.invoke(callmarco, ['--name', 'Bob'])
  assert result.exit_code == 0
  assert 'No!' in result.output

def test_marco_cli():
  runner = CliRunner()
  result = runner.invoke(callmarco, ['--name', 'Marco'])
  assert result.exit_code == 0
  assert 'Polo' in result.output