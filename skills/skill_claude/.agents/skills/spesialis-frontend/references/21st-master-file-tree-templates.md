# 21st.dev Master File Tree & Directory Hierarchy Templates

Analisis pola dan blueprint komponen File Tree berdasarkan 61+ komponen hierarki direktori di 21st.dev (React + Tailwind v4 + Framer Motion).

---

## 1. Empat Arketipe File Tree Modern

### Arketipe 1: The IDE-Style Collapsible Directory Tree (VS Code / Finder)
- **Fungsi**: Penjelajah berkas proyek, repositori kode, atau pengelola aset dokumen CMS.
- **Karakteristik Visual**:
  - Garis panduan indentasi vertikal halus di sisi kiri setiap anak cabang (`border-l border-slate-800/80`).
  - Folder berganti ikon saat dibuka (`FolderOpen` warna amber) dan ditutup (`Folder`).
  - Ikon file disesuaikan secara otomatis berdasarkan ekstensi berkas (.tsx, .json, .css).
  - Baris yang dipilih (*selected*) ditandai dengan latar belakang pendar biru/indigo lembut.
- **Inspirasi**: `Tree Code Viewer (ui layout)`, `File Tree (Dillion Verma)`.

### Arketipe 2: The Search & Filter Highlighting Tree
- **Fungsi**: Membantu pengguna menemukan file spesifik dalam struktur folder yang dalam dan bercabang ratusan.
- **Karakteristik Visual**:
  - Kolom pencarian di bagian atas direktori.
  - Begitu pengguna mengetik teks (misal: "button"), folder induk yang memuat berkas tersebut otomatis mekar (*auto-expand*), dan nama file yang cocok diberi warna sorotan teks (*text highlight*).
- **Inspirasi**: `Tree with Search Highlight (Origin UI)`.

### Arketipe 3: The Async Loading Tree (Lazy Fetching)
- **Fungsi**: Menampilkan struktur file dari cloud storage (AWS S3 / Google Drive / GitHub API) yang datanya baru diambil saat folder diklik.
- **Karakteristik Visual**:
  - Ikon folder berubah menjadi pemintal kecil (*mini spinner*) selama 500ms saat data sedang di-request sebelum anak cabang meluncur turun.
- **Inspirasi**: `Async Loading Tree (Abraham)`.

### Arketipe 4: The Inline Action File Row
- **Fungsi**: Manajemen berkas langsung (Rename, Download, Delete).
- **Karakteristik Visual**: Saat baris file di-hover kursor, di ujung kanan muncul tombol aksi mikro (Ikon pensil, unduh, atau titik tiga).

---

## 2. Blueprint Kode Master (The Recursive Interactive File Tree)

```tsx
import { useState } from "react";
import { 
  Folder, 
  FolderOpen, 
  FileCode, 
  FileJson, 
  FileText, 
  ChevronRight, 
  ChevronDown 
} from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

interface FileNode {
  id: string;
  name: string;
  type: "folder" | "file";
  children?: FileNode[];
}

const PROJECT_TREE: FileNode = {
  id: "root",
  name: "berlayar-cafe-frontend",
  type: "folder",
  children: [
    {
      id: "src",
      name: "src",
      type: "folder",
      children: [
        {
          id: "components",
          name: "components",
          type: "folder",
          children: [
            { id: "hero.tsx", name: "HeroSection.tsx", type: "file" },
            { id: "bento.tsx", name: "BentoGrid.tsx", type: "file" },
            { id: "button.tsx", name: "ActionButton.tsx", type: "file" },
          ],
        },
        { id: "app.tsx", name: "App.tsx", type: "file" },
        { id: "index.css", name: "index.css", type: "file" },
      ],
    },
    { id: "package.json", name: "package.json", type: "file" },
    { id: "readme.md", name: "README.md", type: "file" },
  ],
};

// Helper Pemilih Ikon File Berdasarkan Ekstensi
function getFileIcon(fileName: string) {
  if (fileName.endsWith(".tsx") || fileName.endsWith(".ts") || fileName.endsWith(".js")) {
    return <FileCode className="w-4 h-4 text-sky-400 shrink-0" />;
  }
  if (fileName.endsWith(".json")) {
    return <FileJson className="w-4 h-4 text-amber-400 shrink-0" />;
  }
  return <FileText className="w-4 h-4 text-slate-400 shrink-0" />;
}

// Komponen Rekursif untuk Setiap Node
function TreeNode({ 
  node, 
  selectedId, 
  onSelect 
}: { 
  node: FileNode; 
  selectedId: string; 
  onSelect: (id: string) => void;
}) {
  const [isOpen, setIsOpen] = useState(true);
  const isFolder = node.type === "folder";
  const isSelected = selectedId === node.id;

  const handleClick = (e: React.MouseEvent) => {
    e.stopPropagation();
    if (isFolder) {
      setIsOpen(!isOpen);
    }
    onSelect(node.id);
  };

  return (
    <div className="select-none">
      {/* Baris Node Item */}
      <div
        onClick={handleClick}
        className={`flex items-center gap-1.5 py-1 px-2 rounded-lg cursor-pointer transition-colors text-xs font-mono ${
          isSelected
            ? "bg-indigo-500/15 text-indigo-300 font-semibold"
            : "text-slate-300 hover:bg-slate-800/60 hover:text-white"
        }`}
      >
        {isFolder ? (
          <>
            <span className="text-slate-500">
              {isOpen ? <ChevronDown className="w-3.5 h-3.5" /> : <ChevronRight className="w-3.5 h-3.5" />}
            </span>
            {isOpen ? (
              <FolderOpen className="w-4 h-4 text-amber-400 shrink-0" />
            ) : (
              <Folder className="w-4 h-4 text-amber-500/80 shrink-0" />
            )}
          </>
        ) : (
          <>
            <span className="w-3.5" /> {/* Spacer pengganti panah chevron */}
            {getFileIcon(node.name)}
          </>
        )}

        <span className="truncate">{node.name}</span>
      </div>

      {/* Anak Cabang Folder (Recursive Loop) */}
      <AnimatePresence initial={false}>
        {isFolder && isOpen && node.children && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
            transition={{ duration: 0.15, ease: "easeOut" }}
            className="ml-4 pl-2 border-l border-slate-800 space-y-0.5 mt-0.5 overflow-hidden"
          >
            {node.children.map((child) => (
              <TreeNode
                key={child.id}
                node={child}
                selectedId={selectedId}
                onSelect={onSelect}
              />
            ))}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

export function MasterFileTree() {
  const [selectedId, setSelectedId] = useState("app.tsx");

  return (
    <div className="w-full max-w-xs p-4 rounded-2xl border border-slate-800 bg-slate-900/90 shadow-2xl backdrop-blur-xl">
      <div className="flex items-center justify-between pb-3 mb-3 border-b border-slate-800">
        <h4 className="text-xs font-bold font-mono text-slate-400 uppercase tracking-wider">
          Struktur Direktori
        </h4>
        <span className="text-[10px] font-mono text-indigo-400 bg-indigo-500/10 px-2 py-0.5 rounded-full">
          VS Code Style
        </span>
      </div>

      {/* Render Root */}
      <TreeNode
        node={PROJECT_TREE}
        selectedId={selectedId}
        onSelect={(id) => setSelectedId(id)}
      />
    </div>
  );
}
```

---

## 3. Checklist UX File Tree
1. **Garis Indentasi (*Indent Guides*)**: Kunci kenyamanan visual pohon direktori ada pada garis vertikal di sebelah kiri (`border-l border-slate-800`). Tanpa garis ini, pengguna akan kesulitan membedakan kedalaman subfolder saat hirarki sudah masuk ke level 4 ke atas.
2. **Double-Click vs Single-Click**: Pada standar desktop/IDE, *single-click* memilih berkas dan membuka preview sementara, sedangkan *double-click* membuka berkas secara permanen di tab editor baru.
3. **Aksesibilitas Keyboard (WAI-ARIA Treeview)**:
   - Gunakan `role="tree"` pada kontainer terluar dan `role="treeitem"` pada setiap baris berkas.
   - Pengguna harus bisa membuka folder dengan menekan `Panah Kanan` dan menutupnya dengan menekan `Panah Kiri`.
