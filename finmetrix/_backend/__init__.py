# finmetrix/_backend/__init__.py

BACKEND = "python"
twr_impl = None

try:
    from ._cpp import twr as twr_impl
except Exception:
    twr_impl = None
else:
    BACKEND = "cpp"
