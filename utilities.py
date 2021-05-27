import config as cfg
import importlib


def initialize_vault_engine(engine_name=None):
    if not engine_name:
        engine_name = cfg.VAULT_TYPE

    secret_engine = importlib.import_module(f"secret_engines.{engine_name}")

    return secret_engine
