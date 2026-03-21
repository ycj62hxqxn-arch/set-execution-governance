from pathlib import Path
from textwrap import dedent


ROOT = Path("/Users/alaaatia/1. Project AI Manifest")


RANGE_START = "January 23, 2026"
RANGE_END = "March 20, 2026"
RANGE_LABEL = f"{RANGE_START} to {RANGE_END}"


weekly_milestones = [
    {
        "week": "Week 1",
        "date": "January 23 to January 29, 2026",
        "title": "Authority doctrine and execution-control framing stabilized",
        "items": [
            "The governance doctrine moved from conceptual framing into an authority-first execution model.",
            "The BIG G layer, Alcatara decision logic, and PMS_GOVERN relationships were aligned into one stack.",
            "The shift from authority creation to authority maintenance became a working project principle.",
        ],
    },
    {
        "week": "Week 2",
        "date": "January 30 to February 5, 2026",
        "title": "CARSHUNTER inventory and controlled public interface model expanded",
        "items": [
            "Vehicle inventory transformation workflows were formalized for public and internal cuts.",
            "Two-tier disclosure patterns were reinforced: public-safe view vs. authority-triggered full detail.",
            "Offer, review, and evidence packaging patterns became reusable across automotive cases.",
        ],
    },
    {
        "week": "Week 3",
        "date": "February 6 to February 12, 2026",
        "title": "PMS_GOVERN core governance stack advanced toward canonical form",
        "items": [
            "Command schema, actor registry, governance context, and system manifest assets were consolidated.",
            "QGED gate logic and authority validation became central to the runtime narrative.",
            "AI was consistently framed as proposal-capable but non-sovereign.",
        ],
    },
    {
        "week": "Week 4",
        "date": "February 13 to February 19, 2026",
        "title": "Ledger, audit, evidence, and freeze-state ideas became operational",
        "items": [
            "Immutable ledger, evidence metadata, and snapshot/freeze concepts were pushed into explicit artifacts.",
            "Runtime state and provenance tracking were elevated from notes into documented system surfaces.",
            "Audit-ready language matured across internal and public architecture materials.",
        ],
    },
    {
        "week": "Week 5",
        "date": "February 20 to February 26, 2026",
        "title": "Presentation and publication layers scaled across BPB and platform surfaces",
        "items": [
            "Reveal-style architecture presentations, public overviews, and board-facing materials expanded.",
            "Commercial, internal, and public messaging split more clearly into audience-specific cuts.",
            "Narrative consistency improved between system architecture, strategy, and external positioning.",
        ],
    },
    {
        "week": "Week 6",
        "date": "February 27 to March 5, 2026",
        "title": "GTC4u augmented governance presentation stack and deployment framing matured",
        "items": [
            "GTC4u platform presentation assets were produced in branded, internal, and enhanced forms.",
            "Domain deployment language covered automotive, finance, logistics, AI control, and regulated sectors.",
            "Multi-party onboarding, validation, and risk assessment began to appear as platform features rather than side notes.",
        ],
    },
    {
        "week": "Week 7",
        "date": "March 6 to March 12, 2026",
        "title": "Session reports, SHAP milestones, and change-impact summaries deepened operational memory",
        "items": [
            "SHAP department milestones and BPB comprehensive systems summaries consolidated program scope.",
            "Session analysis, lessons learned, and change-impact materials strengthened retrospective governance.",
            "The public/internal/audit-ready document separation became a repeatable documentation model.",
        ],
    },
    {
        "week": "Week 8",
        "date": "March 13 to March 20, 2026",
        "title": "Freeze-state discipline, rebuild work, and export packaging completed the cycle",
        "items": [
            "The ALAa ATIA x THE BIG G interface was repaired, restyled, and integrated with BPB visual authority.",
            "A formal freeze checkpoint was recorded with runtime state, snapshot metadata, and audit records.",
            "A broken governance reveal file was rebuilt into a complete standalone slide deck with PPTX, PDF, and DOCX exports.",
        ],
    },
]


deliverables = [
    ("Governance Stack", "PMS_GOVERN, QGED, runtime metadata, manifest, freeze records"),
    ("Presentation Layer", "Reveal decks, platform slides, public summaries, partner-ready cuts"),
    ("Platform Surface", "CARSHUNTER, GTC4u, GTS4u/GMTS4U positioning, onboarding and inventory framing"),
    ("Operational Memory", "Session reports, milestones, lessons learned, change-impact and audit-ready packaging"),
    ("Strategic Narrative", "AA strategic overview, BPB internal architecture, public-safe governance positioning"),
]


platform_updates = {
    "GTC4u": [
        "Augmented governance presentation assets produced for internal, branded, and enhanced deck variants.",
        "Platform language aligned around authority-first governance, compliance automation, and controlled execution.",
        "Deployment narrative extended to automotive, finance, logistics, AI control, and regulated operations.",
    ],
    "GTS4u / GMTS4U": [
        "Platform role clarified as the multi-sector integration and systems layer inside the BPB ecosystem.",
        "Onboarding and developer instruction references indicate a stronger productivity and stakeholder-entry function.",
        "Contact, platform capability, and systems integration messaging now support partner-facing positioning.",
    ],
}


inventory_cards = [
    ("Dealer Inventory Card", "Public-safe listing card with vehicle identity, partial disclosure, pricing zone, and governed CTA."),
    ("Authority Review Card", "Internal card for source, validation state, evidence package, and commercial disposition."),
    ("Case Offer Card", "Structured case card for GO / NO-GO decisions, supplier familiarity, and confidence notes."),
]


member_cards = [
    ("Partner Onboarding Card", "Authority level, sector fit, compliance readiness, and integration priority."),
    ("Dealer Onboarding Card", "Inventory source trust level, document discipline, logistics reliability, and escalation path."),
    ("Member Activation Card", "Entry checklist, evidence requirements, WhatsApp-to-platform traceability, and audit touchpoints."),
]


strategic_points = [
    "Alaa Atia is positioned as sovereign strategic authority, not merely an operator inside a toolchain.",
    "BPB Solutions LTD is evolving from a set of documents into a governance operating environment.",
    "The strongest differentiator is not AI usage; it is the architectural control of execution, evidence, and state transitions.",
    "Public-facing surfaces are increasingly governed by the same doctrine as internal systems, reducing narrative drift.",
]


audit_controls = [
    "Explicit authority path",
    "Immutable or append-only evidence posture",
    "Named runtime state and freeze-state concepts",
    "Audience-specific publication control",
    "Structured retrospective learning via session and milestone reports",
]


def html_page(title: str, body: str, subtitle: str, theme: str = "dark") -> str:
    palette = {
        "dark": {
            "bg": "#0f1722",
            "bg2": "#172231",
            "card": "rgba(255,255,255,0.05)",
            "text": "#f4efe5",
            "muted": "rgba(244,239,229,0.72)",
            "gold": "#c6a85a",
            "line": "rgba(198,168,90,0.26)",
        },
        "light": {
            "bg": "#f6f0e6",
            "bg2": "#fffdf8",
            "card": "rgba(255,255,255,0.8)",
            "text": "#181512",
            "muted": "#5d564c",
            "gold": "#a98939",
            "line": "rgba(169,137,57,0.26)",
        },
    }[theme]
    return dedent(
        f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>{title}</title>
          <style>
            :root {{
              --bg: {palette["bg"]};
              --bg2: {palette["bg2"]};
              --card: {palette["card"]};
              --text: {palette["text"]};
              --muted: {palette["muted"]};
              --gold: {palette["gold"]};
              --line: {palette["line"]};
            }}
            * {{ box-sizing: border-box; margin: 0; padding: 0; }}
            body {{
              font-family: Georgia, "Times New Roman", serif;
              background:
                radial-gradient(circle at top right, rgba(198,168,90,0.16), transparent 24%),
                linear-gradient(180deg, var(--bg), var(--bg2));
              color: var(--text);
              line-height: 1.6;
            }}
            .page {{
              width: min(1120px, calc(100% - 36px));
              margin: 28px auto 60px;
              background: color-mix(in srgb, var(--bg2) 88%, transparent);
              border: 1px solid var(--line);
              box-shadow: 0 24px 80px rgba(0,0,0,0.18);
            }}
            .hero {{
              padding: 52px 52px 36px;
              border-bottom: 1px solid var(--line);
            }}
            .eyebrow {{
              font: 700 12px/1.2 Arial, sans-serif;
              letter-spacing: 0.18em;
              text-transform: uppercase;
              color: var(--gold);
              margin-bottom: 16px;
            }}
            h1 {{
              font-size: clamp(34px, 5vw, 64px);
              line-height: 1.02;
              margin-bottom: 14px;
              max-width: 920px;
            }}
            .subtitle {{
              font-size: 20px;
              color: var(--muted);
              max-width: 840px;
            }}
            .content {{
              padding: 28px 52px 56px;
            }}
            h2 {{
              font-size: 28px;
              margin: 28px 0 12px;
            }}
            p {{
              margin: 10px 0;
              color: var(--muted);
              font-size: 18px;
            }}
            ul {{
              padding-left: 22px;
              margin: 10px 0 18px;
            }}
            li {{
              margin: 9px 0;
              color: var(--muted);
            }}
            .grid {{
              display: grid;
              grid-template-columns: repeat(2, minmax(0, 1fr));
              gap: 16px;
              margin: 18px 0 24px;
            }}
            .cards3 {{
              display: grid;
              grid-template-columns: repeat(3, minmax(0, 1fr));
              gap: 16px;
              margin: 18px 0 24px;
            }}
            .card {{
              background: var(--card);
              border: 1px solid var(--line);
              padding: 18px 18px;
              border-radius: 14px;
            }}
            .card h3 {{
              font-size: 18px;
              margin-bottom: 8px;
              color: var(--text);
            }}
            .callout {{
              padding: 18px 20px;
              border-left: 4px solid var(--gold);
              background: var(--card);
              border-radius: 8px;
              margin: 18px 0 24px;
            }}
            .timeline {{
              display: grid;
              gap: 14px;
              margin-top: 16px;
            }}
            .event {{
              border: 1px solid var(--line);
              background: var(--card);
              border-radius: 14px;
              padding: 16px 18px;
            }}
            .event .meta {{
              font: 700 12px/1.2 "Courier New", monospace;
              color: var(--gold);
              margin-bottom: 8px;
            }}
            table {{
              width: 100%;
              border-collapse: collapse;
              margin: 18px 0 24px;
              border: 1px solid var(--line);
            }}
            th, td {{
              padding: 12px 14px;
              border-bottom: 1px solid var(--line);
              text-align: left;
              vertical-align: top;
            }}
            th {{
              font: 700 12px/1.2 Arial, sans-serif;
              letter-spacing: 0.08em;
              text-transform: uppercase;
              color: var(--gold);
            }}
            td {{
              color: var(--muted);
            }}
            .diagram {{
              width: 100%;
              border: 1px solid var(--line);
              border-radius: 16px;
              background: var(--card);
              padding: 16px;
              margin: 18px 0 24px;
            }}
            .footer {{
              margin-top: 34px;
              padding-top: 18px;
              border-top: 1px solid var(--line);
              font-size: 15px;
              color: var(--muted);
            }}
            @media (max-width: 900px) {{
              .page {{ width: min(100%, calc(100% - 18px)); }}
              .hero, .content {{ padding-left: 20px; padding-right: 20px; }}
              .grid, .cards3 {{ grid-template-columns: 1fr; }}
            }}
          </style>
        </head>
        <body>
          <article class="page">
            <section class="hero">
              <div class="eyebrow">BPB Solutions LTD / Last 8 Weeks Program Scope</div>
              <h1>{title}</h1>
              <div class="subtitle">{subtitle}</div>
            </section>
            <section class="content">
              {body}
              <div class="footer">Scope window: {RANGE_LABEL} | Prepared from repo milestones, platform summaries, reveal decks, session reports, and governance artifacts.</div>
            </section>
          </article>
        </body>
        </html>
        """
    )


def timeline_html() -> str:
    blocks = []
    for item in weekly_milestones:
        bullets = "".join(f"<li>{point}</li>" for point in item["items"])
        blocks.append(
            f"""
            <div class="event">
              <div class="meta">{item["week"]} / {item["date"]}</div>
              <h3>{item["title"]}</h3>
              <ul>{bullets}</ul>
            </div>
            """
        )
    return '<div class="timeline">' + "".join(blocks) + "</div>"


def deliverables_table() -> str:
    rows = "".join(
        f"<tr><td>{name}</td><td>{desc}</td></tr>" for name, desc in deliverables
    )
    return f"""
    <table>
      <thead><tr><th>Program Area</th><th>Deliverables Consolidated</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
    """


def inline_program_svg() -> str:
    return """
    <div class="diagram">
      <svg viewBox="0 0 1000 320" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Program stack diagram">
        <rect width="1000" height="320" fill="transparent"/>
        <g font-family="Arial, sans-serif">
          <rect x="40" y="100" width="180" height="96" rx="16" fill="rgba(198,168,90,0.12)" stroke="rgba(198,168,90,0.45)"/>
          <text x="130" y="132" fill="#c6a85a" text-anchor="middle" font-size="12" font-weight="700">DOCTRINE</text>
          <text x="130" y="164" fill="currentColor" text-anchor="middle" font-size="22" font-weight="700">BIG G</text>
          <text x="130" y="186" fill="currentColor" text-anchor="middle" font-size="15">Authority-first governance</text>

          <rect x="290" y="100" width="180" height="96" rx="16" fill="rgba(198,168,90,0.08)" stroke="rgba(198,168,90,0.35)"/>
          <text x="380" y="132" fill="#c6a85a" text-anchor="middle" font-size="12" font-weight="700">DECISION MODEL</text>
          <text x="380" y="164" fill="currentColor" text-anchor="middle" font-size="22" font-weight="700">ALCATARA</text>
          <text x="380" y="186" fill="currentColor" text-anchor="middle" font-size="15">Energy to output logic</text>

          <rect x="540" y="100" width="180" height="96" rx="16" fill="rgba(255,255,255,0.06)" stroke="rgba(198,168,90,0.28)"/>
          <text x="630" y="132" fill="#c6a85a" text-anchor="middle" font-size="12" font-weight="700">EXECUTION GOVERNANCE</text>
          <text x="630" y="164" fill="currentColor" text-anchor="middle" font-size="22" font-weight="700">PMS_GOVERN</text>
          <text x="630" y="186" fill="currentColor" text-anchor="middle" font-size="15">QGED, runtime, commands</text>

          <rect x="790" y="100" width="170" height="96" rx="16" fill="rgba(99,167,255,0.12)" stroke="rgba(99,167,255,0.35)"/>
          <text x="875" y="132" fill="#c6a85a" text-anchor="middle" font-size="12" font-weight="700">EVIDENCE</text>
          <text x="875" y="164" fill="currentColor" text-anchor="middle" font-size="22" font-weight="700">LEDGER</text>
          <text x="875" y="186" fill="currentColor" text-anchor="middle" font-size="15">Audit and freeze memory</text>

          <path d="M220 148H290M470 148H540M720 148H790" stroke="#c6a85a" stroke-width="3"/>
        </g>
      </svg>
    </div>
    """


def main_report_body() -> str:
    sections = [
        "<h2>Program Summary</h2>",
        f"<p>The last eight weeks of work, from {RANGE_LABEL}, pushed BPB Solutions LTD from fragmented governance artifacts into a more coherent operating environment. The stack now spans doctrine, decision logic, execution governance, immutable evidence, platform presentation, onboarding logic, and freeze-state discipline.</p>",
        inline_program_svg(),
        "<h2>Weekly Milestones</h2>",
        timeline_html(),
        "<h2>Deliverables Consolidated</h2>",
        deliverables_table(),
        '<div class="callout"><strong>Program reading:</strong> the strongest pattern across the eight-week window is the convergence of public interface work and internal governance work. Interfaces, reports, ledgers, runtime state, and platform positioning now increasingly speak the same language.</div>',
        "<h2>Platform Updates: GTC4u and GTS4u</h2>",
        "<div class=\"grid\">"
        + "".join(
            f"<div class=\"card\"><h3>{name}</h3><ul>"
            + "".join(f"<li>{point}</li>" for point in points)
            + "</ul></div>"
            for name, points in platform_updates.items()
        )
        + "</div>",
        "<h2>Deployment Assets and Operational Cards</h2>",
        "<div class=\"cards3\">"
        + "".join(
            f"<div class=\"card\"><h3>{title}</h3><p>{text}</p></div>"
            for title, text in inventory_cards + member_cards
        )
        + "</div>",
        "<h2>Strategic Reading</h2>",
        "<ul>" + "".join(f"<li>{point}</li>" for point in strategic_points) + "</ul>",
        "<h2>Audit-Ready Controls Emergent in the Program</h2>",
        "<ul>" + "".join(f"<li>{point}</li>" for point in audit_controls) + "</ul>",
    ]
    return "".join(sections)


def shap_body() -> str:
    milestones = "".join(
        f"<li>{item['title']} ({item['date']})</li>" for item in weekly_milestones
    )
    return (
        "<h2>SHAP Department Scope</h2>"
        "<p>This report reframes SHAP Department as the program surface where governance milestones, systems updates, bridges, and maintenance converged during the last eight weeks.</p>"
        "<div class=\"grid\">"
        "<div class=\"card\"><h3>Milestones</h3><ul>"
        + milestones
        + "</ul></div>"
        "<div class=\"card\"><h3>Systems Updated</h3><ul>"
        "<li>PMS_GOVERN governance engine and command surfaces</li>"
        "<li>Immutable ledger, evidence metadata, and freeze-state artifacts</li>"
        "<li>Runtime state engine, manifest, provenance, and audit traces</li>"
        "<li>Reveal decks, public cuts, and internal board-facing materials</li>"
        "</ul></div></div>"
        "<h2>Maintenance and Extension</h2>"
        "<div class=\"cards3\">"
        "<div class=\"card\"><h3>Bridges</h3><p>WhatsApp intake, evidence packaging, and document export pipelines expanded operational reach.</p></div>"
        "<div class=\"card\"><h3>Maintenance</h3><p>Governance files, slide decks, manifests, and policy surfaces were kept in active alignment.</p></div>"
        "<div class=\"card\"><h3>Operational Effect</h3><p>SHAP increasingly acts as the consolidation point for lessons learned, architecture memory, and readiness packaging.</p></div>"
        "</div>"
    )


def platform_body() -> str:
    gtc = "".join(f"<li>{x}</li>" for x in platform_updates["GTC4u"])
    gts = "".join(f"<li>{x}</li>" for x in platform_updates["GTS4u / GMTS4U"])
    inv = "".join(f"<div class=\"card\"><h3>{a}</h3><p>{b}</p></div>" for a, b in inventory_cards)
    mem = "".join(f"<div class=\"card\"><h3>{a}</h3><p>{b}</p></div>" for a, b in member_cards)
    return (
        "<h2>Platform Update Summary</h2>"
        "<div class=\"grid\">"
        f"<div class=\"card\"><h3>GTC4u</h3><ul>{gtc}</ul></div>"
        f"<div class=\"card\"><h3>GTS4u / GMTS4U</h3><ul>{gts}</ul></div>"
        "</div>"
        "<h2>Inventory Deployment Assets</h2>"
        f"<div class=\"cards3\">{inv}</div>"
        "<h2>Member Onboarding Cards</h2>"
        f"<div class=\"cards3\">{mem}</div>"
        "<div class=\"callout\"><strong>Deployment direction:</strong> inventory and onboarding are no longer just sales or admin surfaces. They are governed entry points into the BPB execution environment.</div>"
    )


def strategic_partner_body() -> str:
    return (
        "<h2>Partner Summary</h2>"
        "<p>This standalone partner cut presents Alaa Atia as a strategic architect building governance-first systems across BPB Solutions LTD, CARSHUNTER, ALCATARA, and the platform layer represented by GTC4u and GTS4u / GMTS4U.</p>"
        "<h2>Why It Matters</h2>"
        "<ul>" + "".join(f"<li>{point}</li>" for point in strategic_points) + "</ul>"
        "<h2>What Matured in the Last Eight Weeks</h2>"
        "<div class=\"grid\">"
        "<div class=\"card\"><h3>Architecture</h3><p>Governance doctrine, decision logic, and execution surfaces now read as one stack rather than disconnected files.</p></div>"
        "<div class=\"card\"><h3>Documentation</h3><p>Public, partner, internal, and audit-ready cuts are increasingly separated by audience without losing conceptual consistency.</p></div>"
        "<div class=\"card\"><h3>Platforms</h3><p>GTC4u and GTS4u are being framed as governed deployment surfaces rather than ordinary websites or marketing layers.</p></div>"
        "<div class=\"card\"><h3>Signal</h3><p>The strongest signal to partners is discipline: versioning, freeze states, evidence continuity, and authority clarity.</p></div>"
        "</div>"
    )


def internal_body(owner: str) -> str:
    emphasis = (
        "This internal cut emphasizes sovereign control, freeze-state discipline, and architecture consolidation under Alaa Atia."
        if owner == "AA"
        else "This internal cut emphasizes BPB-wide architecture maturity, platform alignment, and audit posture."
    )
    return (
        f"<h2>Internal Reading</h2><p>{emphasis}</p>"
        "<h2>Milestones and Deliverables</h2>"
        + timeline_html()
        + "<h2>Program Risks</h2>"
        "<div class=\"grid\">"
        "<div class=\"card\"><h3>Authority Concentration</h3><p>Strong control is an advantage, but future scaling needs formal delegation models that do not erode doctrine.</p></div>"
        "<div class=\"card\"><h3>Evidence Drift</h3><p>Runtime state, ledgers, public decks, and narrative summaries need continued synchronization to avoid symbolic governance.</p></div>"
        "<div class=\"card\"><h3>Platform Fragmentation</h3><p>GTC4u, GTS4u, CARSHUNTER, and BPB materials need ongoing identity alignment so onboarding and deployment stay coherent.</p></div>"
        "<div class=\"card\"><h3>Operational Load</h3><p>Rapid document creation across many audiences increases the value of templates, generation scripts, and canonical source files.</p></div>"
        "</div>"
    )


def public_body() -> str:
    return (
        "<h2>Public Cut</h2>"
        "<p>Over the last eight weeks, BPB Solutions LTD advanced a governance-first infrastructure spanning authority control, audit-ready evidence, platform deployment, and partner-facing documentation.</p>"
        "<div class=\"cards3\">"
        "<div class=\"card\"><h3>Governance</h3><p>Authority-first system design moved from concept to visible platform narrative.</p></div>"
        "<div class=\"card\"><h3>Platforms</h3><p>GTC4u and GTS4u / GMTS4U now read more clearly as governed deployment surfaces.</p></div>"
        "<div class=\"card\"><h3>Documentation</h3><p>Public, partner, internal, and audit-ready outputs expanded in parallel.</p></div>"
        "</div>"
        "<h2>Public-Safe Themes</h2>"
        "<ul><li>Execution control</li><li>Audit-ready infrastructure</li><li>Sector-spanning deployment readiness</li><li>Institutional documentation discipline</li></ul>"
    )


def audit_body() -> str:
    controls = "".join(f"<li>{c}</li>" for c in audit_controls)
    return (
        "<h2>Audit-Ready Report</h2>"
        "<p>This variant focuses on controls, evidence posture, and the progression of documentation discipline across the last eight weeks.</p>"
        "<h2>Control Surfaces</h2>"
        f"<ul>{controls}</ul>"
        "<h2>Evidence of Progression</h2>"
        + deliverables_table()
        + "<h2>Program Conclusion</h2>"
        "<div class=\"callout\"><strong>Audit reading:</strong> the program is strongest where state, authority, evidence, and audience classification are made explicit. The remaining work is less about inventing components and more about tightening consistency across them.</div>"
    )


def md_report() -> str:
    week_blocks = []
    for item in weekly_milestones:
        week_blocks.append(
            f"## {item['week']} - {item['date']}\n\n### {item['title']}\n\n"
            + "\n".join(f"- {point}" for point in item["items"])
        )
    return dedent(
        f"""\
        ---
        title: "BPB Solutions LTD - Last 8 Weeks Program Session Report"
        author: "Alaa Atia / BPB Solutions LTD"
        date: "{RANGE_END}"
        lang: en
        fontsize: 11pt
        geometry: margin=0.9in
        colorlinks: true
        ---

        # Executive Summary

        This session report covers the last eight weeks of BPB Solutions LTD program work from {RANGE_LABEL}. The period consolidated governance doctrine, execution-control architecture, immutable evidence posture, platform deployment narratives, and audience-specific reporting.

        # Milestone Timeline

        {'\n\n'.join(week_blocks)}

        # Core Deliverables

        {"\n".join(f"- **{name}:** {desc}" for name, desc in deliverables)}

        # Platform Updates

        ## GTC4u

        {"\n".join(f"- {item}" for item in platform_updates["GTC4u"])}

        ## GTS4u / GMTS4U

        {"\n".join(f"- {item}" for item in platform_updates["GTS4u / GMTS4U"])}

        # Deployment Assets

        ## Inventory Cards

        {"\n".join(f"- **{title}:** {text}" for title, text in inventory_cards)}

        ## Member Onboarding Cards

        {"\n".join(f"- **{title}:** {text}" for title, text in member_cards)}

        # Strategic Reading

        {"\n".join(f"- {point}" for point in strategic_points)}

        # Audit-Ready Controls

        {"\n".join(f"- {point}" for point in audit_controls)}

        # Conclusion

        The most important pattern across the reporting window is convergence. The same doctrine now shapes internal systems, public-facing platform language, partner summaries, audit-ready packaging, and freeze-state discipline.
        """
    )


def linkedin_svg(title: str, subtitle: str, steps, filename: str):
    cards = []
    x = 70
    for step_title, step_text in steps:
        cards.append(
            f"""
            <g transform="translate({x} 302)">
              <rect x="0" y="0" width="240" height="170" rx="20" fill="rgba(255,255,255,0.04)" stroke="#c6a85a"/>
              <text x="24" y="34" fill="#c6a85a" font-family="Arial, sans-serif" font-size="12" font-weight="700" letter-spacing="2">{step_title.upper()}</text>
              <text x="24" y="74" fill="#ffffff" font-family="Georgia, serif" font-size="30" font-weight="700">{step_title}</text>
              <text x="24" y="106" fill="#d1c6b5" font-family="Arial, sans-serif" font-size="17">{step_text}</text>
            </g>
            """
        )
        x += 270
    svg = dedent(
        f"""\
        <svg width="1200" height="628" viewBox="0 0 1200 628" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="1200" height="628" fill="#10131a"/>
          <circle cx="1030" cy="110" r="180" fill="#c6a85a" fill-opacity="0.08"/>
          <text x="64" y="58" fill="#c6a85a" font-family="Arial, sans-serif" font-size="12" font-weight="700" letter-spacing="4">PUBLIC CUT / LAST 8 WEEKS</text>
          <text x="64" y="122" fill="#ffffff" font-family="Georgia, serif" font-size="48" font-weight="700">{title}</text>
          <text x="64" y="170" fill="#d1c6b5" font-family="Arial, sans-serif" font-size="20">{subtitle}</text>
          {''.join(cards)}
          <text x="64" y="592" fill="#9d917e" font-family="Arial, sans-serif" font-size="12" font-weight="700" letter-spacing="3">BPB SOLUTIONS LTD / LINKEDIN PUBLIC CUT / {RANGE_END.upper()}</text>
        </svg>
        """
    )
    (ROOT / filename).write_text(svg, encoding="utf-8")


def main():
    files = {
        "Last_8_Weeks_Program_Session_Report_2026-03-20.md": md_report(),
        "Last_8_Weeks_Program_Session_Report_2026-03-20.html": html_page(
            "Last 8 Weeks Program Session Report",
            main_report_body(),
            "Comprehensive session report spanning governance architecture, platform updates, deployment assets, onboarding structures, and audit-ready deliverables.",
            "dark",
        ),
        "Shap_Department_Last_8_Weeks_Comprehensive_Report.html": html_page(
            "SHAP Department Last 8 Weeks Comprehensive Report",
            shap_body(),
            "Comprehensive SHAP department cut focused on milestones, systems updates, extensions, and maintenance across the reporting window.",
            "dark",
        ),
        "GTC4u_GTS4u_Systems_Deployment_Assets_And_Onboarding.html": html_page(
            "GTC4u and GTS4u Systems Update, Deployment Assets, Inventory and Member Onboarding",
            platform_body(),
            "Platform update covering GTC4u and GTS4u / GMTS4U systems, deployment assets, inventory cards, and member onboarding structures.",
            "light",
        ),
        "Alaa_Atia_Strategic_Overview_Partner_Summary.html": html_page(
            "Alaa Atia Strategic Overview - Partner Summary",
            strategic_partner_body(),
            "Standalone partner-facing strategic overview of Alaa Atia, BPB governance infrastructure, and platform maturity over the last eight weeks.",
            "light",
        ),
        "AA_Internal_Last_8_Weeks_Deep_Report.html": html_page(
            "AA Internal Last 8 Weeks Deep Report",
            internal_body("AA"),
            "Internal deep report focused on sovereign control, consolidation, risks, and architecture maturity.",
            "dark",
        ),
        "BPB_Internal_Last_8_Weeks_Deep_Report.html": html_page(
            "BPB Internal Last 8 Weeks Deep Report",
            internal_body("BPB"),
            "Internal BPB-wide report focused on architecture, platform alignment, reporting discipline, and delivery scope.",
            "dark",
        ),
        "BPB_Public_Last_8_Weeks_Overview.html": html_page(
            "BPB Public Last 8 Weeks Overview",
            public_body(),
            "Public-safe overview of governance, platform, and documentation progress during the reporting window.",
            "light",
        ),
        "BPB_Audit_Ready_Last_8_Weeks_Report.html": html_page(
            "BPB Audit-Ready Last 8 Weeks Report",
            audit_body(),
            "Audit-oriented reporting cut emphasizing controls, evidence posture, and consistency across architecture and documentation.",
            "light",
        ),
    }

    for name, content in files.items():
        (ROOT / name).write_text(content, encoding="utf-8")

    linkedin_svg(
        "Governance became a program, not a file set",
        "Across eight weeks, doctrine, execution, evidence, and platform packaging moved into one operating narrative.",
        [
            ("Doctrine", "BIG G and Alcatara aligned the decision model."),
            ("Execution", "PMS_GOVERN and QGED framed controlled runtime action."),
            ("Evidence", "Ledger and freeze-state artifacts gave the system memory."),
            ("Platforms", "GTC4u and GTS4u absorbed the governance language."),
        ],
        "LinkedIn_Public_Cut_Last_8_Weeks_01.svg",
    )

    linkedin_svg(
        "Platforms now carry governance signals",
        "Inventory, onboarding, and partner entry points are increasingly treated as governed surfaces.",
        [
            ("Inventory", "Offer cards and review cards gained structure."),
            ("Onboarding", "Members and dealers are framed through control logic."),
            ("Partner", "Audience-specific summaries improved trust and clarity."),
            ("Audit", "External-ready packaging moved closer to discipline."),
        ],
        "LinkedIn_Public_Cut_Last_8_Weeks_02.svg",
    )

    linkedin_svg(
        "The strongest milestone was convergence",
        "The same language now appears in internal decks, public cuts, partner summaries, and audit-ready reports.",
        [
            ("Internal", "AA and BPB deep reports stabilized the internal view."),
            ("Public", "Public-safe cuts retained structure without overexposing detail."),
            ("Partner", "Strategic partner narratives became cleaner."),
            ("Freeze", "State discipline closed the loop on execution."),
        ],
        "LinkedIn_Public_Cut_Last_8_Weeks_03.svg",
    )


if __name__ == "__main__":
    main()
