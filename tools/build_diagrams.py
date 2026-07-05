#!/usr/bin/env python3
"""Generate SVG diagrams for the Research Paper Workflow skill family.

Outputs:
  figures/architecture.svg   — 16-skill family overview with layers
  figures/workflow.svg       — 14-stage pipeline (0-14)
  figures/routing.svg        — trigger boundary mapping
  figures/artifact-flow.svg  — artifact dependency chain
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIGURES = ROOT / "figures"
FIGURES.mkdir(exist_ok=True)

# ── color palette ──────────────────────────────────────────────
C = {
    "bg": "#f8fafc",
    "governance": "#fef3c7",  # amber
    "early": "#dbeafe",       # blue
    "design": "#d1fae5",      # emerald
    "exec": "#fce7f3",        # pink
    "writing": "#e0e7ff",     # indigo
    "audit": "#fed7aa",       # orange
    "final": "#ddd6fe",       # violet
    "arrow": "#64748b",
    "text": "#1e293b",
    "label": "#475569",
    "border": "#cbd5e1",
    "white": "#ffffff",
}


def svg_header(w, h):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n'


def svg_footer():
    return "</svg>\n"


def rect(x, y, w, h, fill, rx=6, stroke=None):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" rx="{rx}"'
    if stroke:
        s += f' stroke="{stroke}" stroke-width="1.5"'
    s += "/>\n"
    return s


def text(x, y, content, size=12, fill=C["text"], anchor="start", bold=False):
    w = 'font-weight="bold"' if bold else ""
    return f'<text x="{x}" y="{y}" font-family="system-ui,sans-serif" font-size="{size}" fill="{fill}" text-anchor="{anchor}" {w}>{content}</text>\n'


def arrow(x1, y1, x2, y2, color=C["arrow"]):
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.5"'
        f' marker-end="url(#arrowhead)"/>\n'
    )


def arrowhead_def():
    return """<defs>
  <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
    <polygon points="0 0, 10 3.5, 0 7" fill="#64748b"/>
  </marker>
</defs>
"""


def group_label(x, y, label, color):
    return (
        rect(x, y - 8, 80, 18, color, rx=4)
        + text(x + 40, y + 5, label, size=10, fill=C["text"], anchor="middle", bold=True)
    )


# ═══════════════════════════════════════════════════════════════
# 1. ARCHITECTURE DIAGRAM
# ═══════════════════════════════════════════════════════════════

def build_architecture():
    skills = [
        # (name, stage, color_group)
        ("rpw-common", "Shared", C["governance"]),
        ("rpw-pipeline", "0. Pipeline", C["governance"]),
        ("rpw-idea-optimize", "1. Idea Opt.", C["early"]),
        ("rpw-idea-review", "2. Idea Rev.", C["early"]),
        ("rpw-literature-monitor", "3. Lit. Monitor", C["early"]),
        ("rpw-literature-search", "4. Lit. Search", C["early"]),
        ("rpw-claim-manifest", "5. Claims", C["design"]),
        ("rpw-experiment-design", "6. Exp. Design", C["design"]),
        ("rpw-experiment-implementation", "7. Exp. Impl.", C["exec"]),
        ("rpw-result-engineering", "8. Result Eng.", C["exec"]),
        ("rpw-result-analysis", "9. Result Anal.", C["exec"]),
        ("rpw-paper-writer", "10. Writer", C["writing"]),
        ("rpw-paper-reviewer", "11. Reviewer", C["audit"]),
        ("rpw-integrity-audit", "12. Audit", C["audit"]),
        ("rpw-submission-check", "13. Sub. Check", C["final"]),
        ("rpw-rebuttal", "14. Rebuttal", C["final"]),
    ]

    w, h = 960, 540
    card_w, card_h = 130, 44
    cols, rows = 8, 2
    x0, y0 = 30, 60
    gap_x, gap_y = 10, 28

    svg = svg_header(w, h)
    svg += arrowhead_def()
    svg += rect(0, 0, w, h, C["bg"], rx=0)

    # Title
    svg += text(w // 2, 30, "RPW Skill Family — Architecture", size=18, anchor="middle", bold=True)

    # Governance row
    gov_y = 80
    svg += rect(x0, gov_y - 15, w - 60, 55, C["governance"], rx=8, stroke=C["border"])
    svg += text(x0 + 12, gov_y + 14, "Governance Layer", size=11, fill=C["label"], bold=True)
    for i, (name, stage, color) in enumerate(skills[:2]):
        x = x0 + 20 + i * (card_w + 20)
        svg += rect(x, gov_y + 22, card_w, 24, C["white"], rx=4, stroke=C["border"])
        svg += text(x + 8, gov_y + 38, name, size=10, bold=True)

    # Runtime skills row
    rt_y = 170
    svg += rect(x0, rt_y - 15, w - 60, 68, C["white"], rx=8, stroke=C["border"])
    svg += text(x0 + 12, rt_y + 8, "Runtime Skills (loaded on demand)", size=11, fill=C["label"], bold=True)
    for i, (name, stage, color) in enumerate(skills[2:]):
        col = i % cols
        row_num = i // cols
        x = x0 + 12 + col * (card_w + 6)
        y = rt_y + 16 + row_num * (card_h + 4)
        svg += rect(x, y, card_w, card_h, color, rx=5, stroke=C["border"])
        svg += text(x + 8, y + 18, stage, size=9, fill=C["label"])
        svg += text(x + 8, y + 34, name, size=10, bold=True)

    # Shared resources
    res_y = 300
    svg += rect(x0, res_y, w - 60, 45, C["white"], rx=8, stroke=C["border"])
    svg += text(x0 + 12, res_y + 28, "Shared: references/ (17 files)  ·  assets/ (17 templates)  ·  scripts/ (9 tools)", size=11, fill=C["label"])

    # Legend
    leg_y = 380
    legends = [
        ("Governance", C["governance"]), ("Early Stage", C["early"]),
        ("Design", C["design"]), ("Execution", C["exec"]),
        ("Writing", C["writing"]), ("Review/Audit", C["audit"]), ("Final", C["final"]),
    ]
    for i, (label, color) in enumerate(legends):
        x = x0 + i * 120
        svg += rect(x, leg_y, 16, 16, color, rx=3, stroke=C["border"])
        svg += text(x + 22, leg_y + 13, label, size=10, fill=C["label"])

    # Bottom note
    svg += text(x0, 440, "Each rpw-* skill is an independent directory with its own SKILL.md. Only the matching skill loads — context stays lean.", size=10, fill=C["label"])
    svg += text(x0, 458, "Skills reference shared governance files via ../rpw-common/ and shared references/assets/scripts from the root.", size=10, fill=C["label"])
    svg += text(x0, 480, "Plugin manifests: .claude-plugin/plugin.json (Claude Code)  ·  .codex-plugin/plugin.json (Codex CLI)  ·  agents/openai.yaml (ChatGPT)", size=10, fill=C["label"])

    svg += svg_footer()
    (FIGURES / "architecture.svg").write_text(svg, encoding="utf-8")
    print("  architecture.svg")


# ═══════════════════════════════════════════════════════════════
# 2. WORKFLOW DIAGRAM
# ═══════════════════════════════════════════════════════════════

def build_workflow():
    stages = [
        ("0", "Pipeline", C["governance"]),
        ("1", "Idea\nOptimize", C["early"]),
        ("2", "Idea\nReview", C["early"]),
        ("3", "Lit.\nMonitor", C["early"]),
        ("4", "Lit.\nSearch", C["early"]),
        ("5", "Claim\nManifest", C["design"]),
        ("6", "Exp.\nDesign", C["design"]),
        ("7", "Exp.\nImplement", C["exec"]),
        ("8", "Result\nEngineer", C["exec"]),
        ("9", "Result\nAnalyze", C["exec"]),
        ("10", "Paper\nWrite", C["writing"]),
        ("11", "Paper\nReview", C["audit"]),
        ("12", "Integrity\nAudit", C["audit"]),
        ("13", "Submission\nCheck", C["final"]),
        ("14", "Rebuttal", C["final"]),
    ]

    w, h = 1120, 300
    x0, y0 = 28, 50
    node_w, node_h = 64, 70
    gap = 8

    svg = svg_header(w, h)
    svg += arrowhead_def()
    svg += rect(0, 0, w, h, C["bg"], rx=0)
    svg += text(w // 2, 28, "14-Stage Research Paper Pipeline", size=16, anchor="middle", bold=True)

    for i, (num, name, color) in enumerate(stages):
        x = x0 + i * (node_w + gap)
        y = y0
        svg += rect(x, y, node_w, node_h, color, rx=6, stroke=C["border"])
        svg += text(x + node_w // 2, y + 18, num, size=14, anchor="middle", bold=True, fill=C["label"])
        svg += text(x + node_w // 2, y + 38, name, size=8, anchor="middle", fill=C["text"])
        # Arrow to next
        if i < len(stages) - 1:
            ax = x + node_w + 2
            ay = y + node_h // 2
            bx = x + node_w + gap - 2
            svg += arrow(ax, ay, bx, ay)

    # Gate note
    svg += text(x0, y0 + node_h + 30, "Each stage has a gate condition. If a gate fails, the next-step menu offers [Repair first] instead of [Recommended].", size=10, fill=C["label"])
    svg += text(x0, y0 + node_h + 48, "Do not skip from idea to writing unless the user explicitly accepts evidence placeholders.", size=10, fill=C["label"])

    # Revision loop
    svg += rect(w - 180, y0 + node_h + 20, 160, 40, C["final"], rx=6, stroke=C["border"])
    svg += text(w - 100, y0 + node_h + 40, "Revision Loop", size=10, anchor="middle", bold=True)
    svg += text(w - 100, y0 + node_h + 54, "Rebuttal → Writer → Reviewer → Audit → Check", size=8, anchor="middle", fill=C["label"])

    svg += svg_footer()
    (FIGURES / "workflow.svg").write_text(svg, encoding="utf-8")
    print("  workflow.svg")


# ═══════════════════════════════════════════════════════════════
# 3. ROUTING DIAGRAM
# ═══════════════════════════════════════════════════════════════

def build_routing():
    routes = [
        ("\"I have a vague idea\"", "rpw-idea-optimize", "rpw-idea-review", C["early"]),
        ("\"Score these ideas\"", "rpw-idea-review", "rpw-idea-optimize", C["early"]),
        ("\"Any recent papers on X?\"", "rpw-literature-monitor", "rpw-literature-search", C["early"]),
        ("\"Find related work on X\"", "rpw-literature-search", "rpw-integrity-audit", C["early"]),
        ("\"Map claims to evidence\"", "rpw-claim-manifest", "rpw-experiment-design", C["design"]),
        ("\"Design my experiments\"", "rpw-experiment-design", "rpw-paper-writer", C["design"]),
        ("\"Set up the code/config\"", "rpw-experiment-implementation", "rpw-experiment-design", C["exec"]),
        ("\"Check my run logs\"", "rpw-result-engineering", "rpw-paper-writer", C["exec"]),
        ("\"What do my results mean?\"", "rpw-result-analysis", "rpw-paper-writer", C["exec"]),
        ("\"Write my paper\"", "rpw-paper-writer", "rpw-paper-reviewer", C["writing"]),
        ("\"Review my paper\"", "rpw-paper-reviewer", "rpw-paper-writer", C["audit"]),
        ("\"Audit claims & citations\"", "rpw-integrity-audit", "rpw-literature-search", C["audit"]),
        ("\"Is it ready to submit?\"", "rpw-submission-check", "rpw-paper-writer", C["final"]),
        ("\"Respond to reviewers\"", "rpw-rebuttal", "rpw-paper-reviewer", C["final"]),
    ]

    w, h = 900, 560
    x0, y0 = 28, 40
    col_w = [280, 180, 180, 80]
    row_h = 30

    svg = svg_header(w, h)
    svg += arrowhead_def()
    svg += rect(0, 0, w, h, C["bg"], rx=0)
    svg += text(w // 2, 26, "Trigger Boundary Routing — Use X, Not Y", size=16, anchor="middle", bold=True)

    # Header
    headers = ["User Intent", "→ Use", "Do NOT use", ""]
    cols_x = [x0, x0 + col_w[0], x0 + col_w[0] + col_w[1], x0 + sum(col_w[:3])]
    for ci, (hdr, cx) in enumerate(zip(headers, cols_x)):
        svg += text(cx, y0, hdr, size=11, bold=True, fill=C["label"])

    # Separator
    svg += f'<line x1="{x0}" y1="{y0 + 6}" x2="{x0 + sum(col_w)}" y2="{y0 + 6}" stroke="{C["border"]}" stroke-width="1"/>\n'

    for ri, (intent, use, not_use, color) in enumerate(routes):
        y = y0 + 20 + ri * row_h
        bg = C["white"] if ri % 2 == 0 else C["bg"]
        svg += rect(x0, y - 2, sum(col_w), row_h - 2, bg, rx=0)
        svg += text(x0 + 6, y + 11, intent, size=10, fill=C["text"])
        svg += text(cols_x[1] + 6, y + 11, use, size=10, bold=True, fill=C["text"])
        svg += text(cols_x[2] + 6, y + 11, not_use, size=10, fill=C["label"])
        # color indicator
        svg += rect(cols_x[3] + 4, y + 4, 16, 16, color, rx=3, stroke=C["border"])

    # Bottom note
    ny = y0 + 20 + len(routes) * row_h + 20
    svg += text(x0, ny, "The agent reads the root SKILL.md entry table, then loads only the matching rpw-* SKILL.md.", size=10, fill=C["label"])
    svg += text(x0, ny + 16, "Each skill's YAML description includes trigger phrases (EN + CN) and explicit \"Do NOT use\" boundaries.", size=10, fill=C["label"])

    svg += svg_footer()
    (FIGURES / "routing.svg").write_text(svg, encoding="utf-8")
    print("  routing.svg")


# ═══════════════════════════════════════════════════════════════
# 4. ARTIFACT FLOW DIAGRAM
# ═══════════════════════════════════════════════════════════════

def build_artifact_flow():
    artifacts = [
        ("paper_state.yaml", "Pipeline", C["governance"]),
        ("idea_brief.md", "Idea Optimize", C["early"]),
        ("idea_review.md", "Idea Review", C["early"]),
        ("literature_search_plan.md\npaper_cards.md", "Lit. Monitor/Search", C["early"]),
        ("related_work_matrix.md", "Lit. Search", C["early"]),
        ("claim_manifest.md", "Claim Manifest", C["design"]),
        ("experiment_plan.md", "Exp. Design", C["design"]),
        ("implementation_plan.md\nrun_matrix.csv", "Exp. Implement", C["exec"]),
        ("results/raw/runs.csv", "Execution", C["exec"]),
        ("result_audit.md\ntables/*.tex", "Result Engineer", C["exec"]),
        ("results_analysis.md", "Result Analyze", C["exec"]),
        ("paper_draft.tex", "Paper Writer", C["writing"]),
        ("review_report.md", "Paper Reviewer", C["audit"]),
        ("integrity_report.md\nsource_verification_log.md", "Integrity Audit", C["audit"]),
        ("submission_checklist.md", "Submission Check", C["final"]),
        ("revision_ledger.md", "Rebuttal", C["final"]),
    ]

    w, h = 1080, 620
    x0, y0 = 20, 40
    node_w, node_h = 120, 52
    cols = 4
    gap_x, gap_y = 16, 26

    svg = svg_header(w, h)
    svg += arrowhead_def()
    svg += rect(0, 0, w, h, C["bg"], rx=0)
    svg += text(w // 2, 26, "Artifact Dependency Chain", size=16, anchor="middle", bold=True)

    for i, (art_name, owner, color) in enumerate(artifacts):
        col = i % cols
        row = i // cols
        x = x0 + col * (node_w + gap_x)
        y = y0 + row * (node_h + gap_y)
        svg += rect(x, y, node_w, node_h, color, rx=6, stroke=C["border"])
        svg += text(x + node_w // 2, y + 16, art_name, size=8, anchor="middle", fill=C["text"])
        svg += text(x + node_w // 2, y + node_h - 10, owner, size=7, anchor="middle", fill=C["label"])

        # Arrow to next (within row)
        if col < cols - 1 and i < len(artifacts) - 1:
            ax = x + node_w + 4
            ay = y + node_h // 2
            bx = x + node_w + gap_x - 4
            svg += arrow(ax, ay, bx, ay)
        # Arrow to next row (last col)
        if col == cols - 1 and row < (len(artifacts) - 1) // cols:
            ax = x + node_w // 2
            ay = y + node_h + 4
            by = y + node_h + gap_y - 4
            svg += arrow(ax, ay, ax, by)

    ny = ((len(artifacts) - 1) // cols + 1) * (node_h + gap_y) + y0 + 10
    svg += text(x0, ny, "Each transition preserves provenance. No artifact moves forward if the previous gate failed.", size=10, fill=C["label"])
    svg += text(x0, ny + 16, "Artifacts belong to a single owner skill. Other skills may read but must not overwrite without explicit handoff.", size=10, fill=C["label"])

    svg += svg_footer()
    (FIGURES / "artifact-flow.svg").write_text(svg, encoding="utf-8")
    print("  artifact-flow.svg")


# ═══════════════════════════════════════════════════════════════

def main():
    print("Generating SVG diagrams...")
    build_architecture()
    build_workflow()
    build_routing()
    build_artifact_flow()
    print("Done — figures/")


if __name__ == "__main__":
    main()
