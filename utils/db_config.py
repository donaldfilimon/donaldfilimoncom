import os
import environ

def get_db_config(env_var):
    env = environ.Env()
    environ.Env.read_env(os.path.join('/home/app/w3s-dynamic-storage', '.env'))
    return env.db_url(env_var)
