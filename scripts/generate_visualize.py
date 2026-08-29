import argparse
import sys
import os
import re

# Force utf-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

def generate_visualize_html(source_path_or_text, output_file):
    template_path = os.path.join(os.path.dirname(__file__), "..", "templates", "visualize_stitch_template.html")
    if not os.path.exists(template_path):
        print(f"Error: Template not found at {template_path}")
        return

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    if os.path.exists(source_path_or_text):
        with open(source_path_or_text, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE) or re.search(r'^#\s+(.*)', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else os.path.basename(source_path_or_text)
        subtitle = "Stitch MCP 시네마틱 1페이지 대시보드 및 아키텍처 다이어그램"
    else:
        title = f"{source_path_or_text} (Stitch MCP Visual Architecture)"
        subtitle = f"Stitch MCP 디자인 시스템으로 시각화한 {source_path_or_text} 대시보드입니다."

    arch_cards = [
        {"icon": "🏛️", "title": "1. 시스템 핵심 레이어", "desc": "주요 모듈 및 데이터 흐름 파이프라인", "detail": "시스템 뼈대를 구성하는 핵심 레이어 및 노드 연결 구조입니다."},
        {"icon": "⚙️", "title": "2. 실시간 오케스트레이션", "desc": "비동기 상태 제어 및 트리거 발동", "detail": "이벤트 트리거 및 상태 전이 다이어그램입니다."},
        {"icon": "🛡️", "title": "3. 팩트 무결성 락킹", "desc": "SQLite / Neo4j 온톨로지 DB 검증", "detail": "좌뇌 팩트 DB와 결합된 무결성 락킹 레이어입니다."}
    ]

    topology_cards = [
        {"icon": "🧬", "title": "[[Obsidian_Wiki_Node_1]]", "desc": "장기 메모리 연동 노드 및 하위 관계망", "detail": "옵시디언 LLM-Wiki에 영구 기록된 지식 트리플입니다."},
        {"icon": "🔗", "title": "[[Neurosymbolic_Ontology_Node_2]]", "desc": "Neo4j 지식 그래프 엣지 연결", "detail": "도메인 지식 그래프 상의 유기적 관계 노드입니다."}
    ]

    arch_cards_html = "".join([f"""
    <div class="arch-card" onclick="openModal('{c['title']}', '{c['detail']}')">
      <div class="arch-icon">{c['icon']}</div>
      <h3>{c['title']}</h3>
      <p>{c['desc']}</p>
    </div>
    """ for c in arch_cards])

    topology_cards_html = "".join([f"""
    <div class="arch-card" onclick="openModal('{c['title']}', '{c['detail']}')">
      <div class="arch-icon">{c['icon']}</div>
      <h3>{c['title']}</h3>
      <p>{c['desc']}</p>
    </div>
    """ for c in topology_cards])

    summary_text = f"- {title} Stitch MCP 시네마틱 Visual 아티팩트 빌드 완료"

    html = html.replace("{{TITLE}}", title)
    html = html.replace("{{SUBTITLE}}", subtitle)
    html = html.replace("{{ARCH_CARDS_HTML}}", arch_cards_html)
    html = html.replace("{{TOPOLOGY_CARDS_HTML}}", topology_cards_html)
    html = html.replace("{{SUMMARY_TEXT}}", summary_text)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Generated Stitch MCP Visual HTML at: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stitch MCP Visualize Generator Engine")
    parser.add_argument("--source", required=True, help="Topic or file path to visualize")
    parser.add_argument("--output", default="dist/visualize_stitch.html", help="Output HTML filepath")
    args = parser.parse_args()
    
    generate_visualize_html(args.source, args.output)
