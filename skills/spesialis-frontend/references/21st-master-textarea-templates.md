# 21st.dev Master Textarea Templates

Katalog dan blueprint komponen Textarea (Input Multi-baris) berdasarkan ratusan komponen di 21st.dev (React + Tailwind v4). Sangat krusial untuk antarmuka AI (Chat), komentar, dan formulir panjang.

---

## 1. Empat Arketipe Textarea Modern

### Arketipe 1: The AI Prompt Input (Auto-growing + Actions)
- **Fungsi**: Kotak obrolan AI (seperti ChatGPT/Claude) atau input komentar interaktif.
- **Karakteristik**: 
  - Bisa merentang otomatis (auto-grow) ke bawah seiring user mengetik.
  - Memiliki tombol aksi (Submit, Lampirkan File) yang **tertanam (embedded)** di dalam kotak border textarea, bukan di luarnya.
- **Inspirasi**: `Promt Input with Actions (Julien Thibeaut)`, `useAutoResizeTextarea (Kokonut)`.

### Arketipe 2: Textarea with Floating Label & Hint
- **Fungsi**: Formulir profesional (SaaS/B2B) yang menghemat ruang vertikal.
- **Karakteristik**: Label menyusut dan melayang ke tepi atas border saat textarea di-fokus atau berisi teks. Dilengkapi hint (misal: sisa karakter `24/100`) di sudut bawah.
- **Inspirasi**: `Textarea with floating label (ShadcnSpace)`, `Textarea with Corner Hint (Origin UI)`.

### Arketipe 3: The Markdown / Rich Editor Textarea
- **Fungsi**: Kotak input untuk penulisan artikel atau deskripsi panjang.
- **Karakteristik**: Menyediakan toolbar format (Bold, Italic, Link) tepat di atas kotak teks atau melayang (*floating bubble menu*) saat teks diseleksi.

### Arketipe 4: Support Request / Contact Card
- **Fungsi**: Form kontak mandiri (standalone).
- **Karakteristik**: Textarea dipadukan langsung dengan kontainer Card yang memiliki header bantuan dan tombol kirim penuh (full-width).

---

## 2. Blueprint Kode Master (The AI Prompt Auto-Growing Textarea)

Blueprint ini menggunakan React murni untuk mengatur tinggi otomatis (*auto-resize*) tanpa *scrollbar* ganda, lengkap dengan tombol submit di sudut kanan bawah.

```tsx
import React, { useRef, useState, useEffect } from "react";
import { Send, Paperclip, Mic } from "lucide-react";

interface PromptInputProps {
  onSubmit: (text: string) => void;
  placeholder?: string;
}

export function AutoGrowPromptInput({ onSubmit, placeholder = "Kirim pesan ke AI..." }: PromptInputProps) {
  const [text, setText] = useState("");
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // Auto-resize logic
  useEffect(() => {
    if (textareaRef.current) {
      // Reset height to auto to get the real scrollHeight
      textareaRef.current.style.height = "auto";
      const scrollHeight = textareaRef.current.scrollHeight;
      // Batasi tinggi maksimal agar tidak terus memanjang (misal max 200px)
      textareaRef.current.style.height = `${Math.min(scrollHeight, 200)}px`;
    }
  }, [text]);

  const handleKeyDown = (e: React.KeyboardEvent) => {
    // Submit dengan Enter (tanpa Shift)
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      if (text.trim()) {
        onSubmit(text);
        setText("");
      }
    }
  };

  return (
    <div className="relative w-full max-w-3xl mx-auto rounded-2xl border border-slate-700/80 bg-slate-900/50 shadow-inner focus-within:border-indigo-500/70 focus-within:ring-1 focus-within:ring-indigo-500/70 transition-all">
      <textarea
        ref={textareaRef}
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder={placeholder}
        rows={1}
        className="w-full resize-none bg-transparent px-4 pt-4 pb-12 text-sm text-slate-200 placeholder-slate-500 outline-none leading-relaxed no-scrollbar"
        style={{ minHeight: "60px", maxHeight: "200px" }}
      />
      
      {/* Embedded Actions & Submit Button */}
      <div className="absolute bottom-2 left-2 right-2 flex items-center justify-between">
        
        {/* Attachment & Mic Tools */}
        <div className="flex items-center gap-1">
          <button className="p-1.5 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800 transition-colors focus:outline-none" aria-label="Attach file">
            <Paperclip className="w-4 h-4" />
          </button>
          <button className="p-1.5 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800 transition-colors focus:outline-none" aria-label="Voice input">
            <Mic className="w-4 h-4" />
          </button>
        </div>

        {/* Submit Button */}
        <button
          onClick={() => {
            if (text.trim()) {
              onSubmit(text);
              setText("");
            }
          }}
          disabled={!text.trim()}
          className="p-1.5 rounded-lg bg-indigo-600 text-white disabled:bg-slate-800 disabled:text-slate-600 hover:bg-indigo-500 transition-colors focus:outline-none"
          aria-label="Send message"
        >
          <Send className="w-4 h-4" />
        </button>
        
      </div>
    </div>
  );
}
```

---

## 3. Checklist UX Textarea Modern
1. **Never use single-line input for chat**: Permintaan AI atau chat panjang selalu membutuhkan multi-line (`textarea`) yang otomatis tumbuh, bukan `<input type="text">` biasa.
2. **Shift+Enter for Newline**: Selalu tangkap `onKeyDown`. Enter biasa untuk kirim (submit), `Shift + Enter` untuk garis baru.
3. **Hide Scrollbar**: Sembunyikan *scrollbar* default (`no-scrollbar` class) hingga teks melewati batas `max-height` (misal 200px), barulah scrollbar dimunculkan.
4. **Interactive Focus**: Pastikan border seluruh kontainer luar berubah (glow/highlight) saat textarea menerima fokus (`focus-within:` utility di Tailwind).
