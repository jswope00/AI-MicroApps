PHASES = {
    "phase1": {
        "name": "What is your name?",
        "fields": {
            "name": {
                "type": "text_input",
                "label": "What is your first name?",
            },
            "activity": {
            	"type": "text_input",
            	"label": "What is one of your favorite activities?"
            }
        },
        "user_prompt": "My name is {name} and I like {activity}. Write a haiku about me and my activity.",
    },
}

SIDEBAR_HIDDEN = False

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())