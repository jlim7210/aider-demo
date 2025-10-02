from typer.testing import CliRunner
from app import app

runner = CliRunner()

def test_hi():
    result = runner.invoke(app, ["hi", "Alice"])
    assert result.exit_code == 0
    assert "Hi, Alice" in result.output
