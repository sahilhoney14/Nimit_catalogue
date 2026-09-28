# NIMIT AI Vision — Presentation & Web Portal Ecosystem

A modern, high-performance, and unified web application ecosystem showcasing NIMIT's Vision AI, Edge Surveillance, and Intelligent Industry Solutions.

---

## 🚀 Quick Start & Build

### 1. Prerequisites & Dependencies
```powershell
pip install -r requirements.txt
```

### 2. Build Everything
Compile all 3 web portals into standalone HTML deliverables with a single command:

```powershell
# Compiles index.html, solutions.html, and modules.html
python build_all.py
```

### 3. Individual Portal Compilers
```powershell
python build_company_hub.py  # Compiles index.html (Company Hub)
python build_solutions.py    # Compiles solutions.html (Solutions Ecosystem)
python build_catalog.py      # Compiles modules.html (AI Modules Catalog)
```

### 4. Client Logo Pipeline
```powershell
# Extract, clean, sort A-Z and export all 99 client logos
python tools/extract_client_logos.py
```

---

## 📁 Project Architecture & Structure

```text
nimit/
│
├── 🌐 Core Web Deliverables (Standalone Production HTML)
│   ├── index.html                  # 1. Company Hub & Executive Overview
│   ├── solutions.html              # 2. Intelligent Industry Solutions (18 Slides)
│   └── modules.html                # 3. Art of Intelligence AI Modules (18 Slides)
│
├── ⚡ Master Compilers & Runners
│   ├── build_all.py                # Master build runner (all 3 portals)
│   ├── build_company_hub.py        # Shortcut runner for index.html
│   ├── build_solutions.py          # Shortcut runner for solutions.html
│   └── build_catalog.py            # Shortcut runner for modules.html
│
├── 🏗️ builders/                     # Core HTML Template Generators
│   ├── build_company_hub.py        # Generator for index.html
│   ├── build_solutions.py          # Generator for solutions.html
│   └── build_catalog.py            # Generator for modules.html
│
├── 📊 data/                        # Canonical Data Models & Source of Truth
│   ├── client_names.json           # Canonical Brand Names mapping (Index 0-98)
│   ├── logo_manifest.json          # Alphabetical metadata & asset paths for all 99 logos
│   ├── slides_data.json            # Content model for solution slides
│   └── slides_extracted.json       # Presentation metadata
│
├── 🛠️ tools/                       # Production Utilities & Asset Pipelines
│   ├── extract_client_logos.py     # End-to-end client card cropper & A-Z logo exporter
│   ├── process_combined_clients.py # Master side-by-side & stacked grid assembler
│   └── inspect_modules.py          # Slide content inspector
│
├── 🎨 assets/                      # Production Media & Static Assets
│   ├── client_logos/               # 99 normalized, clean client brand logos
│   ├── *.mp4                       # 16:9 MP4 video feeds for live analytics
│   └── *.png / *.jpg               # Architecture diagrams, mockups, and icons
│
├── 📦 raw_sources/                 # Original Raw Source Presentations
│   └── Nimit AI.pptx               # Source PowerPoint presentation
│
├── 🧪 scratch/                     # Sandbox for Experiments & Diagnostics
│   ├── assign_names.py             # Name mapping module & diagnostic validator
│   └── clean_export_all.py         # Background cleaning sandbox
│
├── requirements.txt                # Python environment dependencies
└── .gitignore                      # Git ignore patterns for clean version control
```

---

## 🎨 Unified Design System Features

- **Cohesive Typography**: Powered by `Plus Jakarta Sans`, `Outfit`, `Space Grotesk`, and `Inter`.
- **Top Header Row**: Persistent NIMIT brand logo on every slide, glassmorphic portal switch pills (`Solutions` $\leftrightarrow$ `AI Modules`), and slide drawer TOC trigger.
- **2-Column Analytics Layout**: Standardized capability topic cards with themed badges on the left, framed 16:9 video player with live HUD telemetry badges on the right.
- **Bottom Navigation Dock**: Floating glassmorphic dock with Prev, Page counter, Next, and keyboard arrow key navigation.
