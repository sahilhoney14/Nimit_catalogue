# NIMIT AI Vision — Presentation & Web Portal Ecosystem

A modern, high-performance, and beautifully unified web application ecosystem showcasing NIMIT's Vision AI, Edge Surveillance, and Intelligent Industry Solutions.

---

## 🚀 Quick Start & Build

Compile all 3 web portals into standalone HTML deliverables with a single command:

```bash
# Compile everything in <0.2 seconds
python build_all.py
```

Or compile individual portals:
```bash
python builders/build_company_hub.py  # Builds index.html (Company Hub)
python builders/build_solutions.py    # Builds solutions.html (Solutions Ecosystem)
python builders/build_catalog.py      # Builds modules.html (AI Modules Catalog)
```

---

## 📁 Clean Workspace Structure

```
c:\nimit\
│
├── 🌐 Core Web Deliverables (Standalone Production HTML)
│   ├── index.html                  # 1. Company Hub & Executive Overview
│   ├── solutions.html              # 2. Intelligent Industry Solutions (18 Slides)
│   └── modules.html                # 3. Art of Intelligence AI Modules (18 Slides)
│
├── ⚡ Master Compilers & Build Tools
│   ├── build_all.py                # One-click master build runner
│   │
│   ├── builders/                   # Core Production HTML Compilers
│   │   ├── build_company_hub.py    # Generator for index.html
│   │   ├── build_solutions.py      # Generator for solutions.html
│   │   └── build_catalog.py        # Generator for modules.html
│   │
│   └── tools/                      # Asset, Visual & Logo Generation Utilities
│       ├── generate_isometric_hospitality.py
│       ├── generate_sectors_visual.py
│       ├── generate_hospitality_visual.py
│       ├── generate_luxury_hospitality.py
│       ├── generate_engaging_hospitality.py
│       ├── generate_perfect_logos.py
│       ├── export_all_logos.py
│       ├── generate_alphabetical_clients.py
│       ├── generate_clients_mobile.py
│       ├── combine_clients_unified.py
│       ├── process_combined_clients.py
│       ├── rebuild_master_images.py
│       └── inspect_modules.py
│
├── 📊 Structured Data Models
│   └── data/
│       ├── slides_data.json        # Single source of truth for slide content
│       ├── slides_extracted.json   # Extracted presentation content metadata
│       └── logo_manifest.json      # Structured manifest for client logo wall
│
├── 🎨 Production Media & Assets
│   └── assets/
│       ├── client_logos/           # High-resolution, cleanly isolated client logos
│       ├── *.mp4                   # 16:9 MP4 video feeds for live analytics
│       └── *.png / *.jpg           # Diagrams, architecture mockups, and logos
│
├── 📦 Raw Sources & Archives
│   └── raw_sources/
│       └── Nimit AI.pptx           # Original source presentation
│
└── 🧪 Scratch & Exploratory Files
    └── scratch/                    # Historical inspection and crop experiments
```

---

## 🎨 Unified Design System Features

- **Cohesive Typography**: Powered by `Plus Jakarta Sans`, `Outfit`, `Space Grotesk`, and `Inter`.
- **Top Header Row**: Persistent NIMIT brand logo on every slide, glassmorphic portal switch pills (`Solutions` $\leftrightarrow$ `AI Modules`), and slide drawer TOC trigger.
- **2-Column Analytics Layout**: Standardized capability topic cards with themed badges on the left, framed 16:9 video player with live HUD telemetry badges on the right.
- **Bottom Navigation Dock**: Floating glassmorphic dock with Prev, Page counter, Next, and keyboard arrow key navigation.
