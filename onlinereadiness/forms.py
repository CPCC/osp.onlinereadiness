from django import forms
from django.utils import simplejson as json


class OnlineReadinessForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(OnlineReadinessForm, self).__init__(*args, **kwargs)
        
        questions = ["I am capable of learning new technologies.",
        "I am capable of sending and receiving e-mail.",
        "I am capable of attaching files to an e-mail message.",
        "I am a competent Internet browser.",
        "I am capable of using standard word processing software.",
        "I am capable of managing files on a computer.",
        "I can download new software when necessary.",
        "I can install new software when necessary.",
        "I can copy and paste text using a computer.",
        "I am capable of using discussion boards online.",
        "I am capable of using chat rooms online.",
        "I am capable of prioritizing my responsibilities.",
        "I am a good time manager.",
        "I am a procrastinator.",
        "I am capable of making time for my coursework.",
        "I am able to balance many tasks at one time.",
        "I am goal-oriented.",
        "I am self-disciplined when it comes to my studies.",
        "I am self-motivated.",
        "I take responsibility for my learning.",
        "I am capable of critical thinking.",
        "I often leave tasks unfinished.",
        "I require help to understand written instructions.",
        "I wait until the last minute to work on assignments.",
        "I have trouble comprehending what I read.",
        "I need faculty to remind me of assignment due dates.",
        "I need incentives/rewards to motivate me to complete a task.",
        "Because of my personal schedule, I need online courses.",
        "It is difficult for me to go to campus to complete course requirements.",
        "I need online courses because of my geographical distance from universities.",
        "I need online courses because of my work schedule.",
        "I need the freedom of completing coursework at the time and place of my choosing.",
        "I can learn by working independently.",
        "I am self-directed in my learning.",
        "I am capable of solving problems alone.",
        "I need face to face interaction to learn.",
        "I need faculty feedback on my completed assignments.",
        "I am a good reader.",
        "I need classroom discussion to learn.",
        "I am capable of asking for help when I have a problem.",
        "I am comfortable learning new skills.",
        "I read carefully.",
        "I am a good writer.",
        "I am capable of following written instructions.",
        "I am capable of conveying my ideas in writing."
        ]

        i = 1
        for question in questions:
            label = question
            choices = [(1, 'Strongly Disagree'),(2,'Disagree'),(3,'Neither Agree Nor Disagree'),(4,'Agree'),(5,'Strongly Agree')]
            field = forms.ChoiceField(label=label, choices=choices,
                    widget=forms.RadioSelect, required=True)
            self.fields['%d' % i] = field
            i += 1