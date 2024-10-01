APP_TITLE = "Case Study: Promoting The Grand Horizon Boutique Hotel in Fairview City"
APP_INTRO = """This is a simple app that assesses the user's understanding of a simple case study. It is for demonstrating the capabilities of a AI MicroApp. 
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

Promoting The Grand Horizon Boutique Hotel in Fairview City
Introduction
In the heart of Fairview City, a medium-sized urban center known for its historic charm and burgeoning cultural scene, Sarah Reynolds faced a critical decision. As the newly appointed Director of Marketing for The Grand Horizon Boutique Hotel, a recently established luxury accommodation nestled within the city’s vibrant downtown district, Sarah was tasked with spearheading a marketing campaign that would position the hotel as the premier choice for discerning travelers. Despite the hotel’s prime location and lavish amenities, the challenge lay in differentiating The Grand Horizon in a market saturated with well-established competitors and attracting a steady stream of guests outside the peak tourist seasons.

Fairview City, though not a major metropolis, had witnessed steady growth over the past decade, drawing a mix of business travelers, weekend tourists, and culture enthusiasts. The city’s economy thrived on its blend of industries, including technology, education, and a burgeoning arts scene. The Grand Horizon, a meticulously renovated historic building, was designed to cater to this diverse audience with its blend of modern luxury and historic charm. However, in a market where large chain hotels dominated, Sarah needed to craft a compelling marketing strategy that would not only highlight the hotel’s unique selling points but also ensure sustained occupancy rates throughout the year.

Background
The Grand Horizon Boutique Hotel was the brainchild of James and Emily Harper, a couple with a deep love for Fairview City and a vision of creating a hotel that reflected the city’s spirit. After acquiring a historic but dilapidated building in the heart of the city, they invested heavily in its renovation, blending modern comforts with the building’s original architectural elements. The result was a 50-room boutique hotel that offered an intimate and luxurious experience, with each room uniquely designed to reflect different aspects of Fairview City’s history and culture.

Despite the hotel’s initial buzz during its grand opening, the Harpers quickly realized that maintaining high occupancy rates was going to be more challenging than anticipated. Fairview City’s tourism was highly seasonal, with a significant dip in visitors during the off-peak months. Furthermore, the hotel faced stiff competition from larger, more established hotels that were part of national and international chains, which had the advantage of brand recognition, loyalty programs, and extensive marketing budgets.

To tackle these challenges, the Harpers brought in Sarah Reynolds, a seasoned marketing professional with experience in the hospitality industry. Sarah’s mission was clear: to develop and implement a marketing strategy that would not only boost The Grand Horizon’s visibility but also attract a steady flow of guests throughout the year, especially during the off-peak season.

The Marketing Challenge
Sarah’s first step was to conduct a comprehensive analysis of the hotel’s current marketing efforts, the competitive landscape, and the target market. She quickly identified several key challenges that needed to be addressed:

Brand Recognition: Unlike the well-known chain hotels, The Grand Horizon lacked brand recognition. Many potential guests, particularly business travelers who relied on corporate loyalty programs, were unaware of the hotel’s existence.

Seasonal Demand: Fairview City’s tourism was heavily influenced by its seasonal events, such as the annual Arts Festival and the Winter Holiday Market. Outside these events, visitor numbers dropped significantly, leading to low occupancy rates during these periods.

Target Audience: The hotel’s target market was diverse, ranging from business travelers to tourists and locals seeking a staycation. Sarah needed to craft a marketing strategy that resonated with each of these segments while maintaining a consistent brand message.

Budget Constraints: Although the Harpers had invested heavily in the hotel’s renovation, the marketing budget was relatively modest compared to the larger chains. This meant that Sarah had to be strategic in her spending, focusing on high-impact initiatives that would yield the best return on investment.

Strategic Differentiation
Given these challenges, Sarah knew that simply advertising the hotel’s luxury and location would not be enough. The Grand Horizon needed to differentiate itself in a way that would resonate deeply with its target audience. After several brainstorming sessions and consultations with the Harpers, Sarah decided to focus on three key areas:

Local Partnerships: Sarah believed that partnering with local businesses and cultural institutions could help The Grand Horizon stand out as a hotel deeply connected to the community. She initiated collaborations with nearby restaurants, offering exclusive dining packages for hotel guests. Additionally, the hotel partnered with the Fairview Arts Council to host monthly art exhibitions in the hotel’s lobby, showcasing works from local artists. These initiatives not only provided added value to guests but also strengthened the hotel’s ties with the local community, making it an integral part of the Fairview experience.

Personalized Guest Experiences: Recognizing that boutique hotels thrive on offering unique, personalized experiences, Sarah introduced several initiatives aimed at enhancing guest satisfaction. Each guest received a personalized welcome note upon arrival, along with a guidebook highlighting lesser-known attractions in Fairview City. The hotel also offered bespoke city tours, tailored to individual interests, whether that be exploring the city’s historic sites, discovering its culinary scene, or enjoying its natural beauty.

Digital Marketing and Social Media: With a limited budget, Sarah knew that digital marketing would be crucial in reaching a wider audience. She revamped the hotel’s website, ensuring it was optimized for search engines and mobile-friendly. Sarah also launched a targeted social media campaign, using visually appealing content to showcase the hotel’s unique features and highlight guest experiences. Influencer partnerships and user-generated content played a significant role in building the hotel’s online presence, particularly on platforms like Instagram and Facebook.

Growth and Future Prospects
The implementation of these strategies began to show positive results within the first few months. Occupancy rates during the off-peak season increased by 15%, and the hotel saw a 25% growth in direct bookings through its website. The collaboration with local businesses and cultural institutions not only enhanced the guest experience but also generated word-of-mouth referrals, further boosting the hotel’s reputation.

Encouraged by these results, Sarah and the Harpers started to explore additional growth opportunities. Plans were made to introduce a loyalty program aimed at encouraging repeat visits, particularly among business travelers. Additionally, Sarah proposed hosting seasonal events at the hotel, such as wine tastings and themed dinners, to attract local residents and visitors alike during slower periods.

However, challenges remained. The hotel’s small size meant that it would always be at a disadvantage compared to the larger chains in terms of economies of scale and marketing reach. Sarah also recognized that maintaining the personalized touch that had become The Grand Horizon’s hallmark would become increasingly difficult as the hotel grew in popularity.

Organizational Structure and Bottlenecks
As The Grand Horizon continued to grow, the hotel’s organizational structure began to show signs of strain. With Sarah overseeing all marketing efforts, including digital campaigns, partnerships, and guest experience initiatives, her role became increasingly demanding. The hotel’s limited staff meant that many employees were stretched thin, juggling multiple responsibilities to maintain the high standards of service that guests had come to expect.

The Harpers, while passionate and involved in the day-to-day operations, found themselves overwhelmed by the administrative and managerial tasks required to run the hotel. This centralization of responsibilities led to bottlenecks in decision-making, particularly in areas like marketing approvals, budget allocations, and event planning.

To address these challenges, Sarah proposed a restructuring of the hotel’s operations. This included hiring additional staff to support the marketing and guest services teams, as well as delegating more responsibilities to department heads to streamline decision-making processes. The Harpers, while initially hesitant, recognized the need for these changes to sustain the hotel’s growth and maintain its competitive edge.

Conclusion and Dilemma
As The Grand Horizon Boutique Hotel solidified its position in the Fairview City market, Sarah and the Harpers found themselves at a crossroads. The marketing strategies implemented had successfully increased occupancy rates and enhanced the hotel’s reputation, but sustaining this momentum required careful planning and resource allocation. The hotel’s future growth would depend on its ability to scale its operations while maintaining the personalized, high-quality experience that had become its signature.

The key questions facing Sarah and the Harpers were clear: How could they continue to differentiate The Grand Horizon in a competitive market without overextending their resources? Could they maintain the hotel’s unique charm and personalized service as they expanded? And, perhaps most importantly, how could they ensure that the hotel’s growth did not compromise the values and vision that had made it successful in the first place?

These questions remained at the forefront as Sarah and the Harpers planned their next steps, knowing that the decisions they made would shape the future of The Grand Horizon and its place in Fairview City’s hospitality landscape."""

PHASES = {
    "about": {
        "name": "About the Case Study",
        "fields": {
            "about": {
                "type": "text_area",
                "height": 200,
                "label": """What is this case study about?""",
                "value": "This case study explores the marketing challenges and strategies of The Grand Horizon Boutique Hotel, a new luxury hotel in Fairview City, as it seeks to differentiate itself in a competitive market. It details the efforts made by Sarah Reynolds, the Director of Marketing, to boost brand recognition, attract guests year-round, and maintain high service standards. The study also examines the organizational challenges faced by the hotel as it grows and the decisions needed to sustain its success.",
            }
        },
        "phase_instructions": """I will summarize the case study. Please critically review my response for accuracy and effort. You are looking for some combination of the facts that the case study is about a hotel, and the hotel needs to differentiate itself in order to grow, and that growth presents challenges that need to be overcome.
        """,
        "user_prompt": "{about}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 2,
        "rubric": """
            1. Hotel
                1 point - I mention the case study is about a hotel. 
                0 points - I do not mention that the case study is about a hotel. 
            2. Growth
                1 point - I speak to the growth challenge of standing out as a new hotel. 
                0 points - I do not speak to the growth challenge of standing out as a new hotel. 
            3. Scaling
                1 point - I speak to the challenges of running a busy hotel in a way that does not compromise the values and vision. 
                0 points - I do not speak to the challenges of running a busy hotel in a way that does not compromise the values and vision. 
                
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
                "label": "Identify two specific risks that can arise from scaling a boutique hotel, and how each risk might be mitigated.",
                "value":"""Scaling a boutique hotel like The Grand Horizon can lead to the risks of losing personalized guest experiences and facing operational inefficiencies. To mitigate these risks, the hotel should invest in customer relationship management systems and staff training to maintain personalized service, while also implementing advanced property management systems and hiring experienced operational managers to handle increased complexity efficiently. These steps will help preserve the hotel’s unique charm and ensure smooth operations as it grows."""
            }
        },
        "phase_instructions": """I will offer two specific risks that can arise from scaling a boutique hotel, and how each risk might be mitigated. Provide me feedback based on:
        1. I provide two risks (not less)
        2. My risks are specific and grounded in the case study. 
        3. I provide realistic mitigation strategies for each
        As the expert, you would speak to the challenge of reputation damage for a small hotel with only one location, mitigated by prompting customers for feedback before they get to the internet. You might also speak to employee burnout mitigated by good training and flexible scheduling. But don't penalize me for answers that are different from yours. 
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
                1 points - Only one risk is specific and grounded in the case study. 
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
                "label": "What strategies should Sarah and the Harpers prioritize to scale the hotel’s operations without diluting the personalized guest experience that distinguishes The Grand Horizon? How can they allocate limited resources effectively to sustain growth?",
                "value":"""Sarah and the Harpers should prioritize implementing scalable personalization strategies, such as investing in a robust customer relationship management (CRM) system to track guest preferences and automate personalized services. They should also focus on staff training and hiring additional personnel dedicated to guest relations to ensure the high-touch service remains consistent as the hotel grows. To allocate limited resources effectively, they should invest in technology that streamlines operations, such as an integrated property management system, while leveraging partnerships with local businesses to enhance guest experiences without overextending the hotel’s internal resources. This approach will help maintain the hotel’s distinctive charm while supporting sustainable growth.""",
            }
        },
        "phase_instructions": """I will offer suggestions on how Sarah and the Harpers can prioritize to scale the hotel’s operations without diluting the personalized guest experience that distinguishes The Grand Horizon. Review my answers based on the following criteria: 
        1. I reference the case study
        2. My arguments make sense. 
        3. My arguments are realistic. 
        As the expert, you would speak to hiring and onboarding the right people as being critical to maintaining a culture of personalization as we scale. But don't penalize me for answers that are different from yours.
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
