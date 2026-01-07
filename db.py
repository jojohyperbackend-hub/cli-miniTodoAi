# db.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()  # otomatis baca .env

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
TABLE_NAME = "todos"

if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("SUPABASE_URL dan SUPABASE_KEY harus di-set di .env")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def insert_todo(title: str, description: str = ""):
    data = {"title": title, "description": description, "done": False}
    res = supabase.table(TABLE_NAME).insert(data).execute()
    return res

def get_todos():
    res = supabase.table(TABLE_NAME).select("*").execute()
    return res.data

def update_todo(todo_id: int, done: bool):
    res = supabase.table(TABLE_NAME).update({"done": done}).eq("id", todo_id).execute()
    return res

def delete_todo(todo_id: int):
    res = supabase.table(TABLE_NAME).delete().eq("id", todo_id).execute()
    return res
