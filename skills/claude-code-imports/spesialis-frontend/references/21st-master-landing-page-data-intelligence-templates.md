# 21st.dev Master Open-Source Data Intelligence Landing Page (Folio Blueprint)

Analisis pola arsitektur landing page Data Intelligence, DevTools, dan Open-Source berbasis template premium Ruixen.ui ("Folio - Open Source Data Intelligence Landing Template", rating 141+ stars di 21st.dev).

---

## 1. Karakteristik Estetika Folio / Data Intelligence

Berbeda dengan landing page agensi konvensional (seperti Northstar yang glamor dan dinamis), genre **Data Intelligence & Open Source DevTools** memiliki bahasa desain yang sangat spesifik:

1. **GitHub Social Proof First**:
   - Menampilkan tombol bintang GitHub (`⭐ Star on GitHub`) lengkap dengan counter bintang live tepat di samping CTA primer.
   - Penegasan status lisensi ("MIT Licensed • 100% Free & Open Source").
2. **Precision Monospace & Metric Accents**:
   - Angka-angka statistik, latensi query (misal: `< 12ms`), dan kode CLI ditampilkan dengan font mono (`font-mono`) berjarak rapat.
3. **Interactive Terminal / Live SQL Code Switcher**:
   - Hero mockup bukan berupa gambar statis, melainkan komponen terminal interaktif (bisa tab SQL, Python, curl) yang bisa di-copy langsung oleh developer dengan 1-klik.
4. **Subtle Mesh / Dot-Matrix Grid Background**:
   - Bukan gradien neon mencolok, melainkan latar belakang *dot matrix* presisi warna Slate/Zinc gelap yang memberi kesan konsol analitik enterprise.

---

## 2. Blueprint Kode Master (The Folio Data Intelligence Shell)

```tsx
import React, { useState } from "react";
import { 
  Terminal, 
  Copy, 
  Check, 
  Star, 
  GitFork, 
  Database, 
  Cpu, 
  ShieldCheck, 
  ArrowRight,
  ExternalLink
} from "lucide-react";

export function FolioDataIntelligenceLanding() {
  const [copied, setCopied] = useState(false);
  const [activeTab, setActiveTab] = useState<"sql" | "python" | "curl">("sql");

  const cliCommand = "npx folio-engine@latest init";

  const handleCopy = () => {
    navigator.clipboard.writeText(cliCommand);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const codeSnippets = {
    sql: `SELECT 
  cluster_id,
  quantile(0.99)(query_duration_ms) AS p99_latency,
  count(*) AS total_queries
FROM system.query_log
WHERE event_date = today()
GROUP BY cluster_id
ORDER BY p99_latency ASC;`,
    python: `from folio import DataCluster

cluster = DataCluster.connect(env="production")
metrics = cluster.telemetry.query(
    metrics=["p99_latency", "throughput"],
    window="15m"
)
print(f"Cluster Healthy: {metrics.is_optimal}")`,
    curl: `curl -X POST https://api.folio.dev/v1/telemetry/ingest \\
  -H "Authorization: Bearer fol_live_9921b" \\
  -H "Content-Type: application/json" \\
  -d '{"event": "db_spike", "region": "ap-southeast-1"}'`
  };

  return (
    <div className="min-h-screen bg-[#07090e] text-slate-100 font-sans selection:bg-cyan-500/20">
      
      {/* Background Dot Matrix Pattern */}
      <div className="fixed inset-0 z-0 pointer-events-none opacity-20 bg-[radial-gradient(#38bdf8_1px,transparent_1px)] [background-size:24px_24px]" />

      {/* Global Header */}
      <header className="fixed top-0 inset-x-0 z-50 h-16 border-b border-slate-800/80 bg-[#07090e]/90 backdrop-blur-md px-6 lg:px-12 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400">
            <Database className="w-4 h-4" />
          </div>
          <span className="font-bold text-base tracking-tight font-mono">folio<span className="text-cyan-400">.ai</span></span>
          <span className="ml-2 px-2 py-0.5 text-[10px] font-mono font-semibold bg-slate-800 text-slate-300 rounded border border-slate-700">v1.4.2</span>
        </div>

        <div className="flex items-center gap-4">
          {/* GitHub Star Pill Button */}
          <a
            href="https://github.com"
            target="_blank"
            rel="noreferrer"
            className="flex items-center gap-2 px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-900/80 hover:bg-slate-800 text-xs font-medium text-slate-200 transition-colors"
          >
            <Star className="w-3.5 h-3.5 text-amber-400 fill-amber-400" />
            <span>Star</span>
            <span className="px-1.5 py-0.2 text-[10px] font-mono bg-slate-800 rounded text-slate-400">4.8k</span>
          </a>

          <button className="px-4 py-1.5 rounded-lg bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-semibold text-xs transition-colors">
            Get Started
          </button>
        </div>
      </header>

      {/* Hero Section */}
      <main className="relative z-10 pt-32 pb-24 px-6 lg:px-12 max-w-6xl mx-auto flex flex-col items-center text-center">
        
        {/* Release Pill */}
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-cyan-500/20 bg-cyan-500/5 text-cyan-300 text-xs font-mono mb-8">
          <span className="w-2 h-2 rounded-full bg-cyan-400 animate-pulse" />
          <span>Open Source Data Intelligence Engine</span>
          <ArrowRight className="w-3 h-3 text-cyan-400" />
        </div>

        {/* Hero Title */}
        <h1 className="text-4xl sm:text-6xl lg:text-7xl font-bold tracking-tight text-white max-w-4xl leading-[1.1] mb-6">
          Query petabytes in real-time with <br />
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-sky-300 to-indigo-400">
            sub-millisecond precision.
          </span>
        </h1>

        {/* Subtitle */}
        <p className="text-base sm:text-lg text-slate-400 max-w-2xl mb-10 leading-relaxed font-normal">
          High-performance distributed telemetry collector and OLAP query accelerator. Self-hosted, lightweight binary, zero vendor lock-in.
        </p>

        {/* Interactive CLI Quickstart Bar */}
        <div className="flex items-center gap-2 p-1.5 pl-4 rounded-xl border border-slate-800 bg-slate-900/90 max-w-md w-full shadow-2xl mb-12">
          <Terminal className="w-4 h-4 text-slate-500 shrink-0" />
          <code className="text-xs font-mono text-cyan-300 flex-1 text-left select-all">
            {cliCommand}
          </code>
          <button
            onClick={handleCopy}
            className="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition-colors"
            title="Salin ke clipboard"
          >
            {copied ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
          </button>
        </div>

        {/* Interactive Code / Query Inspector Mockup */}
        <div className="w-full max-w-4xl rounded-2xl border border-slate-800 bg-[#0b0e14] shadow-2xl overflow-hidden text-left">
          {/* Mockup Header */}
          <div className="flex items-center justify-between px-4 py-3 border-b border-slate-800/80 bg-slate-900/40">
            <div className="flex items-center gap-2">
              <span className="w-3 h-3 rounded-full bg-rose-500/80" />
              <span className="w-3 h-3 rounded-full bg-amber-500/80" />
              <span className="w-3 h-3 rounded-full bg-emerald-500/80" />
              <span className="ml-3 text-xs font-mono text-slate-400">folio-console v1.4</span>
            </div>

            {/* Language Switcher Tabs */}
            <div className="flex items-center bg-slate-950 p-0.5 rounded-lg border border-slate-800">
              {(["sql", "python", "curl"] as const).map((tab) => (
                <button
                  key={tab}
                  onClick={() => setActiveTab(tab)}
                  className={`px-3 py-1 rounded-md text-[11px] font-mono font-medium uppercase transition-colors ${
                    activeTab === tab
                      ? "bg-slate-800 text-cyan-300 shadow-sm"
                      : "text-slate-500 hover:text-slate-300"
                  }`}
                >
                  {tab}
                </button>
              ))}
            </div>
          </div>

          {/* Code Window */}
          <div className="p-6 font-mono text-xs text-slate-300 leading-relaxed overflow-x-auto bg-slate-950/60">
            <pre className="text-cyan-400/90 font-mono">
              <code>{codeSnippets[activeTab]}</code>
            </pre>
          </div>

          {/* Mockup Footer Telemetry Stats */}
          <div className="px-6 py-3 border-t border-slate-800/80 bg-slate-900/20 flex flex-wrap items-center justify-between text-xs font-mono text-slate-400 gap-4">
            <div className="flex items-center gap-6">
              <span className="flex items-center gap-1.5">
                <span className="w-2 h-2 rounded-full bg-emerald-400" />
                <span>Execution Time: <b className="text-slate-200">3.42ms</b></span>
              </span>
              <span>Memory Footprint: <b className="text-slate-200">14.8 MB</b></span>
            </div>
            <span className="text-slate-500">Node: ap-se-1a (Jakarta)</span>
          </div>
        </div>

        {/* Feature Highlights Trio */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-16 w-full max-w-4xl text-left">
          <div className="p-5 rounded-xl border border-slate-800 bg-slate-900/30">
            <Cpu className="w-5 h-5 text-cyan-400 mb-3" />
            <h3 className="text-sm font-semibold text-white mb-1">Native SIMD Acceleration</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Memanfaatkan instruksi vektor AVX-512 untuk aggregasi jutaan baris data per detik tanpa jeda.
            </p>
          </div>

          <div className="p-5 rounded-xl border border-slate-800 bg-slate-900/30">
            <ShieldCheck className="w-5 h-5 text-sky-400 mb-3" />
            <h3 className="text-sm font-semibold text-white mb-1">Self-Hosted Security</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Data tidak pernah keluar dari VPC pribadi Anda. Bebas biaya egress cloud dan mematuhi audit ISO-27001.
            </p>
          </div>

          <div className="p-5 rounded-xl border border-slate-800 bg-slate-900/30">
            <GitFork className="w-5 h-5 text-indigo-400 mb-3" />
            <h3 className="text-sm font-semibold text-white mb-1">100% Extensible Plugins</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Dukungan konektor kustom untuk Postgres, ClickHouse, Redshift, Kafka, dan file Parquet lokal.
            </p>
          </div>
        </div>

      </main>
    </div>
  );
}
```

---

## 3. Checklist Desain Landing Page DevTools / Open Source
1. **Satu-Klik Copy CLI**: Perintah instalasi terminal (`npm install`, `curl -fsSL`, `npx ...`) harus diletakkan persis di *Hero fold* dengan tombol salin instan. Developer tidak mau membaca esai panjang sebelum mencoba aplikasinya.
2. **Konteks Nyata pada Mockup**: Jangan gunakan grafik dummy generic (seperti garis zig-zag tanpa angka). Selalu gunakan data realistis: nama tabel nyata, latensi terukur dalam milidetik (`3.42ms`), dan memori RAM yang masuk akal.
3. **Penyelarasan Warna Cyberspace (Cyan & Sky)**: Sementara produk SaaS korporat condong ke Indigo/Purple, DevTools & Data Platform hampir selalu mengandalkan warna Cyan/Sky/Teal (`#06b6d4`, `#38bdf8`) yang merepresentasikan kecepatan pemrosesan data dingin dan modernitas *low-level engineering*.
