APP_URL = "https://student-interview.streamlit.app"
APP_IMAGE = "ai_debate.png"
PUBLISHED = True

APP_TITLE = "AI Debate Partner"
APP_INTRO = """
In this interactive exercise, you will participate in a structured debate with an AI, which challenges your reasoning and enhances your argumentative skills across various topics. After choosing a topic and a position to take, you'll engage in three rounds of debate, responding to the AI's prompts and refining your arguments. The exercise concludes with a summary from the AI, highlighting key points and providing feedback on your strengths and areas for improvement. Get ready to critically engage and articulate your thoughts in this casual virtual debate setting.
"""

APP_HOW_IT_WORKS = """
 **AI Debate Partner** is an interactive tool that facilitates structured debates between a student and an AI. Utilizing the OpenAI Assistants API with GPT-4, this tool is designed to simulate a real debate environment, allowing students to practice and refine their argumentative skills. Here’s how it works:

1. **Initiate the Debate:** Students can choose a topic they are interested in and input their initial stance on the issue. This kicks off the debate.
2. **Engage in Structured Rounds:** The AI begins the debate with a well-formed argument, setting the tone for a structured exchange. Students respond, and the AI analyzes these responses to present counterarguments. This cycle continues for three rounds, ensuring a comprehensive debate on the topic.
3. **Summary and Feedback:** After the debate rounds, the AI summarizes the discussion, highlighting key points and commendations for the student’s arguments. This helps students understand the strengths of their arguments and areas for improvement.

The tool is built to be an educational aid, encouraging students to think critically and articulate their thoughts clearly. It simulates a learning environment where students can freely experiment with ideas and receive immediate, constructive feedback.

Key Features and Considerations:

- **Feedback and Learning:** The AI provides ongoing feedback throughout the debate, helping students to refine their arguments and consider new perspectives.
- **Experimental Scoring:** While there is no numerical scoring, the AI’s feedback acts as a qualitative assessment of the student’s performance, focusing on the depth and relevance of their arguments rather than on a point system.
- **AI Limitations:** As with any AI-driven tool, the responses are generated based on patterns in data and may not always perfectly align with human reasoning. Students are encouraged to use critical thinking to assess the AI’s feedback and consider its relevance to their arguments.
- **Educational Focus:** The primary aim is to enhance educational experiences, not to replace traditional learning methods. The tool serves as a complement to classroom learning, providing a safe space for students to practice and improve their debate skills.
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
}

SYSTEM_PROMPT = """You are a debate partner for a university-level student taking a course about the debate topic. You will take a side of your choosing or provided by the student on a topic. You will present your arguments convincingly and with evidence. You also recognize clear and evidence-based arguments put forward by the student. """

PHASES = {
    "welcome": {
        "name": "Welcome to the Debate Portal",
        "fields": {
            "intro": {
                "type": "markdown",
                "body": """<h2>Welcome to the Debate Portal! </h2> <p>You'll start by providing your name and a topic you'd like to debate.</p>""",
                "unsafe_allow_html": True,
            }

        },
        "ai_response": False,
        "no_submission": True,
        "scored_phase": False,
        "allow_revisions": False,
        "allow_skip": True,
        #"show_prompt": True,
        #"read_only_prompt": False
    },
    "name": {
        "name": "Your Name",
        "fields": {
            "name": {
                "type": "text_input",
                "label": """What is your first name?""",
                "value": "",
            }
        },
        "phase_instructions": "The user will provide you their name. In one sentence only, welcome them by name and end your statement with 'Let's try a friendly debate in order to increase your understanding and fluency in the topic.'",
        "user_prompt": "My name is {name}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 2,
        "rubric": """
                1. Name
                    2 points - The user has provided you with a valid first name (e.g. Mike, John, Susan)
                    0 points - The user has provided an invalid name (e.g. Macaroni, Huh?, West Coast)
        """,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "round1": {
        "name": "Round 1: Choose a Topic",
        "fields": {
            "topic": {
                "type": "selectbox",
                "label": "Choose a debate topic (Round 1)",
                #"type": "text_input",
                "options": ['Telemedicine: I believe that the rise in telemedicine will improve health outcomes.', 'Telemedicine: I believe that the rise in telemedicine will harm health outcomes.', 'Wearables: I believe the benefits of wearable health technologies outweigh the risk of data breaches', 'Wearables: I believe the risk of data breaches outweigh the benefits of wearable health technologies.', 'Health Data Ownership: I believe that patients should have autonomy and privacy over their personal information.', 'Health Data Ownership: I believe that health information can be shared in order to improve individual and public health outcomes.'],
                #"options": ['Countries should try as much as possible to balance their budgets and avoid debt', 'Countries should prioritize growth over balanced budgets'],
                #"options": ['Horses are better', 'Ponies are better']
            }
        },
        "phase_instructions": "The user will provide you a topic and their stance on the topic. Take the opposite stance, and generate an introductory statement for the debate. Ensure your statement is clear, evidence-based, and structured to provoke thoughtful discourse. End your statement with 'Why did you choose the stance you chose?'",
        "user_prompt": "{topic}",
        "ai_response": True,
        "no_submission": False,
        "scored_phase": False,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "round2": {
        "name": "Round 2: Outline Your Position",
        "fields": {
            "position": {
                "type": "text_area",
                "height": 300,
                "label": """Outline Your Position (Round 2)""",
                "value": """The rise in telemedicine is poised to significantly improve health outcomes for several reasons. First, it greatly increases accessibility to healthcare, especially for individuals in remote or underserved areas who might otherwise face significant barriers to accessing medical services. By enabling patients to consult with doctors via video or phone, telemedicine reduces travel time and associated costs, making it easier for patients to seek care promptly. Secondly, telemedicine supports the continuous monitoring of chronic conditions, allowing for timely adjustments in treatment and preventing complications. This proactive approach can lead to better overall management of chronic diseases and improved long-term health outcomes. Additionally, telemedicine can alleviate the strain on overburdened healthcare facilities by handling routine consultations online, thus improving the quality and speed of both virtual and in-person care services. Overall, the integration of telemedicine into healthcare systems promises a more accessible, efficient, and patient-centered approach to medical care, leading to enhanced health outcomes.""",
            }
        },
        "phase_instructions": "The user will respond to your opening statement. Respond to the student's argument by addressing their points and introducing new evidence or perspectives on the topic. Aim to challenge the student's stance constructively.",
        "user_prompt": "{position}",
        "ai_response": True,
        "no_submission": False,
        "scored_phase": False,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    },
    "round3": {
        "name": "Round 3: Respond and Defend your Position",
        "fields": {
            "position": {
                "type": "text_area",
                "height": 300,
                "label": """Respond and Defend your Position (Round 3)""",
                "value": """Addressing the challenges presented by the rise of telemedicine requires a multifaceted approach to ensure that its benefits are maximized without exacerbating disparities or compromising care quality:

Enhance Digital Literacy: Implementing educational programs tailored for elderly patients and those unfamiliar with technology can help bridge the technology gap. Healthcare providers can partner with community centers and libraries to offer training sessions on using telehealth platforms effectively.
Improve Technology Access: Governments and healthcare organizations should work together to provide subsidized or free devices and internet services to low-income or technologically underserved populations. This can help ensure that everyone has the necessary tools to benefit from telemedicine.
Hybrid Models of Care: Develop models of care that combine telemedicine with traditional in-person visits. For example, routine follow-ups and monitoring could be conducted virtually, while ensuring easy and quick access to in-person care when a physical examination is necessary.
Standardize Telemedicine Practices: Establish clear guidelines and standards for telemedicine practices to ensure consistent quality across services. This includes protocols for when to refer patients for in-person care and how to conduct thorough virtual assessments.
Incorporate Remote Monitoring Tools: Utilize advanced remote monitoring technologies that can provide more comprehensive data to healthcare providers. Devices that measure vital signs, blood sugar levels, and other important health metrics can provide data that enhances the quality of virtual consultations.
Regular Quality Assessments and Feedback Mechanisms: Regularly assess the quality of telemedicine services and gather patient feedback to continuously improve the system. This can help identify areas where telemedicine is failing and areas where it excels, allowing for targeted improvements.
By tackling these challenges through strategic initiatives and policies, the potential of telemedicine to enhance healthcare accessibility and effectiveness can be fully realized without sacrificing the quality of care.""",
            }
        },
        "phase_instructions": "Summarize the key points of the debate, highlighting the student's strong arguments and commend them for their insights. Conclude the debate by reiterating the importance of discussing such topics.",
        "user_prompt": "{position}",
        "ai_response": True,
        "scored_phase": False,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": False,
        "show_prompt": False,
        "read_only_prompt": False
    }

}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Debate",
    "page_icon": "🗣️️",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
