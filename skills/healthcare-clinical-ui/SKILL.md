---
name: healthcare-clinical-ui
description: "Use when designing clinical dashboards or WHO charts."
---

# Healthcare & Clinical Dashboard UI Standards (Healthcare Clinical UI)

> Clinical-grade healthcare UI guidelines for Posyandu, Puskesmas, EHR/EMR dashboards, and anthropometric chart visualizations.

## Core Principles

1. **Macro-Level Scorecards vs Drilldown Modals (No Name Leaks)**
   - Donut charts and summary scorecards must show **aggregate counts only** (e.g. `10 Ibu Hamil`, `51 Balita`), never lists of individual patient names directly in the card legend.
   - For lists of patients matching a cohort/segment, bind an interactive click (`wire:click`, modal dialog, or side drawer) to maintain a clean card layout and prevent vertical overflow.

2. **Zero Nested Scrollbars on KPI/Scorecard Grids**
   - Eliminate fixed clipping heights like `max-h-48 overflow-y-auto` inside dashboard KPI cards.
   - Match card heights symmetrically using `flex flex-col justify-between items-stretch` on parent grids.

3. **Standard Medical Units & Terminology (Indonesian Health Context)**
   - **Gestational Age (Bumil)**: Use `mgg` or `minggu` (e.g., `0–13 mgg (T1)`). NEVER use `mg` (milligrams).
   - **Anthropometry Measurement Positions**: Translate terminology into standard Indonesian:
     - `Recumbent` -> `Terlentang` (balita < 24 bulan).
     - `Standing` -> `Berdiri` (balita >= 24 bulan).
   - **Z-Score Indicators**:
     - `BB/U`: Indikator Berat Badan menurut Umur (Gizi Baik, Gizi Kurang, Gizi Buruk, Berisiko Gizi Lebih).
     - `TB/U`: Indikator Tinggi/Panjang Badan menurut Umur (Stunting / Normal / Tinggi).
     - `BB/TB`: Indikator Wasting / Akut (Gizi Baik, Gizi Kurang, Gizi Buruk).
     - `IMT/U`: Indikator Obesitas & Proporsionalitas Lemak Tubuh Balita/Anak.

4. **Dynamic Indicator Synchronization (Anti-Hardcoding Trap)**
   - Never hardcode the spotlight status card to a single indicator (e.g. `nutrition_status / BB/U`) below multi-tab charts.
   - When switching active chart tabs (`activeChart`: `BB/U`, `TB/U`, `BB/TB`, `IMT/U`), the status label, metric value, Z-score, badge color, and guide text MUST synchronize dynamically to the currently selected indicator (e.g., displaying `DETEKSI STUNTING (TB/U)` with Stunting Z-Score on `TB/U`, not `Gizi Baik`).

5. **Dynamic Axis Title & Unit Binding (Anti-Scale Misinterpretation)**
   - In multi-tab anthropometric charts, always bind the X-axis title dynamically to the dataset schema payload (`data.type` or label check), not an inflexible hardcoded string.
   - For `BB/TB` (Weight-for-Height), the X-axis is **Tinggi/Panjang Badan** (`TINGGI BADAN (CM)`, scale 45–120 cm). If labeled as `UMUR (BULAN)`, users and medical examiners will mistake 45–120 cm for chronological age in months (4–10 years), triggering false alarms about wrong age tracking.
   - For `BB/U`, `TB/U`, and `IMT/U`, the X-axis is `UMUR (BULAN)` (scale 0–60 months).

6. **Unified Single-Row Bar vs Stacked Giant Cards (Anti-Proportion Bloat)**
   - Do not stack bulky multi-row card grids or bloated paragraphs underneath the chart canvas. That consumes excessive vertical viewport and breaks card proportions.
   - Place **Last Visit Spotlight** (left) and **Chart Line Legends** (right) on a single compact horizontal footer row (`flex flex-col lg:flex-row lg:items-center justify-between border-t border-slate-100 mt-6 pt-5`).
   - Disable Chart.js native legend (`plugins: { legend: { display: false } }`) when custom unified key pills are present to prevent redundant duplicate lines.

7. **Chart.js Category Axis Alignment (Anti-Zig-Zag Loop Pitfall)**
   - In Chart.js category line charts (e.g. `BB/TB` with discrete labels `[45, 46, ..., 120]`), never mix an array of reference series with an array of sparse `{x, y}` coordinate objects for the child line unless an explicit linear/time scale is configured. On category scales, `{x, y}` objects cause Chart.js to map `x` as ordinal point indices, drawing child trajectory lines backwards in zig-zag loops across the canvas.
   - Structure child series to match the category labels array length: allocate an array of `null`s for all labels, and place the child metric at the rounded height index (`$childData[(int)round($height) - 45] = $weight`).
   - Ensure external helper imports (like `Carbon\Carbon`) are explicitly imported in chart service classes to prevent fatal 500 errors during dynamic tab transitions.

8. **Comprehensive 4-Indicator Historical Table (Full Clinical Context)**
   - Summary and detail tables must display all 4 Permenkes RI No. 2/2020 WHO LMS indicators simultaneously, not just 1 or 2:
     - `BB/U` (Status Gizi) + exact Z-Score.
     - `TB/U` (Deteksi Stunting) + exact Z-Score.
     - `BB/TB` (Status Wasting) + exact Z-Score.
     - `IMT/U` (Komposisi Massa / Obesitas) + exact Z-Score.
   - Include physical anthropometric values (`BB`, `TB`, `IMT`), visit chronological age, measurement position (`Berdiri`/`Terlentang`), and clinical interventions (Vitamin A capsule color, deworming medication).

9. **Strict Clinical Palette & Anti-AI-Slop Restraint**
   - Use sober clinical EHR card styles (`border-slate-100`, `font-mono` tabular figures, compact spacing).
   - Avoid decorative gradient banners or fabricated generic narrative paragraphs (e.g. avoid pompous lines like "Pertumbuhan anak optimal di median WHO...").
   - Guide key colors must strictly mirror the active Chart.js series colors 1:1 (`#10b981` Green, `#f59e0b` Yellow, `#f43f5e` Red, `#0d9488`/`#be185d` Child line).

10. **Realistic Demo Data Seeding & Case Diversification**
   - In presentation datasets, never leave all patient records uniform (e.g. all 100% "Gizi Baik" or artificially glued exactly onto the median line).
   - Seed realistic medical variance across patient records:
     - **Normal / Median WHO**: Organically oscillating trajectory with minor physiological fluctuations.
     - **Extreme Upper Deviation (+4 SD)**: Explicit high-weight case to demonstrate Obesity / Overweight detection rules.
     - **Lower Deviation (-2 to -3 SD)**: Underweight / Wasted case for malnutrition warnings.
     - **Stunting Flag**: Low height-for-age case demonstrating stunted detection.
   - Maintain natural clinical visit intervals (e.g. monthly KMS visits for baduta 0–24 months), rather than unrealistic clumps of future or identical dates.

11. **Functional Empty States in Healthcare KPIs**
   - When cohort count is 0, do not render inactive 0% legend rows.
   - Replace with a contextual shortcut button (e.g., `[ + Catat Pemeriksaan Bumil ]`) directing the health worker to the input form.
