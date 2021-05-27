import hvac
import config as cfg
from constants import PLATFORM_COMMAND_MAP


def get_client(url, token):
    client = hvac.Client(url, token)

    if client.is_authenticated():
        print("Vault auth successful")

        return client
    else:
        print("Vault auth failed")

        resp = client.renew_self_token()
        print('renew self response {}'.format(resp))

        if client.is_authenticated():
            print("Vault auth successful")

            return client
        else:
            print("Vault auth failed")

            raise Exception("Invalid vault config")


def get_secret(client, secret_path, kv_engine_mount_path):
    secret = client.secrets.kv.v2.read_secret_version(
        path=secret_path,
        mount_point=kv_engine_mount_path
    )['data']['data']

    return secret


def get_env_var_command(key, value, target_platform=None):
    if not target_platform:
        target_platform = cfg.TARGET_PLATFORM

    env_var_command = PLATFORM_COMMAND_MAP[target_platform]

    cmd_text = f'{env_var_command} {key}="{value}"'

    return cmd_text


def write_env_file(secret, output_file_path):
    env_file_data = ''

    for k, v in secret.items():
        command = get_env_var_command(k, v)
        env_file_data += f'{command}\n'

    with open(output_file_path, 'w') as f:
        f.write(env_file_data)
