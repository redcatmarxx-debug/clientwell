from clientwell_generator import ClientReportInput, ClientWellReportGenerator

SAMPLE_CASES = [
    ("Sample Client A", ["depression", "emotional_dysregulation", "trauma_response"], "Client admitted following emotional escalation, hopelessness, and difficulty maintaining safety in home environment."),
    ("Sample Client B", ["anxiety", "sleep_somatic_disturbance", "future_orientation"], "Client presents with chronic worry, fragmented sleep, and limited ability to engage in future planning."),
    ("Sample Client C", ["suicidality", "dts", "external_support"], "Client disclosed passive suicidal ideation, recent self-harm urges, and limited family engagement."),
    ("Sample Client D", ["psychosis", "functioning_level", "gravely_disabled"], "Client presents with disorganized thinking, internal preoccupation, and reduced ability to complete basic daily tasks independently."),
    ("Sample Client E", ["substance_abuse", "dishonesty_function", "circumstance_orientation"], "Client reports substance use history with inconsistent reporting and limited insight into behavioral consequences."),
    ("Sample Client F", ["dto", "anti_social_traits", "social_skills_deficit"], "Client demonstrates escalating peer conflict, aggression, and difficulty navigating social cues within milieu."),
    ("Sample Client G", ["attachment", "identity_self_esteem", "cultural_identity_stress"], "Client presents with relational mistrust, low self-worth, and strong reactivity in spaces experienced as invalidating."),
    ("Sample Client H", ["gender_dysphoria", "trauma_response", "suicidality"], "Client presents with distress linked to identity invalidation, trauma history, and intermittent suicidal ideation."),
    ("Sample Client I", ["csec", "attachment", "external_support"], "Client has history of exploitation, trauma-bonded attachments, inconsistent supports, and elevated risk of running from placement."),
    ("Sample Client J", ["technology_screen_conflict", "anxiety", "emotional_dysregulation"], "Client becomes highly dysregulated when device access is limited and struggles with anxious avoidance and emotional reactivity."),
]


def main() -> None:
    generator = ClientWellReportGenerator()
    for idx, (name, domains, concerns) in enumerate(SAMPLE_CASES, start=1):
        report = generator.generate_report(
            ClientReportInput(
                client_name=name,
                selected_domains=domains,
                presenting_concerns=concerns,
                level_of_care="STRTP/residential",
            )
        )
        for required in ["assessment", "medical_necessity", "treatment_plan", "birp", "risk_summary"]:
            assert report[required].strip(), f"Empty section {required} for sample {idx}"
        print(f"Sample {idx} OK: {report['domains']}")


if __name__ == "__main__":
    main()
