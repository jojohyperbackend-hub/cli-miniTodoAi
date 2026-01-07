import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from agent import (
    process_add,
    process_list,
    process_update,
    process_delete,
    process_ai
)

app = typer.Typer()
console = Console()

console.print(Panel("[bold green]📌 Mini Todo CLI with AI[/]", expand=False, border_style="bright_blue"))

@app.command()
def add(
    title: str = typer.Argument(..., help="Judul todo"),
    description: str = typer.Option("", help="Deskripsi todo")
):
    """Tambah todo baru"""
    process_add(title, description)

@app.command(name="list")
def _list():
    """Tampilkan semua todo dalam tabel modern"""
    todos = process_list()
    if not todos:
        console.print("[yellow]Belum ada todo.[/]")
        return

    table = Table(title="Daftar Todo", show_lines=True, header_style="bold cyan")
    table.add_column("ID", style="dim", width=6)
    table.add_column("Judul", style="bold white")
    table.add_column("Deskripsi", style="white")
    table.add_column("Status", style="bold green")

    for t in todos:
        status = "✔️" if t.get("done") else "❌"
        table.add_row(str(t.get("id")), t.get("title"), t.get("description") or "-", status)

    console.print(table)

@app.command()
def update(
    todo_id: int = typer.Argument(..., help="ID todo yang ingin diupdate"),
    done: bool = typer.Option(..., help="Set status todo: True/False")
):
    """Update status todo"""
    process_update(todo_id, done)

@app.command()
def delete(
    todo_id: int = typer.Argument(..., help="ID todo yang ingin dihapus")
):
    """Hapus todo"""
    process_delete(todo_id)

@app.command()
def ai(
    prompt: str = typer.Argument(..., help="Prompt untuk AI")
):
    """Generate task pakai AI OpenRouter"""
    console.print(Panel(f"[bold cyan]Prompt:[/]\n{prompt}", border_style="magenta"))
    result = process_ai(prompt)

    if result:
        # Output AI bersih, tanpa **
        clean_text = result.replace("**", "")
        console.print(Panel(clean_text, title="AI Response", border_style="green"))

if __name__ == "__main__":
    app()
