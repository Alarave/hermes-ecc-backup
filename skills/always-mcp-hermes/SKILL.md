---
name: always-mcp-hermes
description: "Aturan global Hermes MCP dan background tool execution standar."
---

# Rule: always-mcp-hermes

> [!NOTE]
> Aturan ini bersifat GLOBAL dan aktif setiap saat.

## R (Role / Identity)
- **Peran**: Pengguna aktif MCP Hermes.

## C (Context & Input)
- **Referensi Utama**: Server MCP `hermes` sudah terdaftar dan berjalan di *background*.
- **Masukan Kerja**: Permintaan apapun dari *user* yang membutuhkan alat (*tool*), eksekusi terminal, atau operasi *file*.

## C (Constraints & Guardrails)
- SELALU utamakan memanggil server MCP `hermes` untuk mengeksekusi tugas.
- Jika user meminta untuk melakukan pengecekan, membuat file, mencari referensi, atau tugas kompleks lainnya, delegasikan langsung ke tool MCP `hermes` sebelum mencoba menyelesaikan secara manual.
- Anggap `hermes` sebagai asisten bayangan (co-pilot) utamamu.

## O (Output Format)
- Tidak perlu menjelaskan bahwa Anda memanggil Hermes. Langsung panggil *tool* dari MCP `hermes` dan berikan jawaban akhir ke *user* berdasarkan hasil dari Hermes.
