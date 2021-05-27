import config as cfg

from utilities import initialize_vault_engine

secret_engine = initialize_vault_engine()


def inject_secrets():
    client = secret_engine.get_client(cfg.VAULT_ADDR, cfg.VAULT_TOKEN)

    secret_data = secret_engine.get_secret(client, cfg.SECRET_PATH, cfg.KV_ENGINE_MOUNT_PATH)

    secret_engine.write_env_file(secret_data, cfg.OUTPUT_ENV_FILE_PATH)


if __name__ == '__main__':
    print("Initializing vault injector")
    try:
        inject_secrets()

        print("Secret injected successfully")
    except Exception as e:
        print(f"Secret injection failed. Exception: {e}")
