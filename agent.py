import os
import requests
import time
from rich.console import Console
from db import insert_todo, get_todos, update_todo, delete_todo

console = Console()

# Load API key dari environment
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_MODEL = "qwen/qwen3-235b-a22b-2507"

def process_add(title: str, description: str = ""):
    insert_todo(title, description)
    console.print(f"[green]✅ Berhasil menambahkan todo:[/] {title}")

def process_list():
    todos = get_todos()
    if not todos:
        console.print("[yellow]Belum ada todo[/]")
        return
    console.print("[bold blue]📋 Daftar Todo[/]")
    for todo in todos:
        status = "[green]Done[/]" if todo["done"] else "[red]Pending[/]"
        console.print(f"{todo['id']}. {todo['title']} - {todo['description']} ({status})")

def process_update(todo_id: int, done: bool):
    update_todo(todo_id, done)
    console.print(f"[green]🔄 Todo {todo_id} diupdate[/]")

def process_delete(todo_id: int):
    delete_todo(todo_id)
    console.print(f"[red]🗑 Berhasil hapus todo {todo_id}[/]")

def process_ai(prompt: str):
    """Generate task pakai OpenRouter AI dengan retry"""
    if not OPENROUTER_API_KEY:
        console.print("[red]Error:[/] OPENROUTER_API_KEY tidak ditemukan di environment")
        return

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }

    for attempt in range(5):
        try:
            resp = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
            resp.raise_for_status()
            data = resp.json()
            # Ambil text dari response
            text = data["choices"][0]["message"]["content"]
            console.print(f"[cyan]🤖 AI OpenRouter:[/]\n{text}")
            return text
        except requests.HTTPError as e:
            if e.response.status_code == 429:
                wait = 2 ** attempt
                console.print(f"[yellow]Rate limit, retry {attempt+1}/5 setelah {wait}s[/]")
                time.sleep(wait)
            else:
                console.print(f"[red]AI HTTP Error {attempt+1}/5:[/] {e}")
                time.sleep(1)
    console.print("[red]Gagal memanggil AI setelah beberapa percobaan[/]")
