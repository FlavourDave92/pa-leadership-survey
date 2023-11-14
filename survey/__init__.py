import otree.api
from otree.api import *
import random
import itertools
from math import ceil


# FUNCTIONS
def make_field_7point(label):
    return models.IntegerField(
        choices=[[1, ""], [2, ""], [3, ""], [4, ""], [5, ""], [6, ""], [7, ""]],
        label=label,
        widget=widgets.RadioSelect,
        blank=False,
    )


def get_player_qualityfail_url(participant_label):
    return Constants.qualityfail_url_template


class Subsession(BaseSubsession):
    pass


class Constants(BaseConstants):
    name_in_url = "survey"
    players_per_group = None
    num_rounds = 1

    # right answer to quality check in survey
    right_quality_check_answer = 6

    # failed control check url
    # TODO: Replace with respondi URL
    qualityfail_url_template = (
        "https://app.prolific.com/submissions/complete?cc=CGA1Y97A"
    )

    # finished
    # TODO: Replace with respondi URL
    complete_url_template = "https://app.prolific.com/submissions/complete?cc=C1N2Y8X2"


def creating_session(subsession):
    # treatments
    treatment_pa = ["1_and_4", "2_and_3"]
    positive_szenarios = ["1_and_4", "2_and_3"]

    treatment_combinations = [
        (pa, positive_szenario)
        for pa in treatment_pa
        for positive_szenario in positive_szenarios
    ]

    treatment_cycle = itertools.cycle(treatment_combinations)

    for player in subsession.get_players():
        player.treatment_pa, player.positive_szenarios = next(treatment_cycle)


def check_if_player_failed_comprehension_check(player):
    return Constants.right_comprehension_check_answer != player.comprehension


def check_if_player_failed_quality_check(player):
    return player.CON1 != Constants.right_quality_check_answer


def get_player_complete_url(participant_label):
    return Constants.complete_url_template


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # treatments
    positive_szenarios = models.StringField()
    treatment_pa = models.StringField()

    # failed control check url
    player_qualityfail_url = models.StringField()

    session_variables = models.LongStringField()

    failed_quality_check = models.BooleanField()

    # finished
    player_complete_url = models.StringField()

    feedback = models.LongStringField(
        label="We are very grateful for your feedback on our experiment:",
        blank=True,
    )

    # Trait
    feedback = models.LongStringField(
        label="We are very grateful for your feedback on our experiment:",
        blank=True,
    )

    # Trait
    home_office = models.IntegerField(
        label="How often do you currently work from home (home office)?",
        choices=[
            [0, "never"],
            [1, "less than half of my working hours"],
            [2, "more than half of my working hours"],
            [3, "always"],
        ],
        blank=False,
        widget=widgets.RadioSelect,
    )

    home_office_need = models.IntegerField(
        label="Would you like to work from home more often/less often (home office)?",
        choices=[[0, "more often"], [1, "same amount as currently"], [3, "less often"]],
        blank=False,
        widget=widgets.RadioSelect,
    )

    risk_propensity = models.IntegerField(
        label="How do you see yourself: Are you prepared to take risks, or do you rather try to avoid them?",
        choices=[
            [0, "0: not at all willing to take risks"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
            [6, "6"],
            [7, "7"],
            [8, "8"],
            [9, "9"],
            [10, "10: very willing to take risks"],
        ],
        blank=False,
        widget=widgets.RadioSelect,
    )

    algo_aversion = models.IntegerField(
        label="In general, I will rather decide by myself rather than follow the decisions given by an algorithm.",
        choices=[
            [1, "1: fully disagree"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
            [6, "6"],
            [7, "7: fully agree"],
        ],
        blank=False,
        widget=widgets.RadioSelect,
    )

    teamlead = models.IntegerField(
        label="Do you currently have personnel responsibility in your real working life?",
        choices=[[0, "no"], [1, "yes"]],
        blank=False,
        widget=widgets.RadioSelect,
    )

    hr_job = models.IntegerField(
        label="Do you currently work in human resources (HR) in your real professional life?",
        choices=[[0, "no"], [1, "yes"]],
        blank=False,
        widget=widgets.RadioSelect,
    )

    pa_heard = models.IntegerField(
        label="Before this experiment, did you know what the term people analytics meant?",
        choices=[[0, "no"], [1, "yes"]],
        blank=False,
        widget=widgets.RadioSelect,
    )

    pa_knowledge = models.IntegerField(
        label='Before this experiment, did you know what is meant by the term "people analytics"?',
        choices=[[0, "no"], [1, "yes"]],
        blank=False,
        widget=widgets.RadioSelect,
    )

    pa_experience = models.IntegerField(
        label="Have you ever worked in a company that actively used a people analytics system?",
        choices=[[0, "no"], [1, "yes"]],
        blank=False,
        widget=widgets.RadioSelect,
    )

    # Control Question
    CON1 = make_field_7point("Please select the second circle from the right (++).")

    CMB1 = models.IntegerField(
        label="I am happy with the city I live in.",
        choices=[
            [1, "1: fully disagree"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
            [6, "6"],
            [7, "7: fully agree"],
        ],
        blank=False,
        widget=widgets.RadioSelect,
    )

    CMB2 = models.IntegerField(
        label="I am happy with the television programs.",
        choices=[
            [1, "1: fully disagree"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
            [6, "6"],
            [7, "7: fully agree"],
        ],
        blank=False,
        widget=widgets.RadioSelect,
    )

    PRS1T1 = make_field_7point(
        "How risky do you rate the action of the leader of Project\xa0A?"  # \xa0 = non-breaking space
    )
    PRS1T2 = make_field_7point(
        "How risky do you rate the action of the leader of Project\xa0B?"
    )
    PRS2T1 = make_field_7point("How risky do you rate the action of leader\xa0A?")
    PRS2T2 = make_field_7point("How risky do you rate the action of leader\xa0B?")
    PRS3T1 = make_field_7point("How risky do you rate the action of leader\xa0A?")
    PRS3T2 = make_field_7point("How risky do you rate the action of leader\xa0B?")
    PRS4T1 = make_field_7point("How risky do you rate the action of leader\xa0A?")
    PRS4T2 = make_field_7point("How risky do you rate the action of leader\xa0B?")

    FRS1T1 = make_field_7point(
        "The leader of Project A will feel responsible for the outcome."
    )
    FRS1T2 = make_field_7point(
        "The leader of Project B will feel responsible for the outcome."
    )
    FRS2T1 = make_field_7point("Leader\xa0A will feel responsible for the outcome.")
    FRS2T2 = make_field_7point("Leader\xa0B will feel responsible for the outcome.")
    FRS3T1 = make_field_7point("Leader\xa0A will feel responsible for the outcome.")
    FRS3T2 = make_field_7point("Leader\xa0B will feel responsible for the outcome.")
    FRS4T1 = make_field_7point("Leader\xa0A will feel responsible for the outcome.")
    FRS4T2 = make_field_7point("Leader\xa0B will feel responsible for the outcome.")

    ARS1T1 = make_field_7point("The leader of Project\xa0A acted responsibly.")
    ARS1T2 = make_field_7point("The leader of Project\xa0B acted responsibly.")
    ARS2T1 = make_field_7point("Leader\xa0A acted responsibly.")
    ARS2T2 = make_field_7point("Leader\xa0B acted responsibly.")
    ARS3T1 = make_field_7point("Leader\xa0A acted responsibly.")
    ARS3T2 = make_field_7point("Leader\xa0B acted responsibly.")
    ARS4T1 = make_field_7point("Leader\xa0A acted responsibly.")
    ARS4T2 = make_field_7point("Leader\xa0B acted responsibly.")

    ETHS1T1 = make_field_7point("The leader of Project\xa0A acted ethically.")
    ETHS1T2 = make_field_7point("The leader of Project\xa0B acted ethically.")
    ETHS2T1 = make_field_7point("Leader\xa0A acted ethically.")
    ETHS2T2 = make_field_7point("Leader\xa0B acted ethically.")
    ETHS3T1 = make_field_7point("Leader\xa0A acted ethically.")
    ETHS3T2 = make_field_7point("Leader\xa0B acted ethically.")
    ETHS4T1 = make_field_7point("Leader\xa0A acted ethically.")
    ETHS4T2 = make_field_7point("Leader\xa0B acted ethically.")

    PROS1T1 = make_field_7point("The leader of Project\xa0A acted professionally.")
    PROS1T2 = make_field_7point("The leader of Project\xa0B acted professionally.")
    PROS2T1 = make_field_7point("Leader\xa0A acted professionally.")
    PROS2T2 = make_field_7point("Leader\xa0B acted professionally.")
    PROS3T1 = make_field_7point("Leader\xa0A acted professionally.")
    PROS3T2 = make_field_7point("Leader\xa0B acted professionally.")
    PROS4T1 = make_field_7point("Leader\xa0A acted professionally.")
    PROS4T2 = make_field_7point("Leader\xa0B acted professionally.")


# PAGES


class QualityFail(Page):
    # Only displayed if failed quality check
    @staticmethod
    def is_displayed(player):
        return player.failed_quality_check

    @staticmethod
    def vars_for_template(player):
        return dict(
            player_qualityfail_url=player.player_qualityfail_url,
        )


# PAGES
# class State1(Page):
#     form_model = "player"
#     template_name = "survey/Survey.html"

#     @staticmethod
#     def get_form_fields(player):
#         fields = player.participant.vars["StateItemsPage1"]
#         return fields

#     @staticmethod
#     def before_next_page(player, timeout_happened):
#         player.player_qualityfail_url = get_player_qualityfail_url(
#             player.participant.label
#         )
#         player.player_complete_url = get_player_complete_url(player.participant.label)


# class State2(Page):
#     form_model = "player"
#     template_name = "survey/Survey.html"

#     @staticmethod
#     def get_form_fields(player):
#         fields = player.participant.vars["StateItemsPage2"]
#         return fields


# class State3(Page):
#     form_model = "player"
#     template_name = "survey/Survey.html"

#     @staticmethod
#     def get_form_fields(player):
#         fields = player.participant.vars["StateItemsPage3"]
#         return fields


# class State4(Page):
#     form_model = "player"
#     template_name = "survey/Survey.html"

#     @staticmethod
#     def get_form_fields(player):
#         fields = player.participant.vars["StateItemsPage4"]
#         return fields


# class State5(Page):
#     form_model = "player"
#     template_name = "survey/Survey.html"

#     @staticmethod
#     def get_form_fields(player):
#         fields = player.participant.vars["StateItemsPage5"]
#         return fields


# class StateRest(Page):
#     form_model = "player"
#     template_name = "survey/SurveyRest.html"

#     @staticmethod
#     def get_form_fields(player):
#         fields = player.participant.vars["StateItemsRestRandom"]
#         return fields

#     @staticmethod
#     def before_next_page(player, timeout_happened):
#         player.failed_quality_check = check_if_player_failed_quality_check(player)


class Experience(Page):
    form_model = "player"
    form_fields = [
        "home_office",
        "home_office_need",
        "risk_propensity",
        "algo_aversion",
        "teamlead",
        "hr_job",
        "pa_heard",
        "pa_knowledge",
        "pa_experience",
        "CMB1",
        "CMB2",
    ]


class Feedback(Page):
    form_model = "player"
    form_fields = ["feedback"]


class End(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(
            player_complete_url=player.player_complete_url,
        )


class ManCheck(Page):
    form_model = "player"
    template_name = "survey/Survey.html"

    @staticmethod
    def get_form_fields(player):
        fields = ["MAN_PA", "MAN_RETURN"]
        return fields


class Landing(Page):
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.player_qualityfail_url = get_player_qualityfail_url(
            player.participant.label
        )


class Comprehension(Page):
    form_model = "player"
    form_fields = ["comprehension"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.failed_comprehension_check = check_if_player_failed_comprehension_check(
            player
        )


class SzenarioOne(Page):
    form_model = "player"
    template_name = "survey/SzenarioOne.html"

    @staticmethod
    def get_form_fields(player):
        fields = ["PRS1T1", "PRS1T2"]
        return fields


class SzenarioOneOutcome(Page):
    form_model = "player"
    template_name = "survey/SzenarioOneOutcome.html"

    @staticmethod
    def get_form_fields(player):
        fields = [
            "FRS1T1",
            "ARS1T1",
            "ETHS1T1",
            "PROS1T1",
            "FRS1T2",
            "ARS1T2",
            "ETHS1T2",
            "PROS1T2",
        ]
        return fields


class SzenarioTwo(Page):
    form_model = "player"
    template_name = "survey/SzenarioTwo.html"

    @staticmethod
    def get_form_fields(player):
        fields = ["PRS2T1", "PRS2T2"]
        return fields


class SzenarioTwoOutcome(Page):
    form_model = "player"
    template_name = "survey/SzenarioTwoOutcome.html"

    @staticmethod
    def get_form_fields(player):
        fields = [
            "FRS2T1",
            "ARS2T1",
            "ETHS2T1",
            "PROS2T1",
            "FRS2T2",
            "ARS2T2",
            "ETHS2T2",
            "PROS2T2",
        ]
        return fields


class SzenarioThree(Page):
    form_model = "player"
    template_name = "survey/SzenarioThree.html"

    @staticmethod
    def get_form_fields(player):
        fields = ["PRS3T1", "PRS3T2"]
        return fields


class SzenarioThreeOutcome(Page):
    form_model = "player"
    template_name = "survey/SzenarioThreeOutcome.html"

    @staticmethod
    def get_form_fields(player):
        fields = [
            "FRS3T1",
            "ARS3T1",
            "ETHS3T1",
            "PROS3T1",
            "FRS3T2",
            "CON1",
            "ARS3T2",
            "ETHS3T2",
            "PROS3T2",
        ]
        return fields

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.failed_quality_check = check_if_player_failed_quality_check(player)


class SzenarioFour(Page):
    form_model = "player"
    template_name = "survey/SzenarioFour.html"

    @staticmethod
    def get_form_fields(player):
        fields = ["PRS4T1", "PRS4T2"]
        return fields


class SzenarioFourOutcome(Page):
    form_model = "player"
    template_name = "survey/SzenarioFourOutcome.html"

    @staticmethod
    def get_form_fields(player):
        fields = [
            "FRS4T1",
            "ARS4T1",
            "ETHS4T1",
            "PROS4T1",
            "FRS4T2",
            "ARS4T2",
            "ETHS4T2",
            "PROS4T2",
        ]
        return fields

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.player_qualityfail_url = get_player_qualityfail_url(
            player.participant.label
        )
        player.player_complete_url = get_player_complete_url(player.participant.label)


# TODO: add remaining scenario pages


page_sequence = [
    Landing,
    # Comprehension,
    SzenarioOne,
    SzenarioOneOutcome,
    SzenarioTwo,
    SzenarioTwoOutcome,
    SzenarioThree,
    SzenarioThreeOutcome,
    SzenarioFour,
    SzenarioFourOutcome,
    QualityFail,
    Experience,
    Feedback,
    End,
]
