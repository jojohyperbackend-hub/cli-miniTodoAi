# Mini Todo 

## Deskripsi

Mini Todo CLI adalah aplikasi Command Line Interface untuk manajemen todo list dengan integrasi AI (Gemini atau OpenRouter) untuk membuat task secara otomatis. Interface CLI menggunakan `rich` untuk tabel dan output lebih rapi, dengan emoji status ✔️ / ❌.

---

## Fitur

- Tambah, lihat, update, hapus todo
- Tandai status done / belum done
- AI task generator (Gemini / OpenRouter)
- Tabel todo dengan border modern
- Emoji status untuk setiap todo

---

## Teknologi

- Python 3.11+
- rich (terminal modern & tabel)
- typer (CLI)
- supabase-py (CRUD database)
- requests (HTTP untuk AI)
- dotenv (env variables)

---

## Struktur Folder

```
mini-todo-cli/
├── main.py         # CLI entrypoint
├── agent.py        # Logic pemanggilan AI dan proses CRUD
├── db.py           # CRUD ke Supabase
├── requirements.txt
├── .env            # API keys dan Supabase URL
└── README.md
```

---

## Setup Project

### 1. Clone Repository

```bash
git clone https://github.com/jojohyperbackend-hub/cli-miniTodoAi.git
cd cli-miniTodoAi
```

### 2. Buat Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Siapkan `.env`

Buat file `.env` di root project:

```
SUPABASE_URL=<URL_SUPABASE>
SUPABASE_KEY=<API_KEY_SUPABASE>
OPENROUTER_API_KEY=<API_KEY_OPENROUTER>
```

### 5. Buat Database (Supabase)

- Masuk ke [Supabase](https://app.supabase.com/)
- Buat Project baru
- Buat table `todos`:

```sql
CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    done BOOLEAN DEFAULT FALSE
);
```

---

## Command CLI

### 1. Tambah Todo

```bash
python main.py add "Belajar Python" --description "Baca dokumentasi"
```

### 2. Lihat Semua Todo

```bash
python main.py list
```

Tampilannya berupa tabel:

| ID | Title          | Description      | Status |
| -- | -------------- | ---------------- | ------ |
| 1  | Belajar Python | Baca dokumentasi | ❌      |

### 3. Update Todo

- Tandai selesai / done:

```bash
python main.py update <ID> --done True
```

- Tandai belum selesai:

```bash
python main.py update <ID> --done False
```

### 4. Hapus Todo

```bash
python main.py delete <ID>
```

### 5. AI Generate Task

```bash
python main.py ai "Buat task besok pagi untuk belajar Python"
```

Output AI akan dirapikan tanpa bold `**` dan ditampilkan langsung di CLI.

---

## Tips Developer

- Gunakan `.gitignore` yang disediakan supaya `.env` dan API key tidak ke-commit
- Pastikan Supabase URL & Key sesuai
- Jangan spam AI request karena bisa kena rate limit
- Gunakan virtual environment untuk isolasi dependency

---

## License

Project ini open-source, bebas digunakan dan dikembangkan.

