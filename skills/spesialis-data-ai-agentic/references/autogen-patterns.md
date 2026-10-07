# Microsoft AutoGen Patterns

**Framework**: Multi-Agent Orchestration & Conversational AI.

## Key Architectures
- **ConversableAgent**: Base class for message-driven agents.
- **GroupChat & GroupChatManager**: Multi-agent discussion room where manager selects the next speaker (round-robin or LLM-based selection).
- **Sequential Chats**: Chain of handoffs between specialized agents (e.g., Planner -> Coder -> Tester).

## Core Rules & Guardrails
- **Sandbox Code Execution**: Wajib jalankan eksekusi kode di dalam Docker (`DockerCommandLineCodeExecutor`) atau lingkungan terisolasi untuk mencegah eksekusi perintah berbahaya di host.
- **Kondisi Terminasi Jelas**: Selalu definisikan fungsi `is_termination_msg` (misal: jika mendeteksi kata "TERMINATE") agar agen tidak terjebak dalam *infinite conversation loop*.
- **Human-in-the-Loop Mode**:
  - `TERMINATE`: Manusia diminta input hanya saat selesai atau agen terbentur masalah.
  - `NEVER`: Otonom penuh dengan batas maksimal giliran (`max_turns`).
