import pytest


import syncat


@pytest.fixture()
def mock_argparse(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "syncat",
            "--lexer",
            "json"
            ]
        )


def test_parse_arguments_lexer(mock_argparse):
    assert  syncat.parse_args().lexer == "json"
