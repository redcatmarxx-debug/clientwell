from __future__ import annotations

from io import BytesIO
from pathlib import Path
from typing import Dict, List

import streamlit as st

from clientwell_generator import (
    DEFAULT_DOMAIN_ORDER,
    DOMAIN_LIBRARY,
    ClientReportInput,
    ClientWellReportGenerator,
    resolve_domain_key,
)

APP_TITLE = "ClientWell Auto-Fill Report Generator"

SAMPLE_CASES: Dict[str, Dict[str, object]] = {
    "1. Mood + trauma stabilization": {
        "client_name": "Sample Client A",
        "selected_domains": ["depression", "emotional_dysregulation", "trauma_response"],
        "presenting_concerns": "Client admitted following emotional escalation, hopelessness, and difficulty maintaining safety in home environment.",
        "level_of_care": "STRTP/residential",
    },
    "2. Anxiety + sleep + future planning": {
        "client_name": "Sample Client B",
        "selected_domains": ["anxiety", "sleep_somatic_disturbance", "future_orientation"],
        "presenting_concerns": "Client presents with chronic worry, fragmented sleep, and limited ability to engage in future planning.",
        "level_of_care": "STRTP/residential",
    },
    "3. SI + DTS + low support": {
        "client_name": "Sample Client C",
        "selected_domains": ["suicidality", "dts", "external_support"],
        "presenting_concerns": "Client disclosed passive suicidal ideation, recent self-harm urges, and limited family engagement.",
        "level_of_care": "STRTP/residential",
    },
    "4. Psychosis + functioning": {
        "client_name": "Sample Client D",
        "selected_domains": ["psychosis", "functioning_level", "gravely_disabled"],
        "presenting_concerns": "Client presents with disorganized thinking, internal preoccupation, and reduced ability to complete basic daily tasks independently.",
        "level_of_care": "STRTP/residential",
    },
    "5. Substance + dishonesty + circumstance": {
        "client_name": "Sample Client E",
        "selected_domains": ["substance_abuse", "dishonesty_function", "circumstance_orientation"],
        "presenting_concerns": "Client reports substance use history with inconsistent reporting and limited insight into behavioral consequences.",
        "level_of_care": "STRTP/residential",
    },
    "6. DTO + anti-social + social deficits": {
        "client_name": "Sample Client F",
        "selected_domains": ["dto", "anti_social_traits", "social_skills_deficit"],
        "presenting_concerns": "Client demonstrates escalating peer conflict, aggression, and difficulty navigating social cues within milieu.",
        "level_of_care": "STRTP/residential",
    },
    "7. Attachment + identity + cultural stress": {
        "client_name": "Sample Client G",
        "selected_domains": ["attachment", "identity_self_esteem", "cultural_identity_stress"],
        "presenting_concerns": "Client presents with relational mistrust, low self-worth, and strong reactivity in spaces experienced as invalidating.",
        "level_of_care": "STRTP/residential",
    },
    "8. Gender dysphoria + trauma": {
        "client_name": "Sample Client H",
        "selected_domains": ["gender_dysphoria", "trauma_response", "suicidality"],
        "presenting_concerns": "Client presents with distress linked to identity invalidation, trauma history, and intermittent suicidal ideation.",
        "level_of_care": "STRTP/residential",
    },
    "9. CSEC + attachment + elopement risk": {
        "client_name": "Sample Client I",
        "selected_domains": ["csec", "attachment", "external_support"],
        "presenting_concerns": "Client has history of exploitation, trauma-bonded attachments, inconsistent supports, and elevated risk of running from placement.",
        "level_of_care": "STRTP/residential",
    },
    "10. Tech conflict + anxiety + dysregulation": {
        "client_name": "Sample Client J",
        "selected_domains": ["technology_screen_conflict", "anxiety", "emotional_dysregulation"],
        "presenting_concerns": "Client becomes highly dysregulated when device access is limited and struggles with anxious avoidance and emotional reactivity.",
        "level_of_care": "STRTP/residential",
    },
}


def get_domain_label_map() -> Dict[str, str]:
    return {key: DOMAIN_LIBRARY[key].name for key in DEFAULT_DOMAIN_ORDER}


def ordered_multiselect_default(selected_domains: List[str]) -> List[str]:
    resolved = []
    for item in selected_domains:
        try:
            resolved.append(resolve_domain_key(item))
        except KeyError:
            continue
    unique = []
    for item in resolved:
        if item not in unique:
            unique.append(item)
    return unique


def export_text_bytes(text: str) -> bytes:
    return text.encode("utf-8")


def section_download(stem: str, content: str) -> None:
    st.download_button(
        label=f"Download {stem}",
        data=export_text_bytes(content),
        file_name=f"{stem.lower().replace(' ', '_')}.txt",
        mime="text/plain",
        use_container_width=True,
    )


def render_section(title: str, content: str, key: str) -> None:
    with st.container(border=True):
        st.subheader(title)
        st.text_area(
            label=f"{title} output",
            value=content,
            height=220,
            key=f"text_{key}",
            label_visibility="collapsed",
        )
        section_download(title, content)


def main() -> None:
    st.set_page_config(page_title=APP_TITLE, layout="wide")
    st.title(APP_TITLE)
    st.caption("Generate assessment, medical necessity, treatment plan, BIRP content, and risk summary from selected ClientWell domains.")

    generator = ClientWellReportGenerator()
    label_map = get_domain_label_map()

    with st.sidebar:
        st.header("Sample testing")
        sample_name = st.selectbox("Load one of 10 sample domain combinations", ["None"] + list(SAMPLE_CASES.keys()))
        st.markdown("These sample cases help validate language across multi-domain combinations.")

    default_case = SAMPLE_CASES.get(sample_name) if sample_name != "None" else None

    default_client_name = default_case["client_name"] if default_case else ""
    default_presenting = default_case["presenting_concerns"] if default_case else ""
    default_loc = default_case["level_of_care"] if default_case else "STRTP/residential"
    default_domains = ordered_multiselect_default(default_case["selected_domains"] if default_case else [])

    with st.form("clientwell_form"):
        col1, col2 = st.columns([1, 1])
        with col1:
            client_name = st.text_input("Client name", value=default_client_name)
            level_of_care = st.text_input("Level of care", value=default_loc)
        with col2:
            presenting_concerns = st.text_area("Presenting concerns", value=default_presenting, height=100)
            risk_override = st.text_area("Optional risk notes override", value="", height=100)

        selected_labels = st.multiselect(
            "Select one or more domains",
            options=[label_map[key] for key in DEFAULT_DOMAIN_ORDER],
            default=[label_map[key] for key in default_domains],
        )

        submitted = st.form_submit_button("Generate report", use_container_width=True)

    if not submitted:
        st.info("Select domains and click Generate report.")
        return

    if not client_name.strip():
        st.error("Enter a client name.")
        return
    if not selected_labels:
        st.error("Select at least one domain.")
        return

    reverse_label_map = {v: k for k, v in label_map.items()}
    selected_domain_keys = [reverse_label_map[label] for label in selected_labels]

    report_input = ClientReportInput(
        client_name=client_name.strip(),
        selected_domains=selected_domain_keys,
        presenting_concerns=presenting_concerns.strip() or None,
        level_of_care=level_of_care.strip() or "residential",
        risk_notes_override=risk_override.strip() or None,
    )

    report = generator.generate_report(report_input)
    full_text = generator.generate_text_report(report_input)

    with st.container(border=True):
        st.subheader("Client overview")
        st.write(f"**Client:** {report['client_name']}")
        st.write(f"**Domains:** {report['domains']}")
        st.download_button(
            label="Download full report",
            data=export_text_bytes(full_text),
            file_name=f"clientwell_report_{client_name.strip().replace(' ', '_').lower()}.txt",
            mime="text/plain",
            use_container_width=True,
        )

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["Full report", "Assessment", "Medical necessity", "Treatment plan", "BIRP", "Risk summary"]
    )

    with tab1:
        render_section("Full Report", full_text, "full")
    with tab2:
        render_section("Assessment", report["assessment"], "assessment")
    with tab3:
        render_section("Medical Necessity", report["medical_necessity"], "medical_necessity")
    with tab4:
        render_section("Treatment Plan", report["treatment_plan"], "treatment_plan")
    with tab5:
        render_section("BIRP", report["birp"], "birp")
    with tab6:
        render_section("Risk Summary", report["risk_summary"], "risk")


if __name__ == "__main__":
    main()
