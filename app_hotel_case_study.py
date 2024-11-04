APP_URL = "https://hotel-case-study.streamlit.app"
PUBLISHED=True
APP_IMAGE = "hotel_case_study_flat.webp"

APP_TITLE = "Hotel Case Study"

APP_INTRO = """Promoting The Grand Horizon Boutique Hotel in Fairview City
This is a simple app that assesses the user's understanding of a simple case study. It is for demonstrating the capabilities of a AI MicroApp. 
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
 """

SHARED_ASSET = {
}

HTML_BUTTON = {
    "url": "https://ai-microapps.s3.amazonaws.com/Grand_Horizon_Case_Study.pdf",
    "button_text":"Review Case Study"
}

SYSTEM_PROMPT = """You provide feedback to me as I answer specific questions about the following case study. 
You provide feedback as a business school faculty who wants me to engage critically with the case study. 
You encourage me to be thorough with my answers. 
You applaud me for good answers, but you also try to critically find suggestions for areas of improvement based on the prompts you get and the answers I submit. 
Here is the case study: 

Enhancing Logistics at The Grand Horizon Boutique Hotel in Fairview City

Introduction
In the heart of Fairview City, a medium-sized urban center known for its historic charm and burgeoning cultural scene, Mark Lee faced a critical decision. As the newly appointed Director of Logistics for The Grand Horizon Boutique Hotel, a recently established luxury accommodation nestled within the city’s vibrant downtown district, Mark was tasked with optimizing the hotel’s logistics operations to ensure efficient management of resources and sustainability. Despite the hotel’s prime location and high standards, the challenge lay in streamlining logistical processes in a market with fluctuating demand and maintaining operational excellence at all times.

Fairview City, though not a major metropolis, had witnessed steady growth over the past decade, drawing a mix of business travelers, weekend tourists, and culture enthusiasts. The city’s economy thrived on its blend of industries, including technology, education, and a growing arts scene. The Grand Horizon, a meticulously renovated historic building, was designed to cater to this diverse audience with its blend of modern luxury and historic charm. However, operational inefficiencies and sustainability concerns loomed as the hotel sought to differentiate itself from larger chains through superior logistical management.

Background
The Grand Horizon Boutique Hotel was the brainchild of James and Emily Harper, a couple with a deep love for Fairview City and a vision of creating a hotel that reflected the city’s spirit. After acquiring a historic but dilapidated building in the heart of the city, they invested heavily in its renovation, blending modern comforts with the building’s original architectural elements. The result was a 50-room boutique hotel that offered an intimate and luxurious experience, with each room uniquely designed to reflect different aspects of Fairview City’s history and culture.

Despite the initial buzz during its grand opening, the Harpers quickly realized that achieving operational efficiency would be more challenging than anticipated. Fairview City’s tourism was highly seasonal, with a significant dip in visitors during the off-peak months. Furthermore, the hotel faced competition from larger, more established chains that had robust logistics frameworks, allowing for economies of scale in their operations.

To tackle these challenges, the Harpers brought in Mark Lee, an experienced logistics professional with a background in the hospitality industry. Mark’s mission was clear: to develop and implement logistics strategies that would not only streamline operations but also ensure sustainable practices were in place to support the hotel’s long-term growth.

The Logistics Challenge
Mark’s first step was to conduct a comprehensive analysis of the hotel’s current logistical efforts, the competitive landscape, and the operational requirements. He quickly identified several key challenges that needed to be addressed:

Operational Efficiency: Unlike larger, more established hotel chains, The Grand Horizon lacked a sophisticated logistics system. This often led to inefficiencies in supply management and service delivery, ultimately affecting guest experience.

Seasonal Demand Fluctuations: Fairview City’s tourism was heavily influenced by its seasonal events, such as the annual Arts Festival and the Winter Holiday Market. Outside these events, logistical support had to adapt to varying demands to ensure cost-effectiveness and resource optimization.

Sustainable Practices: The hotel’s commitment to environmental responsibility required a shift towards sustainable logistics practices. Mark needed to identify strategies that would both reduce environmental impact and enhance operational efficiency.

Budget Constraints: Although the Harpers had invested heavily in the hotel’s renovation, the logistics budget was relatively modest compared to the larger chains. This meant that Mark had to be strategic in implementing cost-effective logistics solutions that would yield the best return on investment.

Strategic Optimization
Given these challenges, Mark knew that simply adopting standard operational practices would not be enough. The Grand Horizon needed to optimize its logistics framework in a way that would resonate with its commitment to sustainability and efficiency. After several brainstorming sessions and consultations with the Harpers, Mark decided to focus on three key areas:

Supply Chain Diversification: Mark believed that diversifying suppliers and developing contingency plans could help mitigate potential disruptions. He initiated partnerships with local vendors to build a resilient supply network and introduced technology for real-time supply monitoring to enhance responsiveness.

Process Automation: Recognizing that technological advancements could greatly improve efficiency, Mark introduced several initiatives aimed at automating logistical processes. This included implementing a property management system with capabilities for automated inventory tracking and demand forecasting, ensuring smooth operations regardless of seasonal changes.

Green Logistics Initiatives: With a focus on sustainability, Mark revamped the hotel’s logistics operations to minimize environmental impact. This involved optimizing transportation routes, using eco-friendly materials, and engaging in waste reduction practices, which together supported the hotel’s green objectives without compromising on service quality.

Growth and Future Prospects
The implementation of these strategies began to show positive results within the first few months. Supply chain efficiencies improved, leading to reduced operational costs, and the hotel achieved a 20% reduction in waste. Collaborations with local vendors not only bolstered the hotel’s sustainability efforts but also enhanced its community ties.

Encouraged by these results, Mark and the Harpers started to explore additional growth opportunities. Plans were made to implement predictive analytics for better demand forecasting and resource planning. Additionally, Mark proposed expanding the green initiatives to include a certification program, enhancing the hotel’s reputation for sustainable practices.

However, challenges remained. The hotel’s small size meant that it would always be at a disadvantage compared to the larger chains in terms of scale and logistics reach. Mark also recognized that maintaining the operational excellence and sustainability focus that had become The Grand Horizon’s hallmark would become increasingly complex as the hotel grew in popularity.

Organizational Structure and Bottlenecks
As The Grand Horizon continued to grow, the hotel’s organizational structure began to show signs of strain. With Mark overseeing all logistics efforts, including supply chain management, process automation, and sustainability initiatives, his role became increasingly demanding. The hotel’s limited staff meant that many employees were stretched thin, juggling multiple responsibilities to maintain the high standards the hotel was known for.

The Harpers, while passionate and involved in the day-to-day operations, found themselves overwhelmed by the administrative and managerial tasks required to run the hotel. This centralization of responsibilities led to bottlenecks in decision-making, particularly in areas like budget approvals and logistics planning.

To address these challenges, Mark proposed a restructuring of the hotel’s operations. This included hiring additional staff to support the logistics and guest services teams, as well as delegating more responsibilities to department heads to streamline decision-making processes. The Harpers, while initially hesitant, recognized the need for these changes to sustain the hotel’s growth and maintain its competitive edge.

Conclusion and Dilemma
As The Grand Horizon Boutique Hotel solidified its position in the Fairview City market, Mark and the Harpers found themselves at a crossroads. The logistics strategies implemented had successfully streamlined operations and enhanced sustainability, but sustaining this momentum required careful planning and resource allocation. The hotel’s future growth would depend on its ability to scale logistics operations while maintaining the high-quality service and sustainable practices that had become its signature.

The key questions facing Mark and the Harpers were clear: How could they continue to differentiate The Grand Horizon with superior logistics in a competitive market without overextending their resources? Could they maintain the hotel’s unique charm and operational excellence as they expanded? And, perhaps most importantly, how could they ensure that the hotel’s growth did not compromise the values and vision that had made it successful in the first place?

These questions remained at the forefront as Mark and the Harpers planned their next steps, knowing that the decisions they made would shape the future of The Grand Horizon and its place in Fairview City’s hospitality landscape."""

PHASES = {
    "about": {
        "name": "About the Case Study",
        "fields": {
            "about": {
                "type": "text_area",
                "height": 200,
                "label": """What is this case study about?""",
                "value": "This case study explores the logistical challenges and solutions faced by The Grand Horizon Boutique Hotel as it scales its operations in Fairview City. It covers the initiatives led by Mark Lee, the Director of Logistics, to improve supply chain efficiency, optimize inventory management, and implement sustainable practices. The study also examines the operational hurdles encountered and the strategic steps taken to ensure long-term success.",
            }
        },
        "phase_instructions": """I will summarize the case study. Please critically review my response for accuracy and effort. You are looking for some combination of the facts that the case study addresses logistics challenges within a hotel, emphasizing the need to enhance supply chain efficiency and sustainability as the organization grows.
        """,
        "user_prompt": "{about}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 2,
        "rubric": """
            1. Logistics
                1 point - I mention the case study focuses on logistics. 
                0 points - I do not mention that the case study focuses on logistics. 
            2. Efficiency Improvement
                1 point - I address the challenge of improving supply chain efficiency. 
                0 points - I do not address the challenge of improving supply chain efficiency. 
            3. Sustainability
                1 point - I speak to the need for implementing sustainable logistics practices. 
                0 points - I do not speak to the need for implementing sustainable logistics practices. 
                
        """,
        "allow_revisions": False,
        "allow_skip": True,
    },
    "risk": {
        "name": "Identify Specific Risks",
        "fields": {
            "risk": {
                "type": "text_area",
                "height": 300,
                "label": "Identify two specific risks arising from scaling logistics operations at a boutique hotel, and how each risk might be mitigated.",
                "value":"""Scaling logistics operations at The Grand Horizon can lead to risks such as supply chain disruptions and increased carbon footprint. To mitigate these risks, the hotel should establish multiple sourcing options and develop contingency plans for potential disruptions, while also adopting greener practices like optimizing transportation routes and using eco-friendly packaging materials to reduce environmental impact. These measures will help maintain a resilient and sustainable logistics framework as the hotel expands."""
            }
        },
        "phase_instructions": """I will offer two specific risks that can arise from scaling logistics operations, and how each risk might be mitigated. Provide me feedback based on:
        1. I provide two risks (not less)
        2. My risks are specific and grounded in the case study. 
        3. I provide realistic mitigation strategies for each
        As the expert, you might speak to inventory mismanagement risks, mitigated by adopting real-time tracking systems, and risks of regulatory compliance, mitigated by standardized procedures and staff training. But don't penalize me for answers that are different from yours.
        """,
        "user_prompt": "{risk}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 4,
        "rubric": """
            1. Risks
                2 points - I offered two risks (not less)
                1 point - I offered only one risk
                0 points - I did not offer any risks
            2. Specific and Grounded
                2 points - Both risks are specific and grounded in the case study. 
                1 point - Only one risk is specific and grounded in the case study. 
                0 points - No risks are specific and grounded in the case study. 
            3. Mitigation
                2 points - I offer two reasonable mitigation strategies that address the risks. 
                1 point - I offer only one reasonable mitigation strategy that addresses the risks.
                0 points - I do not offer any reasonable mitigation strategies that address the risks. 
        """,
        "allow_skip": True,
    },
    "scale": {
        "name": "Scale Without Dilution",
        "fields": {
            "scale": {
                "type": "text_area",
                "height": 300,
                "label": "What strategies should Mark and the management prioritize to scale the hotel’s logistics operations without compromising efficiency and sustainability? How can they allocate resources effectively to support growth?",
                "value":"""Mark and the management should prioritize implementing scalable logistics solutions such as leveraging technology for real-time supply chain tracking and adopting sustainable practices like eco-friendly materials. They should also focus on process automation to streamline logistics operations and reduce manual errors. To allocate resources effectively, they should invest in technology that enhances data analysis for demand forecasting and partner with sustainable suppliers to ensure resource efficiency. This approach will help maintain operational excellence while supporting the hotel's sustainable growth objectives.""",
            }
        },
        "phase_instructions": """I will offer suggestions on how Mark and the management can prioritize scaling the hotel’s logistics operations without compromising efficiency and sustainability. Review my answers based on the following criteria: 
        1. I reference the case study
        2. My arguments make sense. 
        3. My arguments are realistic. 
        As the expert, you might emphasize the importance of implementing technologies for predictive analytics in logistics. But don't penalize me for answers that are different from yours.
        """,
        "user_prompt": "{scale}",
        "ai_response": True,
        "scored_phase": False,
        "allow_revisions": False,
        "max_revisions": 2,
        "allow_skip": True,
    }
}

PREFERRED_LLM = "gpt-4o"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Hotel Case Study",
    "page_icon": "️🏨",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())