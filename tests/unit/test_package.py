"""Package related tests."""


def test_import():
    """Test basic import."""
    import importlib
    try:
        importlib.import_module('staticforms')
    except ImportError:
        assert False
