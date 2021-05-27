import os

TARGET_PLATFORM = os.environ.get('TARGET_PLATFORM', 'linux')

VAULT_TYPE = os.environ.get('VAULT_NAME', 'hashicorp_vault')
VAULT_ADDR = os.environ.get('VAULT_ADDR', '')
VAULT_TOKEN = os.environ.get('VAULT_TOKEN', '')

SECRET_PATH = os.environ.get('SECRET_PATH', '')
KV_ENGINE_MOUNT_PATH = os.environ.get('KV_ENGINE_MOUNT_PATH', '')

OUTPUT_ENV_FILE_PATH = os.environ.get('OUTPUT_ENV_FILE_PATH', '')
