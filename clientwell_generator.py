from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class DomainEntry:
    name: str
    assessment: str
    medical_necessity: str
    goal: str
    objective: str
    intervention: str
    birp_behavior: str
    birp_intervention: str
    birp_response: str
    birp_plan: str
    risk_level: str
    risk_type: str
    risk_notes: str


DOMAIN_LIBRARY: Dict[str, DomainEntry] = {
    "anxiety": DomainEntry(
        name="Anxiety",
        assessment=(
            "Client presents with anxiety symptoms as evidenced by anticipatory worry, somatic complaints, and avoidance of structured activities. "
            "These symptoms impact social functioning, treatment engagement, and daily task completion. Contributing factors may include trauma history, heightened threat sensitivity, and difficulty with emotional regulation."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of increased avoidance, emotional dysregulation, and functional decline in social and treatment settings. "
            "Anxiety symptoms significantly interfere with participation in daily programming and require structured therapeutic support within a residential level of care."
        ),
        goal="Client will improve ability to tolerate anxiety and engage in daily treatment activities.",
        objective=(
            "Client will utilize at least one identified coping strategy (e.g., grounding, breathing, or verbal support) in 3 out of 5 observed anxiety-provoking situations."
        ),
        intervention=(
            "Staff will provide co-regulation, grounding techniques, and structured emotional support to address anxiety-related avoidance, including real-time prompting and reinforcement of coping strategies."
        ),
        birp_behavior=(
            "Client displayed increased anxiety during group activity, including hesitation, physical restlessness, and verbalized discomfort."
        ),
        birp_intervention=(
            "Staff provided grounding prompts and offered structured support to reduce anticipatory worry."
        ),
        birp_response=(
            "Client demonstrated partial engagement after intervention and remained in group setting."
        ),
        birp_plan=(
            "Continue reinforcing coping strategies and increase tolerance for structured group participation."
        ),
        risk_level="Moderate",
        risk_type="Emotional Dysregulation / Avoidance",
        risk_notes=(
            "No current SI/DTO reported. Anxiety contributes to functional impairment and potential escalation under stress."
        ),
    ),
    "depression": DomainEntry(
        name="Depression",
        assessment=(
            "Client presents with depressive symptoms as evidenced by low mood, reduced engagement in activities, social withdrawal, and decreased energy or motivation. "
            "Client may also demonstrate irritability, hopelessness, or difficulty completing daily tasks. These symptoms impact emotional functioning, social relationships, and participation in treatment programming. Contributing factors may include trauma history, chronic stress, identity-related challenges, and/or underlying mood disorder."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of further emotional decline, increased isolation, and potential escalation to self-harm or suicidal ideation. "
            "Depressive symptoms significantly impair daily functioning, motivation, and engagement in treatment, requiring structured therapeutic services within a residential level of care to stabilize mood and improve functioning."
        ),
        goal="Client will increase emotional engagement and improve mood stability in daily functioning.",
        objective=(
            "Client will engage in at least one structured activity (group, school, or therapeutic task) per day and demonstrate use of one coping strategy to manage low mood in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide behavioral activation support, emotional validation, and structured engagement strategies to address depressive symptoms, including prompting participation, reinforcing small successes, and offering coping tools to increase motivation and emotional regulation."
        ),
        birp_behavior=(
            "Client presented with low energy and limited engagement, initially refusing participation in group activity and verbalizing low motivation."
        ),
        birp_intervention=(
            "Staff provided supportive encouragement, normalized depressive symptoms, and offered structured options for partial participation."
        ),
        birp_response=(
            "Client demonstrated gradual engagement and participated in a portion of the activity with staff support."
        ),
        birp_plan="Continue reinforcing behavioral activation strategies and increase tolerance for structured participation.",
        risk_level="Moderate",
        risk_type="DTS / SI (monitor)",
        risk_notes=(
            "Client presents with depressive symptoms that may increase risk for passive or active self-harm if unaddressed. No current active plan reported, but ongoing monitoring is indicated due to mood instability and functional impairment."
        ),
    ),
    "emotional_dysregulation": DomainEntry(
        name="Emotional Dysregulation",
        assessment=(
            "Client presents with emotional dysregulation as evidenced by rapid escalation in emotional responses, difficulty returning to baseline after distress, and inconsistent ability to manage frustration, disappointment, or interpersonal conflict. "
            "Client may exhibit outbursts, shutdown behaviors, or prolonged emotional reactivity across situations. These symptoms impact behavioral control, peer and staff relationships, and overall participation in treatment. Contributing factors may include trauma history, attachment disruption, neurodevelopmental patterns, and limited coping skill development."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued emotional escalation, behavioral incidents, and impaired functioning across treatment settings. "
            "Emotional dysregulation significantly interferes with the client’s ability to safely engage in daily programming and relationships, requiring structured therapeutic support within a residential level of care to promote stabilization and skill development."
        ),
        goal="Client will improve ability to regulate emotional responses and return to baseline following distress.",
        objective=(
            "Client will demonstrate use of at least one regulation strategy (e.g., grounding, requesting support, taking space) during emotional escalation in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide co-regulation, emotional identification support, and structured coping interventions to address dysregulation, including real-time de-escalation, modeling of regulation strategies, and reinforcement of recovery following escalation."
        ),
        birp_behavior=(
            "Client became emotionally escalated during peer interaction, demonstrating raised voice, agitation, and difficulty disengaging from conflict."
        ),
        birp_intervention=(
            "Staff utilized co-regulation techniques, provided space, and offered grounding prompts to support emotional stabilization."
        ),
        birp_response=(
            "Client demonstrated gradual reduction in escalation and was able to re-engage with support after a period of de-escalation."
        ),
        birp_plan="Continue reinforcing emotional regulation strategies and increase client’s ability to identify early escalation cues.",
        risk_level="Moderate to High",
        risk_type="DTO / DTS (situational)",
        risk_notes=(
            "Emotional dysregulation increases risk for impulsive behaviors, including aggression toward others or self-directed behaviors during escalation. Monitoring and structured intervention are required to maintain safety."
        ),
    ),
    "sleep_somatic_disturbance": DomainEntry(
        name="Sleep & Somatic Disturbance",
        assessment=(
            "Client presents with sleep and somatic disturbance as evidenced by difficulty initiating or maintaining sleep, irregular sleep patterns, and/or physical complaints such as fatigue, headaches, stomach discomfort, or body tension without clear medical cause. "
            "Client may demonstrate nighttime dysregulation, daytime fatigue, or inconsistent participation in daily activities. These symptoms impact emotional regulation, cognitive functioning, and overall treatment engagement. Contributing factors may include trauma history, anxiety, depression, environmental instability, and nervous system dysregulation."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of worsening emotional instability, impaired cognitive functioning, and reduced capacity to participate in treatment programming. "
            "Sleep and somatic disturbances significantly interfere with daily functioning and regulation, requiring structured therapeutic support within a residential level of care to stabilize biological rhythms and improve overall functioning."
        ),
        goal="Client will improve sleep consistency and increase ability to regulate physical and somatic responses.",
        objective=(
            "Client will follow a structured sleep routine and demonstrate use of at least one regulation strategy (e.g., grounding, relaxation, or staff support) during periods of somatic distress in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide structured sleep support, environmental regulation, and somatic-based interventions to address dysregulation, including grounding techniques, sensory tools, and consistent nighttime and daytime structure."
        ),
        birp_behavior=(
            "Client reported difficulty sleeping and demonstrated fatigue and low engagement during daytime activities, including decreased focus and withdrawal."
        ),
        birp_intervention=(
            "Staff provided support with structured routine, encouraged use of grounding and relaxation strategies, and monitored somatic complaints."
        ),
        birp_response=(
            "Client demonstrated partial engagement in activities and was receptive to support, with slight improvement in participation."
        ),
        birp_plan="Continue reinforcing sleep routine and somatic regulation strategies to improve daily functioning and engagement.",
        risk_level="Low to Moderate",
        risk_type="Emotional Dysregulation / DTS (secondary)",
        risk_notes=(
            "Sleep disruption and somatic distress may contribute to increased emotional dysregulation, irritability, and reduced impulse control. Ongoing monitoring is recommended due to impact on overall functioning and potential escalation into higher-risk behaviors."
        ),
    ),
    "psychosis": DomainEntry(
        name="Psychosis",
        assessment=(
            "Client presents with psychotic symptoms as evidenced by perceptual disturbances, disorganized thinking, impaired reality testing, and/or delusional beliefs. "
            "Client may demonstrate confusion, paranoia, internal preoccupation, or difficulty maintaining coherent communication. These symptoms impact cognitive functioning, safety awareness, social interaction, and ability to engage in treatment. Contributing factors may include primary psychotic disorder, mood disorder with psychotic features, trauma-related dissociation, or substance-induced symptoms."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of significant deterioration in reality testing, impaired judgment, and potential harm to self or others due to disorganized thinking or perceptual disturbances. "
            "Psychotic symptoms severely impair functioning and require structured therapeutic and psychiatric support within a residential level of care to ensure safety, stabilization, and symptom management."
        ),
        goal="Client will improve reality orientation and increase ability to engage safely in daily functioning.",
        objective=(
            "Client will demonstrate improved orientation to person, place, and situation and utilize support to manage symptoms in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide reality orientation, structured support, and low-stimulation engagement to address psychotic symptoms, including use of clear communication, grounding techniques, and coordination with psychiatric services for medication management."
        ),
        birp_behavior=(
            "Client presented with signs of internal preoccupation and disorganized thinking, including difficulty maintaining focus and responding to internal stimuli."
        ),
        birp_intervention=(
            "Staff provided reality orientation, used simple and direct communication, and reduced environmental stimulation to support stabilization."
        ),
        birp_response=(
            "Client demonstrated partial responsiveness to staff support and was able to engage briefly in structured activity."
        ),
        birp_plan="Continue monitoring symptoms, reinforce orientation strategies, and coordinate with clinical team for ongoing stabilization.",
        risk_level="Moderate to High",
        risk_type="DTS / DTO (variable)",
        risk_notes=(
            "Impaired reality testing may increase risk for unsafe or unpredictable behavior, including self-harm or aggression. Ongoing monitoring and structured support are required to maintain safety."
        ),
    ),
    "suicidality": DomainEntry(
        name="Suicidality",
        assessment=(
            "Client presents with suicidal ideation as evidenced by verbal statements, passive or active thoughts of death, and/or history of suicide attempts or self-harm behaviors. "
            "Client may demonstrate hopelessness, emotional distress, withdrawal, or fluctuating mood states associated with increased risk. These symptoms impact safety, emotional stability, and overall functioning within the treatment environment. Contributing factors may include depression, trauma history, emotional dysregulation, identity-related stress, and/or environmental instability."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of serious self-harm or suicide attempt. Suicidal ideation significantly impairs safety and emotional functioning, requiring structured therapeutic support, continuous monitoring, and intervention within a residential level of care to ensure stabilization and risk reduction."
        ),
        goal="Client will increase ability to maintain safety and reduce frequency and intensity of suicidal thoughts.",
        objective=(
            "Client will verbalize suicidal thoughts to staff and utilize at least one identified coping or safety strategy in 3 out of 5 observed instances of distress."
        ),
        intervention=(
            "Staff will provide ongoing safety monitoring, emotional support, and crisis intervention as needed, including use of safety planning, co-regulation, and structured check-ins to reduce suicidal ideation and increase coping capacity."
        ),
        birp_behavior=(
            "Client expressed passive suicidal thoughts during check-in, reporting feelings of hopelessness and emotional overwhelm."
        ),
        birp_intervention=(
            "Staff provided supportive listening, reinforced safety planning, and engaged client in grounding and coping strategies."
        ),
        birp_response=(
            "Client was receptive to support, denied active plan or intent at this time, and remained engaged with staff."
        ),
        birp_plan="Continue close monitoring, reinforce safety strategies, and support emotional regulation during periods of distress.",
        risk_level="High",
        risk_type="SI / DTS",
        risk_notes=(
            "Client presents with suicidal ideation requiring ongoing monitoring and structured intervention. No immediate plan reported at this time (if applicable), but risk remains elevated due to emotional instability and underlying contributing factors. Safety protocols and continued assessment are required."
        ),
    ),
    "dto": DomainEntry(
        name="Danger to Others (DTO)",
        assessment=(
            "Client presents with risk of harm to others as evidenced by verbal threats, aggressive behavior, physical altercations, or escalation during interpersonal conflict. "
            "Client may demonstrate low frustration tolerance, impulsivity, and difficulty managing anger or perceived threats. These behaviors impact the safety of peers and staff, disrupt the treatment environment, and impair the client’s ability to engage in structured programming. Contributing factors may include trauma history, emotional dysregulation, learned behavioral patterns, substance use, and/or underlying psychiatric conditions."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued aggressive behavior and potential harm to others. These behaviors significantly impair safe functioning within less structured environments and require structured therapeutic support, supervision, and intervention within a residential level of care to maintain safety and promote behavioral stabilization."
        ),
        goal="Client will reduce aggressive behaviors and increase ability to manage conflict safely.",
        objective=(
            "Client will demonstrate use of at least one coping or de-escalation strategy (e.g., taking space, verbalizing needs, seeking staff support) during moments of escalation in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide real-time de-escalation, clear limit-setting, and co-regulation support to address aggressive behaviors, including identification of triggers, reinforcement of appropriate responses, and structured opportunities to practice safe conflict resolution."
        ),
        birp_behavior=(
            "Client became verbally aggressive during peer interaction, including raised voice and threatening language, and demonstrated difficulty disengaging from conflict."
        ),
        birp_intervention=(
            "Staff implemented de-escalation techniques, set clear behavioral limits, and provided space for the client to regulate."
        ),
        birp_response=(
            "Client demonstrated partial reduction in escalation and was able to disengage from the situation with staff support."
        ),
        birp_plan="Continue reinforcing de-escalation strategies and support client in identifying triggers and alternative responses.",
        risk_level="Moderate to High",
        risk_type="DTO",
        risk_notes=(
            "Client presents with ongoing risk for aggressive behavior toward others, particularly during interpersonal conflict or emotional escalation. Structured supervision and intervention are required to maintain safety and reduce risk of harm."
        ),
    ),
    "dts": DomainEntry(
        name="Danger to Self (DTS)",
        assessment=(
            "Client presents with risk of harm to self as evidenced by non-suicidal self-injury, impulsive or self-endangering behaviors, and/or engagement in actions that compromise personal safety. "
            "Client may demonstrate difficulty regulating emotional distress, low distress tolerance, and reliance on maladaptive coping strategies to manage internal states. These behaviors impact physical safety, emotional stability, and engagement in treatment. Contributing factors may include trauma history, emotional dysregulation, depression, identity-related distress, and/or learned coping patterns."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued self-harm and escalation of unsafe behaviors. These behaviors significantly impair the client’s ability to maintain safety and regulate emotional distress, requiring structured therapeutic support, supervision, and intervention within a residential level of care to reduce risk and promote development of adaptive coping strategies."
        ),
        goal="Client will reduce self-harming behaviors and increase use of safe coping strategies.",
        objective=(
            "Client will utilize at least one alternative coping strategy (e.g., grounding, sensory tools, requesting support) in place of self-harm behaviors in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide close monitoring, emotional support, and skill-building interventions to address self-harm behaviors, including identification of triggers, introduction of alternative coping strategies, and reinforcement of safe emotional expression."
        ),
        birp_behavior=(
            "Client engaged in self-harming behavior following emotional distress related to peer interaction."
        ),
        birp_intervention=(
            "Staff ensured immediate safety, provided emotional support, and introduced alternative coping strategies to address distress."
        ),
        birp_response=(
            "Client was receptive to staff support and demonstrated willingness to engage in alternative coping strategy with prompting."
        ),
        birp_plan="Continue monitoring for self-harm behaviors and reinforce use of adaptive coping strategies during distress.",
        risk_level="Moderate to High",
        risk_type="DTS",
        risk_notes=(
            "Client presents with ongoing risk of self-harm behaviors used as a coping mechanism for emotional distress. While behavior may not reflect suicidal intent, risk remains significant due to potential escalation and physical harm. Structured supervision and intervention are required to maintain safety."
        ),
    ),
    "substance_abuse": DomainEntry(
        name="Substance Abuse",
        assessment=(
            "Client presents with substance use concerns as evidenced by reported use of drugs and/or alcohol, difficulty controlling use, and/or engagement in behaviors associated with substance use. "
            "Client may demonstrate reliance on substances to manage emotional distress, social pressure, or trauma-related symptoms. These behaviors impact emotional regulation, decision-making, safety, and overall functioning. Contributing factors may include trauma history, peer influence, emotional dysregulation, and co-occurring mental health conditions."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued substance use, impaired judgment, and increased engagement in unsafe or high-risk behaviors. Substance use significantly interferes with emotional stability, behavioral control, and treatment engagement, requiring structured therapeutic support within a residential level of care to promote stabilization, reduce risk, and support development of adaptive coping strategies."
        ),
        goal="Client will reduce reliance on substances and increase use of adaptive coping strategies.",
        objective=(
            "Client will identify at least one trigger for substance use and demonstrate use of one alternative coping strategy in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide psychoeducation, motivational support, and coping skill development to address substance use, including identifying triggers, reinforcing alternative behaviors, and supporting engagement in recovery-oriented activities."
        ),
        birp_behavior=(
            "Client discussed prior substance use and demonstrated ambivalence about stopping, identifying stress and peer influence as triggers."
        ),
        birp_intervention=(
            "Staff utilized motivational interviewing techniques, explored triggers, and reinforced alternative coping strategies."
        ),
        birp_response=(
            "Client demonstrated partial insight into substance use patterns and was receptive to discussing alternative coping options."
        ),
        birp_plan="Continue supporting insight development, reinforce coping strategies, and monitor for ongoing risk factors related to substance use.",
        risk_level="Moderate",
        risk_type="Substance Use / DTS / DTO (secondary)",
        risk_notes=(
            "Substance use increases risk for impaired judgment, emotional dysregulation, and engagement in unsafe behaviors. Continued monitoring and structured intervention are required to reduce risk and support stabilization."
        ),
    ),
    "anti_social_traits": DomainEntry(
        name="Anti-Social Traits",
        assessment=(
            "Client presents with anti-social behavioral patterns as evidenced by disregard for rules, manipulation, dishonesty, aggression, and/or limited empathy for others. "
            "Client may demonstrate difficulty with accountability, tendency to externalize blame, and engagement in behaviors that violate social or interpersonal boundaries. These patterns impact peer relationships, staff interactions, and overall participation in treatment. Contributing factors may include trauma history, attachment disruption, learned survival behaviors, environmental influences, and/or longstanding behavioral conditioning."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued engagement in harmful or rule-violating behaviors that compromise the safety and functioning of the treatment environment. These behavioral patterns significantly impair interpersonal functioning and treatment engagement, requiring structured therapeutic support, supervision, and intervention within a residential level of care to promote accountability, skill development, and behavioral change."
        ),
        goal="Client will increase accountability and demonstrate improved prosocial behavior in structured settings.",
        objective=(
            "Client will demonstrate use of at least one prosocial behavior (e.g., accepting redirection, engaging in respectful communication, or taking responsibility for actions) in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide consistent limit-setting, behavioral reinforcement, and skill-building interventions to address anti-social patterns, including promoting accountability, modeling appropriate interactions, and reinforcing prosocial behaviors."
        ),
        birp_behavior=(
            "Client engaged in rule-violating behavior, including dishonesty regarding task completion and deflecting responsibility when addressed."
        ),
        birp_intervention=(
            "Staff provided clear limit-setting, reinforced expectations, and guided client in identifying behavior and alternative responses."
        ),
        birp_response=(
            "Client demonstrated partial acknowledgment of behavior and was able to engage in discussion with staff support."
        ),
        birp_plan="Continue reinforcing accountability and support development of prosocial behaviors through consistent intervention.",
        risk_level="Moderate to High",
        risk_type="DTO / Rule-Violating Behavior",
        risk_notes=(
            "Anti-social behavioral patterns increase risk for aggression, manipulation, and disruption of the treatment environment. Structured supervision and consistent intervention are required to maintain safety and support behavioral change."
        ),
    ),
    "attachment": DomainEntry(
        name="Attachment",
        assessment=(
            "Client presents with attachment-related difficulties as evidenced by patterns of anxious, avoidant, or disorganized relational behavior, including difficulty trusting others, fear of abandonment, emotional withdrawal, or inconsistent engagement with staff and peers. "
            "Client may demonstrate push-pull dynamics, heightened sensitivity to perceived rejection, or avoidance of emotional vulnerability. These patterns impact relationship stability, treatment engagement, and ability to form safe and consistent connections. Contributing factors may include early relational trauma, inconsistent caregiving, attachment disruption, and/or environmental instability."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued relational instability, impaired treatment engagement, and difficulty forming safe and supportive connections. Attachment-related patterns significantly interfere with emotional regulation and participation in treatment, requiring structured therapeutic support within a residential level of care to promote relational safety and stability."
        ),
        goal="Client will increase ability to engage in safe, consistent, and trusting relationships within the treatment environment.",
        objective=(
            "Client will demonstrate at least one form of adaptive relational engagement (e.g., seeking support, tolerating proximity, or engaging in repair after conflict) in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide consistent, predictable interactions, relational support, and modeling of healthy attachment behaviors, including co-regulation, boundary setting, and opportunities for safe relational repair following conflict."
        ),
        birp_behavior=(
            "Client demonstrated avoidant behavior during check-in, including limited eye contact and reluctance to engage with staff support."
        ),
        birp_intervention=(
            "Staff maintained a calm presence, respected client’s need for space, and offered non-intrusive opportunities for connection."
        ),
        birp_response=(
            "Client demonstrated slight increase in engagement and remained present in interaction without escalation."
        ),
        birp_plan="Continue providing consistent relational support and reinforce safe engagement at the client’s pace.",
        risk_level="Low to Moderate",
        risk_type="Emotional Dysregulation / Relational Instability",
        risk_notes=(
            "Attachment-related patterns may contribute to emotional dysregulation, interpersonal conflict, and treatment disengagement. While not directly a safety risk, these patterns may increase vulnerability to escalation in other domains."
        ),
    ),
    "identity_self_esteem": DomainEntry(
        name="Identity / Self-Esteem",
        assessment=(
            "Client presents with identity and self-esteem difficulties as evidenced by negative self-perception, low self-worth, inconsistent sense of self, and/or difficulty identifying personal strengths, values, or goals. "
            "Client may demonstrate self-critical thinking, withdrawal, overcompensation, or reliance on external validation. These patterns impact emotional regulation, decision-making, relationships, and engagement in treatment. Contributing factors may include trauma history, chronic invalidation, identity disruption, and/or developmental challenges."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued negative self-concept, emotional distress, and vulnerability to maladaptive coping behaviors, including self-harm, withdrawal, or engagement in unsafe relationships. Identity and self-esteem difficulties significantly impair emotional functioning and treatment engagement, requiring structured therapeutic support within a residential level of care to promote stability and development of a cohesive sense of self."
        ),
        goal="Client will develop a more stable and positive sense of self and improve self-esteem.",
        objective=(
            "Client will identify and verbalize at least one personal strength, value, or positive self-attribute and demonstrate engagement in one self-supportive behavior in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide strengths-based support, identity exploration opportunities, and reflective interventions to address self-esteem, including reinforcing positive behaviors, challenging negative self-beliefs, and supporting development of personal values and goals."
        ),
        birp_behavior=(
            "Client verbalized negative self-statements and demonstrated reluctance to engage in activity due to perceived inability."
        ),
        birp_intervention=(
            "Staff provided strengths-based reflection, encouraged participation, and supported identification of positive attributes."
        ),
        birp_response=(
            "Client demonstrated partial engagement and was able to identify one positive attribute with staff support."
        ),
        birp_plan="Continue reinforcing strengths-based interventions and support development of positive self-concept.",
        risk_level="Moderate",
        risk_type="DTS / SI (secondary)",
        risk_notes=(
            "Low self-esteem and negative self-concept increase vulnerability to emotional distress, withdrawal, and self-harming behaviors. Ongoing monitoring and support are recommended to reduce risk."
        ),
    ),
    "gender_dysphoria": DomainEntry(
        name="Gender Dysphoria",
        assessment=(
            "Client presents with gender dysphoria as evidenced by distress related to incongruence between gender identity and assigned sex at birth. "
            "Client may demonstrate discomfort with physical characteristics, resistance to gendered expectations, emotional distress during identity-related interactions, or withdrawal from activities that highlight gender incongruence. These experiences impact emotional regulation, self-concept, social engagement, and overall functioning. Contributing factors may include identity suppression, environmental invalidation, trauma, and/or lack of access to affirming support systems."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of increased emotional distress, identity suppression, and vulnerability to self-harm or suicidal ideation. Gender dysphoria significantly impacts emotional functioning and sense of safety, requiring structured therapeutic support within a residential level of care to provide stabilization, affirmation, and development of adaptive coping strategies."
        ),
        goal="Client will increase emotional safety and stability in relation to gender identity and expression.",
        objective=(
            "Client will engage in at least one form of identity-affirming or emotionally supportive behavior (e.g., expressing identity, utilizing coping strategies, or seeking support) in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide affirming, nonjudgmental support and create a safe environment for identity exploration, including use of appropriate name/pronouns, emotional validation, and support for coping with dysphoria-related distress."
        ),
        birp_behavior=(
            "Client demonstrated distress during gender-related interaction, including withdrawal and reduced engagement."
        ),
        birp_intervention=(
            "Staff provided affirming language, respected client’s identity, and offered emotional support without pressure for disclosure."
        ),
        birp_response=(
            "Client demonstrated partial engagement and remained present with staff support."
        ),
        birp_plan="Continue providing affirming support and reinforce emotional safety in identity-related experiences.",
        risk_level="Moderate to High",
        risk_type="SI / DTS (secondary)",
        risk_notes=(
            "Gender dysphoria may increase vulnerability to emotional distress, self-harm, and suicidal ideation, particularly in environments perceived as invalidating. Ongoing monitoring and affirming support are required to maintain safety."
        ),
    ),
    "cultural_identity_stress": DomainEntry(
        name="Cultural / Identity-Based Stress",
        assessment=(
            "Client presents with cultural and/or identity-based stress as evidenced by experiences of marginalization, invalidation, or difficulty navigating environments that do not reflect or affirm their identity. "
            "Client may demonstrate withdrawal, mistrust of authority, emotional reactivity, or reluctance to engage in treatment settings perceived as unsafe or invalidating. These experiences impact emotional regulation, sense of belonging, and engagement in treatment. Contributing factors may include systemic inequities, prior experiences of discrimination, cultural disconnection, and/or chronic identity-based stress."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued emotional distress, disengagement from treatment, and increased vulnerability to maladaptive coping behaviors. Cultural and identity-based stress significantly impacts emotional functioning and relational safety, requiring structured therapeutic support within a residential level of care to promote stabilization, trust-building, and culturally responsive care."
        ),
        goal="Client will increase sense of safety, belonging, and engagement within the treatment environment.",
        objective=(
            "Client will demonstrate at least one form of adaptive engagement (e.g., expressing needs, participating in discussion, or seeking support) in 3 out of 5 observed opportunities within a culturally safe context."
        ),
        intervention=(
            "Staff will provide culturally responsive, trauma-informed care, including validating identity-based experiences, maintaining non-defensive communication, and creating opportunities for safe expression and engagement without pressure."
        ),
        birp_behavior=(
            "Client demonstrated reluctance to engage in group discussion, expressing frustration with perceived lack of understanding from peers and staff."
        ),
        birp_intervention=(
            "Staff validated client’s experience, maintained non-defensive stance, and provided space for expression without pressure."
        ),
        birp_response=(
            "Client demonstrated partial engagement and remained present, with decreased emotional reactivity."
        ),
        birp_plan="Continue reinforcing culturally responsive support and promote safe opportunities for engagement and expression.",
        risk_level="Low to Moderate (can escalate)",
        risk_type="Emotional Dysregulation / SI (secondary)",
        risk_notes=(
            "Cultural and identity-based stress may contribute to emotional distress, mistrust, and disengagement from treatment. Prolonged invalidation may increase risk for escalation into higher-risk domains such as self-harm or withdrawal."
        ),
    ),
    "external_support": DomainEntry(
        name="External Support",
        assessment=(
            "Client presents with limited, inconsistent, or developing external support systems as evidenced by minimal involvement from family, caregivers, or other supportive individuals, or difficulty maintaining stable relationships outside of treatment. "
            "Client may demonstrate reluctance to engage in discussions about support systems, emotional responses to inconsistent contact, or overreliance on a single support figure. These patterns impact emotional stability, sense of safety, and long-term treatment outcomes. Contributing factors may include family disruption, trauma, placement instability, or lack of access to consistent and supportive relationships."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued relational instability and difficulty maintaining progress outside of structured care. Limited or inconsistent external support significantly impacts emotional functioning and discharge readiness, requiring structured therapeutic support within a residential level of care to build stability, strengthen connections, and develop alternative support systems."
        ),
        goal="Client will increase engagement with and utilization of supportive relationships.",
        objective=(
            "Client will identify at least one support person and engage in one form of connection (e.g., phone call, visit, or discussion about support) in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will support development of external support systems through facilitating communication, validating relational experiences, and helping client identify and build safe and consistent connections."
        ),
        birp_behavior=(
            "Client expressed reluctance to engage in discussion about family support and reported limited contact with identified support figures."
        ),
        birp_intervention=(
            "Staff validated client’s experience, explored alternative support options, and encouraged identification of safe connections."
        ),
        birp_response=(
            "Client demonstrated partial openness to discussing support systems and identified one potential support figure."
        ),
        birp_plan="Continue supporting development of external connections and reinforce engagement with identified supports.",
        risk_level="Low to Moderate",
        risk_type="SI / DTS (secondary, due to isolation)",
        risk_notes=(
            "Limited external support increases vulnerability to emotional distress, isolation, and relapse following discharge. Strengthening support systems is essential to reduce long-term risk."
        ),
    ),
    "institutional_experience": DomainEntry(
        name="Institutional Experience",
        assessment=(
            "Client presents with institutional experience factors as evidenced by prior placement in structured systems and demonstrated patterns of either over-compliance, disengagement, mistrust, or behavioral adaptation to institutional environments. "
            "Client may demonstrate familiarity with program structure without meaningful engagement, resistance to authority, or difficulty forming authentic therapeutic relationships. These patterns impact treatment engagement, relational dynamics, and responsiveness to interventions. Contributing factors may include repeated placement history, system-related trauma, and learned survival strategies within institutional settings."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued disengagement, superficial compliance without meaningful progress, and difficulty benefiting from treatment. Institutional experience significantly impacts the client’s ability to engage authentically in care, requiring structured therapeutic support within a residential level of care to address learned patterns and promote genuine behavioral and emotional change."
        ),
        goal="Client will increase authentic engagement in treatment and reduce reliance on institutional survival behaviors.",
        objective=(
            "Client will demonstrate one instance of genuine emotional or behavioral engagement (e.g., expressing thoughts, reflecting on behavior, or participating beyond compliance) in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide consistent, relationally focused support and encourage authentic engagement, including validating client experiences within systems, challenging superficial compliance, and promoting meaningful participation in treatment activities."
        ),
        birp_behavior=(
            "Client demonstrated compliance with program expectations but limited emotional engagement, including minimal participation in discussion and lack of personal reflection."
        ),
        birp_intervention=(
            "Staff encouraged deeper engagement, validated client’s prior system experiences, and provided opportunities for authentic expression."
        ),
        birp_response=(
            "Client demonstrated slight increase in engagement and provided brief personal input with staff support."
        ),
        birp_plan="Continue supporting authentic engagement and reinforce participation beyond compliance.",
        risk_level="Low to Moderate",
        risk_type="Treatment Disengagement / Relapse Risk",
        risk_notes=(
            "Institutional adaptation may result in superficial compliance without internal change, increasing risk for relapse or regression following discharge. Continued monitoring and engagement-focused intervention are recommended."
        ),
    ),
    "csec": DomainEntry(
        name="CSEC",
        assessment=(
            "Client presents with history or indicators of commercial sexual exploitation as evidenced by involvement in survival-based or coerced sexual activity, trauma bonding to exploitive individuals, and/or engagement in high-risk relational or behavioral patterns. "
            "Client may demonstrate mistrust of authority, minimization or normalization of exploitation, emotional dysregulation, or difficulty separating identity from exploitative experiences. These patterns impact emotional stability, safety, identity development, and treatment engagement. Contributing factors may include trauma history, attachment disruption, coercion, environmental instability, and lack of consistent protective support."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued exploitation, unsafe relationships, and engagement in high-risk behaviors, including running away from placement. These experiences significantly impair safety, emotional functioning, and decision-making, requiring structured therapeutic support, supervision, and trauma-informed intervention within a residential level of care to ensure protection and stabilization."
        ),
        goal="Client will increase safety awareness and develop separation between identity and exploitative experiences.",
        objective=(
            "Client will identify at least one unsafe relational pattern or trigger and demonstrate use of one safety or coping strategy in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide trauma-informed, nonjudgmental support focused on safety, identity development, and relational awareness, including validating experiences, avoiding confrontation, and reinforcing protective behaviors and safe connections."
        ),
        birp_behavior=(
            "Client referenced past relationships associated with exploitation and demonstrated ambivalence regarding safety and relational boundaries."
        ),
        birp_intervention=(
            "Staff provided nonjudgmental support, validated client’s experience, and introduced concepts of relational safety and control."
        ),
        birp_response=(
            "Client demonstrated partial engagement and was receptive to discussion without escalation or withdrawal."
        ),
        birp_plan="Continue supporting development of safety awareness and reinforce separation of identity from exploitative experiences.",
        risk_level="High",
        risk_type="Elopement / DTS / Exploitation Risk",
        risk_notes=(
            "Client presents with elevated risk for re-engagement in exploitative relationships and potential elopement from placement. Ongoing monitoring, structured supervision, and trauma-informed intervention are required to maintain safety."
        ),
    ),
    "technology_screen_conflict": DomainEntry(
        name="Technology + Screen Conflict",
        assessment=(
            "Client presents with technology and screen-related conflict as evidenced by excessive or dysregulated use of devices, emotional reactivity when access is limited, and/or reliance on screens as a primary coping mechanism. "
            "Client may demonstrate irritability, withdrawal, avoidance of responsibilities, or difficulty engaging in non-screen-based activities. These patterns impact emotional regulation, social interaction, and participation in treatment programming. Contributing factors may include trauma history, need for control or escape, peer dynamics, and/or underdeveloped coping strategies."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued dysregulation, avoidance of treatment engagement, and escalation of behavioral conflict related to screen use. Technology-related behaviors significantly interfere with emotional stability and participation in structured programming, requiring therapeutic support within a residential level of care to develop adaptive coping strategies and improve functioning."
        ),
        goal="Client will reduce reliance on technology as a primary coping strategy and increase engagement in adaptive activities.",
        objective=(
            "Client will participate in at least one non-screen-based activity and demonstrate use of one alternative coping strategy during periods of screen-related distress in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide structured limits, emotional support, and skill-building interventions to address screen-related behaviors, including identifying underlying needs, reinforcing alternative activities, and supporting emotional regulation during transitions away from devices."
        ),
        birp_behavior=(
            "Client became irritable when access to device was limited and demonstrated resistance to transitioning to structured activity."
        ),
        birp_intervention=(
            "Staff provided clear expectations, offered alternative activities, and supported emotional regulation through grounding and redirection."
        ),
        birp_response=(
            "Client demonstrated partial reduction in reactivity and engaged in alternative activity with staff support."
        ),
        birp_plan="Continue reinforcing structured limits and support development of adaptive coping strategies.",
        risk_level="Low to Moderate",
        risk_type="Emotional Dysregulation / Avoidance",
        risk_notes=(
            "Technology reliance may contribute to emotional dysregulation, avoidance of treatment engagement, and behavioral conflict. Ongoing monitoring is recommended to prevent escalation into higher-risk domains."
        ),
    ),
    "social_skills_deficit": DomainEntry(
        name="Social Skills Deficit",
        assessment=(
            "Client presents with social skills deficits as evidenced by difficulty initiating or maintaining appropriate interactions, limited awareness of social cues, and/or challenges with communication, boundaries, or peer relationships. Client may demonstrate withdrawal, inappropriate responses, conflict escalation, or difficulty interpreting others’ intentions. These patterns impact peer relationships, group participation, and overall engagement in treatment. Contributing factors may include trauma history, attachment disruption, neurodevelopmental differences, social learning deficits, and/or environmental instability."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued interpersonal conflict, social isolation, and impaired functioning within group and structured environments. Social skills deficits significantly interfere with treatment engagement and relational stability, requiring structured therapeutic support within a residential level of care to develop appropriate communication and interaction skills."
        ),
        goal="Client will improve ability to engage in appropriate and effective social interactions.",
        objective=(
            "Client will demonstrate use of at least one appropriate social skill (e.g., respectful communication, turn-taking, or boundary recognition) in 3 out of 5 observed interactions."
        ),
        intervention=(
            "Staff will provide modeling, coaching, and real-time feedback to support development of social skills, including role modeling appropriate interactions, reinforcing positive behaviors, and guiding corrective responses during peer interactions."
        ),
        birp_behavior=(
            "Client demonstrated difficulty during peer interaction, including interrupting others and responding in a reactive manner."
        ),
        birp_intervention=(
            "Staff provided real-time coaching, modeled appropriate communication, and guided client in practicing alternative responses."
        ),
        birp_response=(
            "Client demonstrated partial improvement in interaction and was able to engage more appropriately with prompting."
        ),
        birp_plan="Continue reinforcing social skills and provide ongoing coaching during peer interactions.",
        risk_level="Low to Moderate",
        risk_type="DTO (secondary) / Social Conflict",
        risk_notes=(
            "Social skills deficits may contribute to peer conflict, emotional escalation, and behavioral incidents. Ongoing support is recommended to reduce risk of escalation into higher-risk domains."
        ),
    ),
    "trauma_response": DomainEntry(
        name="Trauma Response",
        assessment=(
            "Client presents with trauma-related responses as evidenced by hyperarousal (e.g., heightened reactivity, anxiety), hypoarousal (e.g., shutdown, dissociation), and/or maladaptive coping behaviors in response to perceived threat. Client may demonstrate sensitivity to triggers, difficulty regulating emotional responses, avoidance behaviors, or intrusive thoughts related to past experiences. These patterns impact emotional regulation, sense of safety, relationships, and engagement in treatment. Contributing factors include history of trauma, chronic stress exposure, attachment disruption, and/or environmental instability."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued dysregulation, impaired functioning, and reinforcement of maladaptive coping patterns related to trauma. Trauma responses significantly interfere with the client’s ability to maintain safety, regulate emotions, and engage in treatment, requiring structured, trauma-informed therapeutic support within a residential level of care to promote stabilization and recovery."
        ),
        goal="Client will increase ability to recognize and regulate trauma-related responses.",
        objective=(
            "Client will identify at least one trigger and demonstrate use of one regulation strategy (e.g., grounding, requesting support, or taking space) in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide trauma-informed care, including co-regulation, trigger identification, and emotional support, while maintaining predictable structure and avoiding re-traumatization through consistent, non-reactive interactions."
        ),
        birp_behavior=(
            "Client demonstrated heightened emotional response following a triggering interaction, including increased agitation and withdrawal."
        ),
        birp_intervention=(
            "Staff provided co-regulation, validated emotional experience, and supported grounding techniques to reduce distress."
        ),
        birp_response=(
            "Client demonstrated partial reduction in reactivity and remained present with staff support."
        ),
        birp_plan="Continue reinforcing trauma-informed interventions and support identification of triggers and coping strategies.",
        risk_level="Moderate to High",
        risk_type="DTS / DTO / SI (context-dependent)",
        risk_notes=(
            "Trauma responses may contribute to emotional dysregulation, impulsive behaviors, and increased vulnerability to self-harm or aggression. Ongoing monitoring and structured support are required to maintain safety."
        ),
    ),
    "circumstance_orientation": DomainEntry(
        name="Circumstance Orientation",
        assessment=(
            "Client presents with impaired or limited circumstance orientation as evidenced by difficulty accurately interpreting situations, understanding cause-and-effect relationships, and/or recognizing the impact of their behavior on outcomes. Client may demonstrate externalization of blame, rigid thinking patterns, or misinterpretation of social and environmental cues. These patterns impact decision-making, accountability, and ability to engage in treatment effectively. Contributing factors may include trauma history, cognitive distortions, emotional dysregulation, and/or developmental factors."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued maladaptive decision-making, repeated behavioral patterns, and limited progress in treatment due to impaired insight. Difficulty with circumstance orientation significantly interferes with the client’s ability to benefit from less structured environments, requiring therapeutic support within a residential level of care to develop insight, accountability, and adaptive thinking patterns."
        ),
        goal="Client will improve ability to accurately interpret situations and understand the impact of their behavior.",
        objective=(
            "Client will identify at least one connection between behavior and outcome and demonstrate increased insight in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide cognitive support, reflective questioning, and real-time feedback to help client identify patterns, challenge distortions, and develop more accurate interpretations of situations."
        ),
        birp_behavior=(
            "Client demonstrated difficulty recognizing the impact of their behavior during a conflict, attributing outcome solely to external factors."
        ),
        birp_intervention=(
            "Staff utilized reflective questioning and provided feedback to support understanding of behavior and consequences."
        ),
        birp_response=(
            "Client demonstrated partial insight and was able to acknowledge one contributing factor with staff support."
        ),
        birp_plan="Continue supporting development of insight and reinforce connections between behavior and outcomes.",
        risk_level="Moderate",
        risk_type="DTS / DTO (secondary, due to poor judgment)",
        risk_notes=(
            "Impaired circumstance orientation increases risk for repeated maladaptive decisions, poor judgment, and escalation into higher-risk behaviors. Continued monitoring and intervention are recommended."
        ),
    ),
    "dishonesty_function": DomainEntry(
        name="Dishonesty Function",
        assessment=(
            "Client presents with patterns of dishonesty as evidenced by misrepresentation of information, minimization, denial of behavior, or inconsistencies in reporting. These behaviors appear to serve a functional purpose, such as avoidance of consequences, protection from perceived threat, maintenance of control, or preservation of self-image. Client may demonstrate difficulty with accountability, fear-based responses to correction, or reliance on dishonesty as a learned coping strategy. These patterns impact trust, treatment engagement, and relational stability. Contributing factors may include trauma history, attachment disruption, prior punitive environments, and/or maladaptive coping patterns."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued reliance on dishonesty as a primary coping mechanism, impairing treatment progress, relational trust, and accountability. These patterns significantly interfere with the client’s ability to engage meaningfully in treatment, requiring structured therapeutic support within a residential level of care to develop adaptive coping strategies and improve honesty and accountability."
        ),
        goal="Client will increase honest communication and accountability in interactions with staff and peers.",
        objective=(
            "Client will demonstrate truthful communication or acknowledgment of behavior in 3 out of 5 observed opportunities, with or without prompting."
        ),
        intervention=(
            "Staff will provide non-punitive, supportive responses to dishonesty, including reducing perceived threat, reinforcing honesty, and helping client identify the function behind dishonest behavior to develop alternative coping strategies."
        ),
        birp_behavior=(
            "Client provided inconsistent information regarding behavior and initially denied involvement when addressed."
        ),
        birp_intervention=(
            "Staff responded in a non-confrontational manner, reduced perceived threat, and encouraged honest communication through supportive questioning."
        ),
        birp_response=(
            "Client demonstrated partial acknowledgment of behavior and engaged in discussion with staff support."
        ),
        birp_plan="Continue reinforcing honest communication and support development of accountability without increasing defensive responses.",
        risk_level="Moderate",
        risk_type="Treatment Interference / DTO (secondary)",
        risk_notes=(
            "Dishonesty may interfere with accurate assessment, safety planning, and treatment progress. While not inherently a direct safety risk, it may contribute to escalation in other domains if underlying needs are not addressed."
        ),
    ),
    "future_orientation": DomainEntry(
        name="Future Orientation",
        assessment=(
            "Client presents with limited or impaired future orientation as evidenced by difficulty identifying goals, lack of planning for the future, or focus on immediate needs without consideration of long-term consequences. Client may demonstrate hopelessness, lack of motivation, or inability to connect current behavior to future outcomes. These patterns impact decision-making, treatment engagement, and readiness for transition out of structured care. Contributing factors may include trauma history, depression, instability in environment, and/or limited exposure to future planning or goal-setting."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued short-term decision-making, disengagement from treatment goals, and difficulty maintaining stability outside of structured care. Impaired future orientation significantly interferes with the client’s ability to transition successfully to lower levels of care, requiring structured therapeutic support within a residential setting to develop goal-setting, planning, and forward-thinking skills."
        ),
        goal="Client will increase ability to identify and work toward future goals.",
        objective=(
            "Client will identify at least one short-term or long-term goal and demonstrate one action toward that goal in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide goal-setting support, motivational engagement, and structured planning interventions to help client connect current behaviors to future outcomes and develop realistic and achievable goals."
        ),
        birp_behavior=(
            "Client demonstrated limited engagement in future planning and expressed uncertainty about goals following discharge."
        ),
        birp_intervention=(
            "Staff provided support in identifying short-term goals and explored connections between current behavior and future outcomes."
        ),
        birp_response=(
            "Client demonstrated partial engagement and was able to identify one potential goal with staff support."
        ),
        birp_plan="Continue reinforcing goal-setting and support development of future-oriented thinking.",
        risk_level="Moderate",
        risk_type="SI / DTS (secondary, due to hopelessness)",
        risk_notes=(
            "Limited future orientation may contribute to hopelessness, disengagement, and increased vulnerability to maladaptive behaviors. Ongoing support is recommended to reduce risk and improve long-term stability."
        ),
    ),
    "functioning_level": DomainEntry(
        name="Functioning Level",
        assessment=(
            "Client presents with impaired functioning level as evidenced by difficulty maintaining consistent performance across daily living tasks, emotional regulation, interpersonal interactions, and/or structured activities such as school or treatment programming. Client may demonstrate variability in functioning, requiring prompting, redirection, or support to complete tasks. These impairments impact independence, safety, and ability to function in less structured environments. Contributing factors may include mental health symptoms, trauma history, cognitive limitations, and/or environmental instability."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of continued impairment in daily functioning, inability to maintain safety and stability, and unsuccessful transition to lower levels of care. Reduced functioning level significantly interferes with the client’s ability to meet basic expectations independently, requiring structured therapeutic support within a residential level of care to promote stabilization and skill development."
        ),
        goal="Client will improve overall functioning and increase independence in daily activities.",
        objective=(
            "Client will complete at least one daily task (e.g., hygiene, participation in programming, or assigned responsibility) with decreased prompting in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide structured support, prompting, and skill-building interventions to improve functioning, including breaking tasks into manageable steps, reinforcing completion, and gradually reducing support as independence increases."
        ),
        birp_behavior=(
            "Client required multiple prompts to engage in daily activity and demonstrated difficulty completing tasks independently."
        ),
        birp_intervention=(
            "Staff provided step-by-step guidance, prompting, and reinforcement to support task completion."
        ),
        birp_response=(
            "Client demonstrated partial completion of task with support and responded to prompting."
        ),
        birp_plan="Continue supporting task completion and gradually reduce prompting to increase independence.",
        risk_level="Moderate",
        risk_type="DTS / SI (secondary due to impairment)",
        risk_notes=(
            "Impaired functioning may increase vulnerability to emotional distress, instability, and inability to maintain safety in less structured environments. Continued monitoring and support are required."
        ),
    ),
    "gravely_disabled": DomainEntry(
        name="Gravely Disabled",
        assessment=(
            "Client presents with gravely disabled functioning as evidenced by inability or significant difficulty meeting basic needs, including safety, self-care, decision-making, or utilization of available resources. Client may demonstrate impaired judgment, disorganized behavior, severe emotional or cognitive dysregulation, and/or inability to maintain basic daily functioning without continuous support. These impairments impact the client’s ability to care for themselves, remain safe, and function independently. Contributing factors may include severe mental health symptoms, psychosis, trauma, cognitive limitations, and/or environmental instability."
        ),
        medical_necessity=(
            "Without intervention, client is at risk of significant harm due to inability to maintain safety or meet basic needs independently. Level of impairment requires continuous supervision and structured therapeutic support within a residential level of care to ensure safety, stabilization, and restoration of functioning."
        ),
        goal="Client will increase ability to maintain safety and meet basic needs with reduced support.",
        objective=(
            "Client will complete at least one basic self-care or safety-related task (e.g., hygiene, following safety instructions, or engaging in structured activity) with support in 3 out of 5 observed opportunities."
        ),
        intervention=(
            "Staff will provide high-level supervision, structured support, and step-by-step guidance to address impaired functioning, including ensuring safety, reinforcing basic routines, and coordinating with clinical and psychiatric services as needed."
        ),
        birp_behavior=(
            "Client demonstrated impaired functioning, including difficulty engaging in basic self-care and limited awareness of safety needs."
        ),
        birp_intervention=(
            "Staff provided direct support, prompting, and supervision to ensure completion of basic tasks and maintain safety."
        ),
        birp_response=(
            "Client demonstrated partial participation with support and required continued assistance to maintain functioning."
        ),
        birp_plan="Continue high-level supervision and structured support to ensure safety and improve basic functioning.",
        risk_level="High",
        risk_type="DTS / SI / Inability to Maintain Safety",
        risk_notes=(
            "Client presents with significant impairment in ability to meet basic needs and maintain safety. Risk is elevated due to reduced capacity for independent functioning. Continuous supervision and structured intervention are required."
        ),
    ),
}


DEFAULT_DOMAIN_ORDER: List[str] = [
    "anxiety",
    "depression",
    "emotional_dysregulation",
    "sleep_somatic_disturbance",
    "psychosis",
    "suicidality",
    "dto",
    "dts",
    "substance_abuse",
    "anti_social_traits",
    "attachment",
    "identity_self_esteem",
    "gender_dysphoria",
    "cultural_identity_stress",
    "external_support",
    "institutional_experience",
    "csec",
    "technology_screen_conflict",
    "social_skills_deficit",
    "trauma_response",
    "circumstance_orientation",
    "dishonesty_function",
    "future_orientation",
    "functioning_level",
    "gravely_disabled",
]


ALIASES: Dict[str, str] = {
    "danger_to_others": "dto",
    "danger_to_self": "dts",
    "identity": "identity_self_esteem",
    "self_esteem": "identity_self_esteem",
    "cultural_stress": "cultural_identity_stress",
    "technology": "technology_screen_conflict",
    "screen_conflict": "technology_screen_conflict",
    "social_skills": "social_skills_deficit",
    "sleep_and_somatic_disturbance": "sleep_somatic_disturbance",
}


def normalize_domain_key(value: str) -> str:
    return (
        value.strip()
        .lower()
        .replace("&", "and")
        .replace("/", "_")
        .replace("-", "_")
        .replace(" ", "_")
    )


def resolve_domain_key(value: str) -> str:
    key = normalize_domain_key(value)
    key = ALIASES.get(key, key)
    if key not in DOMAIN_LIBRARY:
        valid = ", ".join(DEFAULT_DOMAIN_ORDER)
        raise KeyError(f"Unknown domain '{value}'. Valid domain keys: {valid}")
    return key


@dataclass
class ClientReportInput:
    client_name: str
    selected_domains: List[str]
    presenting_concerns: Optional[str] = None
    level_of_care: str = "residential"
    risk_notes_override: Optional[str] = None


class ClientWellReportGenerator:
    def __init__(self, domain_library: Optional[Dict[str, DomainEntry]] = None):
        self.domain_library = domain_library or DOMAIN_LIBRARY

    def get_domains(self, selected_domains: List[str]) -> List[DomainEntry]:
        resolved = [resolve_domain_key(d) for d in selected_domains]
        return [self.domain_library[key] for key in resolved]

    def build_assessment(self, domains: List[DomainEntry], presenting_concerns: Optional[str] = None) -> str:
        parts: List[str] = []
        if presenting_concerns:
            parts.append(f"Presenting concerns: {presenting_concerns}")
        for d in domains:
            parts.append(f"{d.name}: {d.assessment}")
        return "\n\n".join(parts)

    def build_medical_necessity(self, domains: List[DomainEntry], level_of_care: str) -> str:
        items = [
            f"{d.name}: {d.medical_necessity.replace('residential level of care', f'{level_of_care} level of care')}"
            for d in domains
        ]
        return "\n\n".join(items)

    def build_treatment_plan(self, domains: List[DomainEntry]) -> str:
        blocks: List[str] = []
        for d in domains:
            blocks.append(
                f"{d.name}\n"
                f"Goal: {d.goal}\n"
                f"Objective: {d.objective}\n"
                f"Intervention: {d.intervention}"
            )
        return "\n\n".join(blocks)

    def build_birp(self, domains: List[DomainEntry]) -> str:
        blocks: List[str] = []
        for d in domains:
            blocks.append(
                f"{d.name}\n"
                f"Behavior: {d.birp_behavior}\n"
                f"Intervention: {d.birp_intervention}\n"
                f"Response: {d.birp_response}\n"
                f"Plan: {d.birp_plan}"
            )
        return "\n\n".join(blocks)

    def build_risk_summary(self, domains: List[DomainEntry], risk_notes_override: Optional[str] = None) -> str:
        blocks: List[str] = []
        for d in domains:
            notes = risk_notes_override if risk_notes_override else d.risk_notes
            blocks.append(
                f"{d.name}\n"
                f"Risk Level: {d.risk_level}\n"
                f"Risk Type: {d.risk_type}\n"
                f"Notes: {notes}"
            )
        return "\n\n".join(blocks)

    def generate_report(self, report_input: ClientReportInput) -> Dict[str, str]:
        domains = self.get_domains(report_input.selected_domains)
        return {
            "client_name": report_input.client_name,
            "domains": ", ".join(d.name for d in domains),
            "assessment": self.build_assessment(domains, report_input.presenting_concerns),
            "medical_necessity": self.build_medical_necessity(domains, report_input.level_of_care),
            "treatment_plan": self.build_treatment_plan(domains),
            "birp": self.build_birp(domains),
            "risk_summary": self.build_risk_summary(domains, report_input.risk_notes_override),
        }

    def generate_text_report(self, report_input: ClientReportInput) -> str:
        report = self.generate_report(report_input)
        sections = [
            f"CLIENTWELL AUTO-FILL REPORT\nClient: {report['client_name']}\nDomains: {report['domains']}",
            f"ASSESSMENT\n{report['assessment']}",
            f"MEDICAL NECESSITY\n{report['medical_necessity']}",
            f"TREATMENT PLAN\n{report['treatment_plan']}",
            f"BIRP NOTE CONTENT\n{report['birp']}",
            f"RISK SUMMARY\n{report['risk_summary']}",
        ]
        return "\n\n".join(sections)
