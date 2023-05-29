
from flask_entrypoint import health

def test_health():
    assert 'ok' in health()