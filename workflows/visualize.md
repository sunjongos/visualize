---
description: 모든 주제/문서를 Stitch MCP 최고급 디자인 시스템 기반의 '시네마틱 1페이지 대시보드 및 다이어그램'으로 시각화하는 워크플로우 (/visualize)
---

# 💎 Visualize Stitch MCP Workflow

사용자가 `/visualize <주제 또는 파일경로>`를 입력하면 다음 순서로 최고급 Stitch MCP 시네마틱 Visual HTML 아티팩트를 즉시 생성하고 브라우저에 띄웁니다.

---

### 1단계: 주제 파싱 및 팩트 파이프라인 (Parse & Verify)
- 입력된 문서나 주제에서 핵심 아키텍처 노드(3~6개), 데이터 흐름, 핵심 KPI 지표를 파싱합니다.
- `local_ontology.db` 및 `Luca_Memory_Vault`에서 관련 지식 노드를 대조 락킹합니다.

---

### 2단계: Stitch MCP 디자인 토큰 바인딩 (Design Token Injection)
- **Glassmorphism UI**: Dark Ambient Glass, Pulse Glow Connectors, Neon Borders
- **Multi-Tab Views**:
  - 🏛️ Architecture View (SVG Node Flow)
  - 📊 Executive Metrics View (Chart.js / Dynamic KPIs)
  - 🧬 Knowledge Topology View (Obsidian [[Wikilink]] Nodes)
  - 📄 Deep Spec & Action View (Copy Markdown / Print PDF)

---

### 3단계: Standalone HTML 파일 빌드 (Build HTML)
- `html_tools/visualize_<주제_키워드>.html` 경로로 1페이지 독립형 HTML 파일을 생성합니다.

---

### 4단계: 1초 브라우저 자동 렌더링 및 다운로드 복사 (Launch)
- 생성된 HTML 파일을 사용자 다운로드 폴더 (`C:\Users\USER\Downloads\`)로 복사합니다.
- `Start-Process`를 통해 대표님의 기본 웹 브라우저에 1초 만에 자동 렌더링합니다.
