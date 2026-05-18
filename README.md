# 🛰️ TechRangers: AI-powered FRA Atlas & WebGIS Decision Support System (DSS)

> Dynamically digitizing, mapping, and orchestrating Forest Rights Act (FRA) claims, community resources, and Central Sector Scheme (CSS) benefits using PyTorch U-Net, PostGIS, and Model Context Protocol (MCP).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=flat-square)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-orange.svg?style=flat-square)](https://pytorch.org/)
[![PostGIS](https://img.shields.io/badge/PostGIS-3.3+-blue.svg?style=flat-square)](https://postgis.net/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-emerald.svg?style=flat-square)](https://fastapi.tiangolo.com/)
[![Celery](https://img.shields.io/badge/Queue-Celery-darkred.svg?style=flat-square)](https://docs.celeryq.dev/)

TechRangers is a state-of-the-art spatial intelligence framework engineered to **digitize, verify, map, and optimize the implementation of the Forest Rights Act (FRA), 2006**. Designed for the complex socio-ecological landscapes of Madhya Pradesh, Tripura, Odisha, and Telangana, the system bridges the gap between historical paper-based land claims and targeted, data-driven sustainable development.

---

## 🏛️ Comprehensive System Architecture

```mermaid
flowchart TD
    subgraph Ingestion [Spatial & Document Ingestion]
        A["Scanned FRA Paper Claims"] & B["High-Res Multispectral TIFFs"] & C["Village & Boundary Shapefiles"] -->|Ingestion Pipeline| D["Celery Task Broker"]
    end
    
    subgraph AI_Core [Deep Learning & NLP Engines]
        D -->|spaCy / Hugging Face NER| E["OCR & Named Entity Extraction"]
        D -->|PyTorch U-Net CNN| F["Satellite Semantic Segmentation"]
    end
    
    subgraph Data_Core [Spatial Database Core]
        E -->|Text & Coordinates| G["PostgreSQL + PostGIS DB"]
        F -->|Vectorized Polygons [WKT/GeoJSON]| G
        C -->|GIS Boundaries| G
        
        G -->|Spatial Joins & Pre-computing| H[("Materialized View: village_dss_data")]
    end
    
    subgraph App_Layer [Decision Support & APIs]
        H -->|Environmental / Infra Indices| I["Rules-based DSS Engine"]
        I -->|Eligibility & Justifications| J["FastAPI REST Web Service"]
        I -->|MCP Schema Integration| K["Model Context Protocol Server"]
    end
    
    subgraph Frontend [Presentation Layer]
        J & K -->|Dynamic Layer Overlays| L["Interactive WebGIS Dashboard"]
    end
```

---

## ⚡ Core Technical Pillars

### 1. Deep Semantic Segmentation (U-Net CNN)
*   **Neural Network Architecture:** Utilizes a custom **U-Net CNN** built in PyTorch. The model features 4 symmetric downsampling (encoder) and upsampling (decoder) blocks coupled with skip connections to retain high-frequency spatial boundaries during deep feature extraction.
*   **Loss Function Strategy:** Optimized using a hybrid **BCE + Dice Loss** function to handle highly imbalanced geographic datasets (e.g., small farm patches or narrow water streams against large forest tracts).
*   **Vectorization & Post-Processing:** Translates predicted pixel-level raster masks into vectorized geometries (`GeoJSON` / `WKT` polygons) using GDAL, saving the physical boundaries directly to PostGIS spatial tables.

### 2. OCR & Named Entity Recognition (NER)
*   **Document Digitization:** Extracts structured information from scanned historical FRA paper claims and certificates.
*   **Entity Extraction:** Employs spaCy and fine-tuned Transformer-based NER models to isolate critical fields: `patta_holder_name`, `village_name`, geographic coordinates, claimed area, and claim status.
*   **Asynchronous Queuing:** Managed by Celery task queues backed by Redis to support high-throughput document scanning.

### 3. Spatial PostGIS & Materialized View Optimization
*   **Normalized Geospatial Schema:** Relates foundational hierarchies (`states`, `districts`, `villages`) to environmental factors (`forest_data`, `groundwater_data`, `infrastructure_data`) via spatial keys.
*   **Pre-computed Spatial Joins:** Rather than executing heavy spatial overlap queries (`ST_Contains`, `ST_DWithin`, `ST_Distance`) on-the-fly, a high-performance **Materialized View (`village_dss_data`)** pre-computes indices including forest cover percentages, nearest groundwater tables, and road connectivity.
*   **Fast Queries:** Speeds up DSS queries, yielding sub-millisecond query execution speeds on regional datasets.

### 4. Rule-Based + AI-Enhanced DSS
*   **Central Sector Scheme (CSS) Layering:** Evaluates structural indices against policy rules to determine village-level and individual eligibility for programs like **PM-KISAN**, **Jal Jeevan Mission**, **MGNREGA**, and **DAJGUA**.
*   **Asset-based Intervention Priority:** If a village exhibits a critically low water index, the DSS flags the sector for targeted borewell installations under Jal Shakti, generating a policy recommendation backed by empirical data.
*   **AI Policy Clustering:** Runs K-Means clustering on multi-dimensional asset vectors to group villages into operational categories (e.g., highly forested with low road access vs. agricultural with high water risk), enabling precise resource distribution.

### 5. Model Context Protocol (MCP) Integration
*   **Agent-Ready Geospatial API:** Exposes the entire spatial database, U-Net inference triggers, and DSS recommendation algorithms to AI agents (like Claude or Gemini) via the **Model Context Protocol (MCP)**.
*   **Natural Language Spatial Inquiries:** Enables city administrators and planners to ask complex geographic questions (e.g., *"Show me all villages in Odisha eligible for Jal Jeevan Mission that have less than 15% forest cover"*), which the system automatically resolves via dynamic database lookups and returns as structured map overlays.

---

## 📂 Repository Layout

*   `/cv_models`: The semantic segmentation engine, containing the U-Net architecture, training pipelines, data pre-processors, and containerized Docker environments.
*   `/dss`: The analytical heart of the system, including PostGIS connectors, the rules engine, and the Model Context Protocol (MCP) integration.
*   `dss_schema.sql` / `dss_materialized_view.sql`: Database definition scripts for table architectures and index pre-computations.
*   `import_district_boundaries.py` (and related scripts): Geospatial import scripts that parse shapefiles and populate PostGIS tables.
*   `kmeans_clustering.py`: Unsupervised machine learning models to cluster and profile villages based on social and natural resources.

---

## 🚀 Dev Setup & Spatial Ingest

### 1. Install System Dependencies
Ensure you have Python 3.9+ and PostgreSQL (with the PostGIS extension) installed.

### 2. Set Up Virtual Environment & Packages
Clone the repository and install all required geospatial and deep learning libraries:

```bash
git clone https://github.com/seeramsujay/TechRangers.git
cd TechRangers
pip install -r requirements.txt
```

### 3. Initialize the Spatial Database
Initialize your PostGIS database and run the schema setup scripts:

```bash
psql -h localhost -U postgres -d postgres -f dss_schema.sql
psql -h localhost -U postgres -d postgres -f dss_materialized_view.sql
```

### 4. Import Foundational GIS Boundaries
Run the import scripts to ingest administrative boundaries into PostGIS:

```bash
python import_state_boundaries.py
python import_district_boundaries.py
python import_village_boundaries.py
```

### 5. Run U-Net Training (Optional)
To train the satellite image semantic segmentation model:

```bash
python cv_models/train.py --data_dir /path/to/satellite/images
```

### 6. Launch the FastAPI REST & MCP Servers
Start the local server to serve REST APIs and the Model Context Protocol:

```bash
python dss/dss_api.py
```
This spins up:
*   **REST API:** `http://localhost:8000` (exposing endpoints like `/api/dss/recommendations`)
*   **MCP Protocol Server:** Running concurrently, allowing smart-city dashboards and AI agents to query the system using natural language.

---

## 📄 License

This project is licensed under the **MIT License**. See `LICENSE` for details.