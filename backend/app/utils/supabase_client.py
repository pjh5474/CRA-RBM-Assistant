import os

from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()


def get_supabase_client() -> Client:
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")

    if not supabase_url:
        raise ValueError("SUPABASE_URL is not defined")

    if not supabase_key:
        raise ValueError("SUPABASE_KEY is not defined")

    return create_client(supabase_url, supabase_key)
