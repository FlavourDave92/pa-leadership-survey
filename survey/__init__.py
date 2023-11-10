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
    return Constants.qualityfail_url_template.replace(
        "[unserTicket]", participant_label
    )


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
        "https://survey.maximiles.com/quality?p=89360&m=[unserTicket]"
    )

    # finished
    # TODO: Replace with respondi URL
    complete_url_template = (
        "https://survey.maximiles.com/complete?p=89360_aca788b3&m=[unserTicket]"
    )


def creating_session(subsession):
    # for player in subsession.get_players():
    #     state_items = [
    #         "PRS1T1",
    #         "PRS1T2",
    #         "PRS2T1",
    #         "PRS2T2",
    #         "PRS3T1",
    #         "PRS3T2",
    #         "PRS4T1",
    #         "PRS4T2",
    #         "FRS1T1",
    #         "FRS1T2",
    #         "FRS2T1",
    #         "FRS2T2",
    #         "FRS3T1",
    #         "FRS3T2",
    #         "FRS4T1",
    #         "FRS4T2",
    #         "ARS1T1",
    #         "ARS1T2",
    #         "ARS2T1",
    #         "ARS2T2",
    #         "ARS3T1",
    #         "ARS3T2",
    #         "ARS4T1",
    #         "ARS4T2",
    #     ]

    #     random.shuffle(state_items)

    #     player.participant.vars["StateItemsRandom"] = state_items

    #     state_items_rest = ["PR1", "PR2", "PR3", "PR4"]
    #     random.shuffle(state_items_rest)

    #     player.participant.vars["StateItemsRestRandom"] = state_items_rest

    #     # 8 items per page
    #     player.participant.vars["StateItemsPage1"] = player.participant.vars[
    #         "StateItemsRandom"
    #     ][0:8]
    #     player.participant.vars["StateItemsPage2"] = player.participant.vars[
    #         "StateItemsRandom"
    #     ][8:16]
    #     player.participant.vars["StateItemsPage3"] = player.participant.vars[
    #         "StateItemsRandom"
    #     ][16:24]
    #     player.participant.vars["StateItemsPage4"] = player.participant.vars[
    #         "StateItemsRandom"
    #     ][24:32]
    #     player.participant.vars["StateItemsPage5"] = player.participant.vars[
    #         "StateItemsRandom"
    #     ][32:35]

    #     player.session_variables = str(player.participant.vars)
    pass


def check_if_player_failed_comprehension_check(player):
    return Constants.right_comprehension_check_answer != player.comprehension


def check_if_player_failed_quality_check(player):
    return player.CON1 != Constants.right_quality_check_answer


def get_player_complete_url(participant_label):
    return Constants.complete_url_template.replace("[unserTicket]", participant_label)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # failed control check url
    player_qualityfail_url = models.StringField()

    session_variables = models.LongStringField()

    failed_quality_check = models.BooleanField()

    # finished
    player_complete_url = models.StringField()

    feedback = models.LongStringField(
        label="Wir sind sehr dankbar für Ihr Feedback zu unserem Experiment:",
        blank=True,
    )

    # Trait
    home_office = models.IntegerField(
        label="Wie häufig arbeiten Sie aktuell von Zuhause (Home Office)?",
        choices=[
            [0, "nie"],
            [1, "weniger als die Hälfte meiner Arbeitszeit"],
            [2, "mehr als die Hälfte meiner Arbeitszeit"],
            [3, "immer"],
        ],
        blank=False,
        widget=widgets.RadioSelect,
    )

    home_office_need = models.IntegerField(
        label="Würden Sie gerne häufiger/seltener von Zuhause arbeiten (Home Office)?",
        choices=[[0, "häufiger"], [1, "gleich viel wie aktuell"], [3, "seltener"]],
        blank=False,
        widget=widgets.RadioSelect,
    )

    risk_propensity = models.IntegerField(
        label="Wie schätzen Sie sich persönlich ein: Sind Sie im allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden?",
        choices=[
            [0, "0: überhaupt nicht risikofreudig"],
            [1, "1"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
            [6, "6"],
            [7, "7"],
            [8, "8"],
            [9, "9"],
            [10, "10: sehr risikofreudig"],
        ],
        blank=False,
        widget=widgets.RadioSelect,
    )

    teamlead = models.IntegerField(
        label="Haben Sie in Ihrem echten Berufsleben aktuell Personalverantwortung?",
        choices=[[0, "nein"], [1, "ja"]],
        blank=False,
        widget=widgets.RadioSelect,
    )

    hr_job = models.IntegerField(
        label="Arbeiten Sie in Ihrem echten Berufsleben aktuell im Personalwesen (HR)?",
        choices=[[0, "nein"], [1, "ja"]],
        blank=False,
        widget=widgets.RadioSelect,
    )

    pa_heard = models.IntegerField(
        label="Kennen Sie den Begriff „People Analytics“?",
        choices=[[0, "nein"], [1, "ja"]],
        blank=False,
        widget=widgets.RadioSelect,
    )

    pa_knowledge = models.IntegerField(
        label="Wissen Sie, was mit dem Begriff „People Analytics“ gemeint ist?",
        choices=[[0, "nein"], [1, "ja"]],
        blank=False,
        widget=widgets.RadioSelect,
    )

    pa_experience = models.IntegerField(
        label="Haben Sie jemals in einem Unternehmen gearbeitet, das aktiv ein System, wie das im Experiment gezeigte, verwendet hat?",
        choices=[[0, "nein"], [1, "ja"]],
        blank=False,
        widget=widgets.RadioSelect,
    )

    CMB1 = models.IntegerField(
        label="Ich bin zufrieden mit der Stadt, in der ich lebe.",
        choices=[
            [1, "1: stimme überhaupt nicht zu"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
            [6, "6"],
            [7, "7: stimme voll und ganz zu"],
        ],
        blank=False,
        widget=widgets.RadioSelect,
    )

    CMB2 = models.IntegerField(
        label="Ich bin mit den Fernsehprogrammen zufrieden.",
        choices=[
            [1, "1: stimme überhaupt nicht zu"],
            [2, "2"],
            [3, "3"],
            [4, "4"],
            [5, "5"],
            [6, "6"],
            [7, "7: stimme voll und ganz zu"],
        ],
        blank=False,
        widget=widgets.RadioSelect,
    )

    PRS1T1 = make_field_7point(
        "How risky do you rate the action of the leader of Project A?"
    )
    PRS1T2 = make_field_7point(
        "How risky do you rate the action of the leader of Project B?"
    )
    PRS2T1 = make_field_7point(
        "How risky do you rate the action of the leader of Project A?"
    )
    PRS2T2 = make_field_7point(
        "How risky do you rate the action of the leader of Project B?"
    )
    PRS3T1 = make_field_7point(
        "How risky do you rate the action of the leader of Project A?"
    )
    PRS3T2 = make_field_7point(
        "How risky do you rate the action of the leader of Project B?"
    )
    PRS4T1 = make_field_7point(
        "How risky do you rate the action of the leader of Project A?"
    )
    PRS4T2 = make_field_7point(
        "How risky do you rate the action of the leader of Project B?"
    )
    FRS1T1 = make_field_7point("The leader of Project A will feel responsible for the outcome.")
    FRS1T2 = make_field_7point("The leader of Project B will feel responsible for the outcome.")
    FRS2T1 = make_field_7point("The leader of Project A will feel responsible for the outcome.")
    FRS2T2 = make_field_7point("The leader of Project B will feel responsible for the outcome.")
    FRS3T1 = make_field_7point("The leader of Project A will feel responsible for the outcome.")
    FRS3T2 = make_field_7point("The leader of Project B will feel responsible for the outcome.")
    FRS4T1 = make_field_7point("The leader of Project A will feel responsible for the outcome.")
    FRS4T2 = make_field_7point("The leader of Project B will feel responsible for the outcome.")
    ARS1T1 = make_field_7point("The leader of Project A acted responsibly.")
    ARS1T2 = make_field_7point("The leader of Project B acted responsibly.")
    ARS2T1 = make_field_7point("The leader of Project A acted responsibly.")
    ARS2T2 = make_field_7point("The leader of Project B acted responsibly.")
    ARS3T1 = make_field_7point("The leader of Project A acted responsibly.")
    ARS3T2 = make_field_7point("The leader of Project B acted responsibly.")
    ARS4T1 = make_field_7point("The leader of Project A acted responsibly.")
    ARS4T2 = make_field_7point("The leader of Project B acted responsibly.")


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
            "FRS1T2",
            "ARS1T1",
            "ARS1T2",
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
            "FRS2T2",
            "ARS2T1",
            "ARS2T2",
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
            "FRS3T2",
            "ARS3T1",
            "ARS3T2",
        ]
        return fields


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
            "FRS4T2",
            "ARS4T1",
            "ARS4T2",
        ]
        return fields


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
