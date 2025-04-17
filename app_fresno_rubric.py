PUBLISHED = True
APP_URL = "https://fresno-rubric.streamlit.app"
APP_IMAGE = "fresno_rubric_flat.webp"

APP_TITLE = "Fresno Test for Evidence Based Medicine"
APP_INTRO = """This is an application that applies the Fresno test (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC143529/pdf/319.pdf) for competence in evidence based medicine, and provides feedback via AI using the same rubric as the Fresno test. It is an experimental app to determine the correlation between AI scoring and human scoring for a validated accurate and effective rubric. 
"""

APP_HOW_IT_WORKS = """
 This is an **AI-Tutored Rubric exercise** that acts as a tutor guiding a student through a shared asset, like an article. It uses the OpenAI Assistants API with GPT-4. The **questions and rubric** are defined by a **faculty**. The **feedback and the score** are generarated by the **AI**. 

It can:

1. provide feedback on a student's answers to questions about an asset
2. roughly "score" a student to determine if they can move on to the next section.  

Scoring is based on a faculty-defined rubric on the backend. These rubrics can be simple (i.e. "full points if the student gives a thoughtful answer") or specific with different criteria and point thresholds. The faculty also defines a minimum pass threshold for each question. The threshold could be as low as zero points to pass any answer, or it could be higher. 

Using AI to provide feedback and score like this is a very experimental process. Some things to note: 

 - AIs make mistakes. Users are encourage to skip a question if the AI is not understanding them or giving good feedback. 
 - The AI might say things that it can't do, like "Ask me anything about the article". I presume further refinement can reduce these kinds of responses. 
 - Scoring is highly experimental. At this point, it should mainly be used to gauge if a user gave an approximately close answer to what the rubric suggests. It is not recommended to show the user the numeric score. 
 - Initial testing indicates that the AI is a very easy grader. This is probably good in this experiment, and it may be refined with different prompting. 
 """

SHARED_ASSET = {"path":"shared_assets/EBM Fresno Test grading rubric.pdf",
"name":"Fresno State Grading Rubric",
"button_text":"View the Rubric"
}

HTML_BUTTON = {
    "url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC143529/pdf/319.pdf",
    "button_text":"Read the Fresno Test Study"
}

SYSTEM_PROMPT = "You are an expert in evidence based medicine who grades submissions based on the Fresno Test of Evidence Based Medicine Grading Rubric."

PHASES = {
    "phase1": {
        "name": "PatientEncounter1",
        "fields": {
            "case_1": {
                "type": "markdown",
                "body": """You have just seen Lydia who recently delivered a healthy baby. She plans to breastfeed, but also wants to start oral contraception.
You generally prefer to prescribe combination oral contraceptives (estrogen + progesterone) but you have been told that these
might more negatively affect her breastmilk production than progesterone only pills. """,
            },
            "clinical_question_1": {
                "type": "text_area",
                "label": "Write a focused clinical question for this patient encounter that will help you organize a search of the clinical literature for an answer and choose the best article from among those you find. ",
                "value": """In postpartum women who are breastfeeding, how do combination oral contraceptives (estrogen + progesterone) compare to progestin-only pills in terms of effects on breastmilk production?"""
            }
        },
        "phase_instructions": """Provide brief feedback for the student based on the scoring rubric here. When in doubt, consider whether what was written will contribute to an optimally specific search of the clinical literature.
        Rubric:
        1. Population
            3 points - Multiple relevant descriptors. e.g., "post partum woman," "breast feeding/lactating mother" or "breastfeeding mom desiring contraception," or "breast fed newborn". Note: "breastfeeding woman" is considered two descriptors.
            2 points - One appropriate descriptor as above examples. e.g., "woman," or "infant" or "breastfeeding".
            1 point - A single general descriptor unlikely to contribute to search. e.g., "patient".
            0 points - None of the above present.
        2. Intervention
            3 points - Includes specific intervention of interest. e.g., combined contraceptives (estrogen and progesterone), or specific individual components of contraception such as "estrogen".
            2 points - Mentions contraception or type of intervention. e.g., oral contraceptives, or hormones.
            1 point - Mentions intervention but unlikely to contribute to search. e.g., "methods," "options," "treatments".
            0 points - None of the above present.
        3. Comparison
            3 points - Identifies specific alternative of interest since patient wants to use oral contraception. e.g., progesterone-only contraception.
            2 points - Mentions a specific comparison group. e.g., placebo, or a specific form of contraception, or mothers not taking OCP’s.
            1 point - Mentions comparison but unlikely to contribute to search. e.g., "compared to other methods". Note: Using a plural non-specific term, e.g., "various treatment options," should only be counted once in the comparison column.
            0 points - None of the above present.
        4. Outcome
            3 points - Outcome that is objective and meaningful to the patient. e.g., infant growth rate, number of lactation "dropouts," or maternal satisfaction with infant satiety or milk flow.
            2 points - Non-specific outcome. e.g., "milk" or "breastfeeding". OR disease-oriented outcome such as milk volume without accompanying measure of clinical relevance. e.g., "milk volume" or "chemical composition of milk" or "breastmilk production".
            1 point - Reference to outcome, but so general as to be unlikely to contribute to search. e.g., "effects" or "change the outcome".
            0 points - None of the above present.
        """,
        "user_prompt": "{clinical_question_1}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 4,
        "rubric": """
        1. Population
            3 points - Multiple relevant descriptors. e.g., "post partum woman," "breast feeding/lactating mother" or "breastfeeding mom desiring contraception," or "breast fed newborn". Note: "breastfeeding woman" is considered two descriptors.
            2 points - One appropriate descriptor as above examples. e.g., "woman," or "infant" or "breastfeeding".
            1 point - A single general descriptor unlikely to contribute to search. e.g., "patient".
            0 points - None of the above present.
        2. Intervention
            3 points - Includes specific intervention of interest. e.g., combined contraceptives (estrogen and progesterone), or specific individual components of contraception such as "estrogen".
            2 points - Mentions contraception or type of intervention. e.g., oral contraceptives, or hormones.
            1 point - Mentions intervention but unlikely to contribute to search. e.g., "methods," "options," "treatments".
            0 points - None of the above present.
        3. Comparison
            3 points - Identifies specific alternative of interest since patient wants to use oral contraception. e.g., progesterone-only contraception.
            2 points - Mentions a specific comparison group. e.g., placebo, or a specific form of contraception, or mothers not taking OCP’s.
            1 point - Mentions comparison but unlikely to contribute to search. e.g., "compared to other methods". Note: Using a plural non-specific term, e.g., "various treatment options," should only be counted once in the comparison column.
            0 points - None of the above present.
        4. Outcome
            3 points - Outcome that is objective and meaningful to the patient. e.g., infant growth rate, number of lactation "dropouts," or maternal satisfaction with infant satiety or milk flow.
            2 points - Non-specific outcome. e.g., "milk" or "breastfeeding". OR disease-oriented outcome such as milk volume without accompanying measure of clinical relevance. e.g., "milk volume" or "chemical composition of milk" or "breastmilk production".
            1 point - Reference to outcome, but so general as to be unlikely to contribute to search. e.g., "effects" or "change the outcome".
            0 points - None of the above present.
                """,
        "allow_revisions": False,
        "allow_skip": True,
        "show_prompt": True,
        "read_only_prompt": True
    },
    "phase2": {
        "name": "Patient Encounter 2",
        "fields": {
            "case_2": {
                "type": "markdown",
                "body": """John is an 11 year old boy who presents with primary enuresis. He has grown frustrated with the inconvenience and
embarrassment of his problem. You have excluded the possibility of urinary tract anomalies and infection as possible causes. You
consider recommending a bedwetting alarm, but a colleague tells you he thinks they’re "worthless" and suggests that you treat with
imiprimine or desmopressin. """,
            },
            "clinical_question_2": {
                "type": "text_area",
                "label": "Write a focused clinical question for this patient encounter that will help you organize a search of the clinical literature for an answer and choose the best article from among those you find. ",
                "value": "In children with primary enuresis, how do bedwetting alarms compare to pharmacological treatments (such as imipramine or desmopressin) in terms of efficacy and long-term outcomes?"
            }
        },
        "phase_instructions": """Provide brief feedback for the student based on the scoring rubric here. When in doubt, consider whether what was written will contribute to an optimally specific search of the clinical literature.
        1. Population
            3 points - Multiple relevant descriptors. e.g., "boy with primary enuresis," specific age group, gender, exclude infection or anatomic anomalies. Note: "primary enuresis" is considered two descriptors.
            2 points - One appropriate descriptor as above examples. e.g., "enuresis" or "child".
            1 point - A single general descriptor unlikely to contribute to search. e.g., "patient".
            0 points - None of the above present.
        2. Intervention
            3 points - Specific intervention of interest. e.g., bedwetting alarm.
            2 points - Mentions type of intervention without specifics. e.g., "Behavior modification".
            1 point - Mentions intervention but unlikely to contribute to search. e.g., "methods," "options," "treatments".
            0 points - None of the above present.
        3. Comparison
            3 points - Identifies specific alternative treatment of interest. e.g., "desmopressin acetate" or "imipramine" or "antidepressants".
            2 points - Mentions a specific comparison group. e.g., placebo or medical treatment or no treatment.
            1 point - Mentions comparison but unlikely to contribute to search. e.g., "compared to other methods". Note: Using a plural non-specific term, e.g., "various treatment options," should only be counted once in the Comparison column.
            0 points - None of the above present.
        4. Outcome
            3 points - Outcome that is objective and meaningful to patient. e.g., dry nights.
            2 points - Disease-oriented outcome without accompanying measure of clinical relevance. e.g., "urine output".
            1 point - Reference to outcome, but so general as to be unlikely to contribute to search. e.g., "effective," "improvement," "success," "change the outcome".
            0 points - None of the above present.
        """,
        "user_prompt": "{clinical_question_2}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 4,
        "rubric": """
         1. Population
            3 points - Multiple relevant descriptors. e.g., "boy with primary enuresis," specific age group, gender, exclude infection or anatomic anomalies. Note: "primary enuresis" is considered two descriptors.
            2 points - One appropriate descriptor as above examples. e.g., "enuresis" or "child".
            1 point - A single general descriptor unlikely to contribute to search. e.g., "patient".
            0 points - None of the above present.
        2. Intervention
            3 points - Specific intervention of interest. e.g., bedwetting alarm.
            2 points - Mentions type of intervention without specifics. e.g., "Behavior modification".
            1 point - Mentions intervention but unlikely to contribute to search. e.g., "methods," "options," "treatments".
            0 points - None of the above present.
        3. Comparison
            3 points - Identifies specific alternative treatment of interest. e.g., "desmopressin acetate" or "imipramine" or "antidepressants".
            2 points - Mentions a specific comparison group. e.g., placebo or medical treatment or no treatment.
            1 point - Mentions comparison but unlikely to contribute to search. e.g., "compared to other methods". Note: Using a plural non-specific term, e.g., "various treatment options," should only be counted once in the Comparison column.
            0 points - None of the above present.
        4. Outcome
            3 points - Outcome that is objective and meaningful to patient. e.g., dry nights.
            2 points - Disease-oriented outcome without accompanying measure of clinical relevance. e.g., "urine output".
            1 point - Reference to outcome, but so general as to be unlikely to contribute to search. e.g., "effective," "improvement," "success," "change the outcome".
            0 points - None of the above present.
                """,
        "allow_revisions": False,
        "allow_skip": True,
        "show_prompt": True,
        "read_only_prompt": True
    },
    "phase3": {
        "name": "Information Sources",
        "fields": {
            "information_sources": {
                "type": "text_area",
                "label": "Where might clinicians go to find an answer to questions like these? Name as many possible types or categories of information sources as you can. You may feel that some are better than others, but discuss as many as you can to demonstrate your awareness of the strengths and weaknesses of common information sources in clinical practice. Describe the most important advantages and disadvantages for each type of information source you list. ",
                "value": """Peer-Reviewed Journals
Advantages:
High-quality, evidence-based research; rigorous peer review process ensures reliability.
Covers a wide range of topics and often includes systematic reviews and meta-analyses.
Disadvantages:
Access may be restricted by paywalls; not all clinicians have subscriptions.
Research may be too specialized or complex for practical application without a strong background in the area.

Clinical Guidelines
Advantages:
Developed by expert panels; synthesize evidence to provide clear recommendations.
Often accessible through professional organizations, providing practical guidance.
Disadvantages:
May not be updated frequently; can lag behind new research.
Recommendations may not apply to all patient populations or settings."""
            }
        },
        "phase_instructions": """The student has been asked "Where might clinicians go to find an answer to questions like these? Name as many possible types or categories of information sources as you can. You may feel that some are better than others, but discuss as many as you can to demonstrate your awareness of the strengths and weaknesses of common information sources in clinical practice. Describe the most important advantages and disadvantages for each type of information source you list.". The student will respond. Provide brief feedback for the student based on the scoring rubric here:
        1. Sources
            6 points - At least four types of sources listed. Types include: electronic databases of original literature (e.g., Medline, Embase, CINAHL), journals (e.g., JAMA, NEJM), textbooks (e.g., Merck, Harrison's, monographs), Systematic Reviews (e.g., Cochrane), EBM publications or databases of pre-appraised information (e.g., Best Evidence, InfoRetriever, DynaMed, ACPJC, Clinical Evidence), Medical websites (e.g., MDConsult, PraxisMD, SumSearch), General internet search (e.g., Google, Yahoo), Clinical Guidelines (e.g., Guideline Clearinghouse), Professional Organizations (e.g., AAFP, La Leche League, NIH website), or People (e.g., colleague, consultant, attending, librarian).
            4 points - Three types of sources listed.
            2 points - Two types of sources listed.
            0 points - No variety. Only one source listed, or all sources of same type.
        2. Convenience
            6 points - Discussion includes at least 2 specific issues related to convenience, or mentions the same issue while discussing two different sources. Issues may include: Cost (e.g., "free," "subscription only"), Speed (e.g., "fast," "takes time"), Ease of search (e.g., "must know how to narrow search," "easy to navigate"), Ease of use (e.g., "concise" and "NNTs already calculated"), Availability (e.g., "readily available online").
            4 points - Includes 1 specific issue/explanation related to convenience.
            2 points - Mentions convenience involved in using one or more sources, but without explanation. e.g., "convenient," "easy," or "difficult".
            0 points - No mention of convenience.
        3. Clinical Relevance
            6 points - Discussion includes at least 2 specific issues related to relevance, or mentions the same issue while discussing two different sources. Issues may include: clinically relevant outcomes, written for clinical application (e.g., "pertinent," "info on adverse effects" or "has patient information sheets"), appropriate specialty focus (e.g., "directed at FPs"), information applicable to patient in question (e.g., "can go over details of this particular patient"), includes specific interventions in question, specificity (overview vs. targeted), comprehensiveness of source (e.g., "she can find anything").
            4 points - Includes 1 specific issue/explanation related to relevance.
            2 points - Mentions relevance of using one or more source, but without explanation. e.g., "relevant".
            0 points - No mention of relevance.
        4. Validity
            6 points - Discussion includes at least 2 specific issues related to validity, or mentions the same issue while discussing two different sources. Issues may include: certainty of validity (e.g., "quality is uncertain" or "has not been screened" or "needs to be critically appraised"), evidence-based approach (e.g., "evidence-based" or "Grade 1 Evidence"), expert bias, systematic approach, peer review, ability to verify, standard of care, enough information provided to critique validity (e.g., "abstract only" or "not available full-text"), up-to-date/outdated.
            4 points - Includes 1 specific issue/explanation related to validity.
            2 points - Mentions validity of using one or more source, but without explanation. e.g., "good," "junk".
            0 points - No mention of validity.
            """,
        "user_prompt": "{information_sources}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 4,
        "rubric": """
        1. Sources
            6 points - At least four types of sources listed. Types include: electronic databases of original literature (e.g., Medline, Embase, CINAHL), journals (e.g., JAMA, NEJM), textbooks (e.g., Merck, Harrison's, monographs), Systematic Reviews (e.g., Cochrane), EBM publications or databases of pre-appraised information (e.g., Best Evidence, InfoRetriever, DynaMed, ACPJC, Clinical Evidence), Medical websites (e.g., MDConsult, PraxisMD, SumSearch), General internet search (e.g., Google, Yahoo), Clinical Guidelines (e.g., Guideline Clearinghouse), Professional Organizations (e.g., AAFP, La Leche League, NIH website), or People (e.g., colleague, consultant, attending, librarian).
            4 points - Three types of sources listed.
            2 points - Two types of sources listed.
            0 points - No variety. Only one source listed, or all sources of same type.
        2. Convenience
            6 points - Discussion includes at least 2 specific issues related to convenience, or mentions the same issue while discussing two different sources. Issues may include: Cost (e.g., "free," "subscription only"), Speed (e.g., "fast," "takes time"), Ease of search (e.g., "must know how to narrow search," "easy to navigate"), Ease of use (e.g., "concise" and "NNTs already calculated"), Availability (e.g., "readily available online").
            4 points - Includes 1 specific issue/explanation related to convenience.
            2 points - Mentions convenience involved in using one or more sources, but without explanation. e.g., "convenient," "easy," or "difficult".
            0 points - No mention of convenience.
        3. Clinical Relevance
            6 points - Discussion includes at least 2 specific issues related to relevance, or mentions the same issue while discussing two different sources. Issues may include: clinically relevant outcomes, written for clinical application (e.g., "pertinent," "info on adverse effects" or "has patient information sheets"), appropriate specialty focus (e.g., "directed at FPs"), information applicable to patient in question (e.g., "can go over details of this particular patient"), includes specific interventions in question, specificity (overview vs. targeted), comprehensiveness of source (e.g., "she can find anything").
            4 points - Includes 1 specific issue/explanation related to relevance.
            2 points - Mentions relevance of using one or more source, but without explanation. e.g., "relevant".
            0 points - No mention of relevance.
        4. Validity
            6 points - Discussion includes at least 2 specific issues related to validity, or mentions the same issue while discussing two different sources. Issues may include: certainty of validity (e.g., "quality is uncertain" or "has not been screened" or "needs to be critically appraised"), evidence-based approach (e.g., "evidence-based" or "Grade 1 Evidence"), expert bias, systematic approach, peer review, ability to verify, standard of care, enough information provided to critique validity (e.g., "abstract only" or "not available full-text"), up-to-date/outdated.
            4 points - Includes 1 specific issue/explanation related to validity.
            2 points - Mentions validity of using one or more source, but without explanation. e.g., "good," "junk".
            0 points - No mention of validity.
        """,
        "allow_revisions": False,
        "allow_skip": True,
        "show_prompt": True,
        "read_only_prompt": False
    },
    "phase4": {
        "name": "Medline",
        "fields": {
            "medline": {
                "type": "text_area",
                "label": "If you were to search Medline for original research on one of these questions, describe what your search strategy would be. Be as specific as you can about which topics and search categories (fields) you would search. Explain your rationale for taking this approach. Describe how you might limit your search if necessary and explain your reasoning.",
                "value": ""
            }
        },
        "phase_instructions": """The student has been asked "If you were to search Medline for original research on one of these questions, describe what your search strategy would be. Be as specific as you can about which topics and search categories (fields) you would search. Explain your rationale for taking this approach. Describe how you might limit your search if necessary and explain your reasoning.". The student will respond. Provide brief feedback for the student based on the scoring rubric here:
        1. Search Terms
            8 points - 3 or more terms that reflect patient, intervention, comparison, and outcome (PICO) being considered.
            6 points - 2 terms from PICO.
            3 points - 1 term from PICO.
            0 points - Not present.
        2. Tags
            8 points - Description of search strategy reflects understanding that articles in the database are indexed by more than one field. Discusses one or more field/index/tag by name (e.g., MeSH, Title Word, Publication Title, language, Keyword, author, Journal title, etc.) and provides plausible rationale for search strategy using one or more of these indices. e.g., "keyword is less specific than MeSH."
            6 points - Names 1 or more field or index category but does not provide plausible defense of search strategy based on this knowledge. e.g., "I would do a keyword search..."
            3 points - Not applicable.
            0 points - No evident understanding that articles are "tagged" by different fields or indices.
        3. Delimiters
            8 points - Describes more than one approach to limiting search (e.g., "limit to human" or "adult" or "English"), names a specific publication type, or describes Clinical Queries in PubMed, the use of Boolean operators or search combinations, or includes terms related to an optimal study design (e.g., randomized), or suggests use of subheadings. Note: If the subject includes the name of the index when describing a delimiter (e.g., "check language as English"), then credit is given for both a tag and a method of delimiting.
            6 points - Describes only 1 common method of limiting search.
            3 points - Not applicable.
            0 points - No valid techniques for limiting a search listed.
            """,
        "user_prompt": "{medline}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 4,
        "rubric": """
        1. Search Terms
            8 points - 3 or more terms that reflect patient, intervention, comparison, and outcome (PICO) being considered.
            6 points - 2 terms from PICO.
            3 points - 1 term from PICO.
            0 points - Not present.
        2. Tags
            8 points - Description of search strategy reflects understanding that articles in the database are indexed by more than one field. Discusses one or more field/index/tag by name (e.g., MeSH, Title Word, Publication Title, language, Keyword, author, Journal title, etc.) and provides plausible rationale for search strategy using one or more of these indices. e.g., "keyword is less specific than MeSH."
            6 points - Names 1 or more field or index category but does not provide plausible defense of search strategy based on this knowledge. e.g., "I would do a keyword search..."
            3 points - Not applicable.
            0 points - No evident understanding that articles are "tagged" by different fields or indices.
        3. Delimiters
            8 points - Describes more than one approach to limiting search (e.g., "limit to human" or "adult" or "English"), names a specific publication type, or describes Clinical Queries in PubMed, the use of Boolean operators or search combinations, or includes terms related to an optimal study design (e.g., randomized), or suggests use of subheadings. Note: If the subject includes the name of the index when describing a delimiter (e.g., "check language as English"), then credit is given for both a tag and a method of delimiting.
            6 points - Describes only 1 common method of limiting search.
            3 points - Not applicable.
            0 points - No valid techniques for limiting a search listed.
        """,
        "allow_revisions": False,
        "allow_skip": True,
        "show_prompt": True,
        "read_only_prompt": False
    },
    "phase5": {
        "name": "Study Design",
        "fields": {
            "study_design": {
                "type": "text_area",
                "label": "Choose to focus on one of the clinical scenarios (breastfeeding and oral contraceptives, or bedwetting alarm). What type of study (study design) would best be able to address this question? Why? ",
                "value": "Focusing on the clinical scenario of breastfeeding and oral contraceptives, the best study design to address the question of how combination oral contraceptives (estrogen + progesterone) compare to progestin-only pills in terms of effects on breastmilk production would be a randomized controlled trial (RCT)"
            }
        },
        "phase_instructions": """The student has been asked "Choose to focus on one of the clinical scenarios (breastfeeding and oral contraceptives, or bedwetting alarm). What type of study (study design) would best be able to address this question? Why? ". The student will respond. Provide brief feedback for the student based on the scoring rubric here:
        1. Study Design
            12 points - Names one of the best sources: Randomized Controlled Trial or Randomized Trial, Systematic Review or Meta-Analysis of RCTs, Randomized, Double-Blinded Clinical Trial.
            9 points - Describes but does not call by name one of the best sources. e.g., "comparing two groups, one gets treatment, the other gets placebo…" or "avoid selection bias."
            6 points - Describes or names a less desirable study design. e.g., "Cohort study," "Prospective clinical trial," or "longitudinal."
            3 points - Describes or names a poor study design. e.g., "case-control," "cross-sectional study," or "case report."
            0 points - None of the above present.
        2. Justification
            12 points - Includes well-reasoned justification that reflects understanding of the importance of randomization and/or blinding. Explicitly connects randomization to reduction of confounding and/or blinding to observer or measurement bias. e.g., "An RCT will attempt to avoid any bias which would influence the outcome of the study through randomization" OR "best suited for therapy questions because it reduces bias and controls for confounding factors."
            9 points - Justification is present and touches on issues related to randomization and/or blinding, but is less clearly articulated. e.g., "groups should be similar" or "try to eliminate confounding factors."
            6 points - Justification is present and raises legitimate issues unrelated to randomization or blinding, such as cost-effectiveness, ethical concerns, or recall bias. May mention randomization or blinding but without explanation. e.g., "best in a random and blind setting."
            3 points - Attempted justification, but arguments are non-specific and do not demonstrate understanding of the relationship between the design and various threats to validity. May mention randomization or blinding but without explanation. e.g., "best in a random and blind setting."
            0 points - None of the above present.
            """,
        "user_prompt": "{study_design}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 4,
        "rubric": """
        1. Study Design
            12 points - Names one of the best sources: Randomized Controlled Trial or Randomized Trial, Systematic Review or Meta-Analysis of RCTs, Randomized, Double-Blinded Clinical Trial.
            9 points - Describes but does not call by name one of the best sources. e.g., "comparing two groups, one gets treatment, the other gets placebo…" or "avoid selection bias."
            6 points - Describes or names a less desirable study design. e.g., "Cohort study," "Prospective clinical trial," or "longitudinal."
            3 points - Describes or names a poor study design. e.g., "case-control," "cross-sectional study," or "case report."
            0 points - None of the above present.
        2. Justification
            12 points - Includes well-reasoned justification that reflects understanding of the importance of randomization and/or blinding. Explicitly connects randomization to reduction of confounding and/or blinding to observer or measurement bias. e.g., "An RCT will attempt to avoid any bias which would influence the outcome of the study through randomization" OR "best suited for therapy questions because it reduces bias and controls for confounding factors."
            9 points - Justification is present and touches on issues related to randomization and/or blinding, but is less clearly articulated. e.g., "groups should be similar" or "try to eliminate confounding factors."
            6 points - Justification is present and raises legitimate issues unrelated to randomization or blinding, such as cost-effectiveness, ethical concerns, or recall bias. May mention randomization or blinding but without explanation. e.g., "best in a random and blind setting."
            3 points - Attempted justification, but arguments are non-specific and do not demonstrate understanding of the relationship between the design and various threats to validity. May mention randomization or blinding but without explanation. e.g., "best in a random and blind setting."
            0 points - None of the above present.
        """,
        "allow_revisions": False,
        "allow_skip": True,
        "show_prompt": True,
        "read_only_prompt": False
    },
    "phase6": {
        "name": "Study Characteristics",
        "fields": {
            "relevance": {
                "type": "text_area",
                "label": "When you find a report of original research on these questions, what characteristics of the study will you consider to determine if it is relevant? Include examples. (Questions 6 and 7 will ask how to determine if the study is valid, and how important the findings are....for this question, focus on how to determine if it is really relevant to your practice.) ",
                "value": ""
            },
            "validity": {
                "type": "text_area",
                "label": "When you find a report of original research on these questions, what characteristics of the study will you consider to determine if its findings are valid? Include examples(You've already addressed relevance, and question 7 will ask how to determine the importance of the findings...for this question, focus on the validity of the study.) ",
                "value": ""
            },
            "significance": {
                "type": "text_area",
                "label": "When you find a report of original research on these questions, what characteristics of the findings will you consider to determine their magnitude and significance? Include examples. (You’ve already addressed relevance and validity…for this question, focus on how to determine the size and meaning of an effect reported in the study.) ",
                "value": ""
            },
        },
        "phase_instructions": """The student has been asked to define good characteristics of relevant, valid, and significant studies. The student will respond. Provide brief feedback for the student based on the scoring rubric here:
        1. Relevance of Question
            12 points - Well-reasoned and thoughtful discussion of the relevance of the independent and dependent variables used in the study, including examples/specific reasons. May refer to: the feasibility of the test or intervention (e.g., "the test might work but if my practice can’t afford to buy the machine, it doesn’t matter"); the patient or disease-oriented nature of the outcome (e.g., "did they measure dry nights after a week or after several months?" or "should measure infant growth, not just amount of milk produced"); the congruence between the operational definition and the research question (e.g., "whether their method of measuring the outcome is a realistic representation of the outcome we care about").
            9 points - Less thoughtful discussion of the relevance of the independent and dependent variables used in the study. May include specific concepts or examples without clear rationale. May refer to: the feasibility of the test or intervention (e.g., "is it feasible?" or "can I actually use it?"); the patient or disease-oriented nature of the outcome (e.g., "look for patient-oriented outcomes" or "does the outcome matter to my patient?"); the congruence between the operational definition and the research question (e.g., "did they measure what they set out to study?" or "what methods were used to determine lactation performance?").
            5 points - Response implies consideration of how well the study addresses the question at hand, but offers little discussion about why this may be important (e.g., "what are the variables?"; "does it answer my question?"; "the outcome measure"; "the purpose of the study"; "will it impact my practice?").
            0 points - No discussion of the research question and variables used to answer it.
        2. Description of Subjects
            12 points - Includes both: a clear expression of the importance of the link between the study subjects and target population, and at least one example of a relevant disease or demographic characteristic (e.g., "were the patients similar to mine in terms of age and race?" or "was it a hospital or clinic sample like my patients?" or "did patients have the same level of disease severity as my patient?" or "did selection or inappropriate inclusion criteria result in a study population that differs from mine by race, age, etc.").
            9 points - Includes one but not both: a clear expression of the importance of the link between the study subjects and target population, and at least one example of a relevant disease or demographic characteristic (e.g., "is the patient like mine?" or "education level of population").
            5 points - Response implies consideration of the study subjects, but offers no discussion of the connection between study subjects and target population or specific characteristics of the sample (e.g., "is it an appropriate sample?" or "what was the response or participation rate?" or "what were the exclusion criteria?" or "selection bias" or "setting" or "where study was conducted").
            0 points - No discussion of the characteristics of the research subjects.
        3. Validity
            24 points - Lists or describes at least 5 issues important to internal validity, such as: appropriateness of study design, adequacy of blinding, allocation concealment, randomization of group assignment, invalid or biased measurement ("followed own protocol?"), importance of comparison or control group, intention-to-treat analysis, consideration of appropriate covariates ("were other relevant factors considered?"), conclusions consistent with evidence ("do the results make sense?"), importance of follow-up of all study participants, appropriate statistical analysis, sample size/power, sponsorship, when the study was conducted, confirmation with other studies.
            18 points - Identifies 3-4 specific issues as above.
            10 points - Identifies 2 specific issues as above.
            5 points - Mentions internal validity or lists one specific concept from examples above.
            0 points - None of the above present.
        4. Magnitude
            12 points - Response must clearly discuss both: clinical significance (e.g., "what is the clinical significance?" or "how large a difference was found?") and example(s) of effect size measurements (e.g., specificity, sensitivity, likelihood ratio of a test, number needed to treat, relative risk, absolute risk reduction, mean difference for continuous outcomes, positive or negative predictive value).
            9 points - Response discusses one but not both: clinical significance (e.g., "what is the clinical significance?" or "how large a difference was found?") and example(s) of effect size measurements (e.g., specificity, sensitivity, likelihood ratio of a test, number needed to treat, relative risk, absolute risk reduction, mean difference for continuous outcomes, positive or negative predictive value).
            5 points - Response only suggests consideration of clinical significance or size of effect (e.g., "does it matter?" "will it impact my practice?").
            0 points - None of the above present.
        5. Statistical Significance
            12 points - Well-reasoned and thoughtful discussion of the indices of statistical significance, including at least 2 specific examples of important related concepts such as: p-values, confidence intervals, power, precision of estimates, Type 1 or Type 2 error.
            9 points - Lists more than one concept (as above) with insufficient or absent discussion (e.g., "p-value and confidence intervals") or lists and discusses only one concept (e.g., "p-value less than <.05").
            5 points - Mentions the need to assess statistical significance or names only one concept from above without further discussion (e.g., "p-values").
            0 points - None of the above present.
            """,
        "user_prompt": """{relevance}
        {validity}
        {significance}""",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 4,
        "rubric": """
        1. Relevance of Question
            12 points - Well-reasoned and thoughtful discussion of the relevance of the independent and dependent variables used in the study, including examples/specific reasons. May refer to: the feasibility of the test or intervention (e.g., "the test might work but if my practice can’t afford to buy the machine, it doesn’t matter"); the patient or disease-oriented nature of the outcome (e.g., "did they measure dry nights after a week or after several months?" or "should measure infant growth, not just amount of milk produced"); the congruence between the operational definition and the research question (e.g., "whether their method of measuring the outcome is a realistic representation of the outcome we care about").
            9 points - Less thoughtful discussion of the relevance of the independent and dependent variables used in the study. May include specific concepts or examples without clear rationale. May refer to: the feasibility of the test or intervention (e.g., "is it feasible?" or "can I actually use it?"); the patient or disease-oriented nature of the outcome (e.g., "look for patient-oriented outcomes" or "does the outcome matter to my patient?"); the congruence between the operational definition and the research question (e.g., "did they measure what they set out to study?" or "what methods were used to determine lactation performance?").
            5 points - Response implies consideration of how well the study addresses the question at hand, but offers little discussion about why this may be important (e.g., "what are the variables?"; "does it answer my question?"; "the outcome measure"; "the purpose of the study"; "will it impact my practice?").
            0 points - No discussion of the research question and variables used to answer it.
        2. Description of Subjects
            12 points - Includes both: a clear expression of the importance of the link between the study subjects and target population, and at least one example of a relevant disease or demographic characteristic (e.g., "were the patients similar to mine in terms of age and race?" or "was it a hospital or clinic sample like my patients?" or "did patients have the same level of disease severity as my patient?" or "did selection or inappropriate inclusion criteria result in a study population that differs from mine by race, age, etc.").
            9 points - Includes one but not both: a clear expression of the importance of the link between the study subjects and target population, and at least one example of a relevant disease or demographic characteristic (e.g., "is the patient like mine?" or "education level of population").
            5 points - Response implies consideration of the study subjects, but offers no discussion of the connection between study subjects and target population or specific characteristics of the sample (e.g., "is it an appropriate sample?" or "what was the response or participation rate?" or "what were the exclusion criteria?" or "selection bias" or "setting" or "where study was conducted").
            0 points - No discussion of the characteristics of the research subjects.
        3. Validity
            24 points - Lists or describes at least 5 issues important to internal validity, such as: appropriateness of study design, adequacy of blinding, allocation concealment, randomization of group assignment, invalid or biased measurement ("followed own protocol?"), importance of comparison or control group, intention-to-treat analysis, consideration of appropriate covariates ("were other relevant factors considered?"), conclusions consistent with evidence ("do the results make sense?"), importance of follow-up of all study participants, appropriate statistical analysis, sample size/power, sponsorship, when the study was conducted, confirmation with other studies.
            18 points - Identifies 3-4 specific issues as above.
            10 points - Identifies 2 specific issues as above.
            5 points - Mentions internal validity or lists one specific concept from examples above.
            0 points - None of the above present.
        4. Magnitude
            12 points - Response must clearly discuss both: clinical significance (e.g., "what is the clinical significance?" or "how large a difference was found?") and example(s) of effect size measurements (e.g., specificity, sensitivity, likelihood ratio of a test, number needed to treat, relative risk, absolute risk reduction, mean difference for continuous outcomes, positive or negative predictive value).
            9 points - Response discusses one but not both: clinical significance (e.g., "what is the clinical significance?" or "how large a difference was found?") and example(s) of effect size measurements (e.g., specificity, sensitivity, likelihood ratio of a test, number needed to treat, relative risk, absolute risk reduction, mean difference for continuous outcomes, positive or negative predictive value).
            5 points - Response only suggests consideration of clinical significance or size of effect (e.g., "does it matter?" "will it impact my practice?").
            0 points - None of the above present.
        5. Statistical Significance
            12 points - Well-reasoned and thoughtful discussion of the indices of statistical significance, including at least 2 specific examples of important related concepts such as: p-values, confidence intervals, power, precision of estimates, Type 1 or Type 2 error.
            9 points - Lists more than one concept (as above) with insufficient or absent discussion (e.g., "p-value and confidence intervals") or lists and discusses only one concept (e.g., "p-value less than <.05").
            5 points - Mentions the need to assess statistical significance or names only one concept from above without further discussion (e.g., "p-values").
            0 points - None of the above present.
        """,
        "allow_revisions": False,
        "allow_skip": True,
        "show_prompt": True,
        "read_only_prompt": False
    },
}

PREFERRED_LLM = "gpt-4-turbo"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Fresno Rubric",
    "page_icon": "️#️⃣",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())