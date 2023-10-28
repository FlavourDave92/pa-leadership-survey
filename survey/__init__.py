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
    for player in subsession.get_players():
        state_items = [
            "TRS1",
            "TRS2",
            "TRS3",
            "TRO1",
            "TRO2",
            "TRO3",
            "TRO4",
            "TRO5",
            "TRO6",
            "TRO7",
            "DTP1",
            "DTP2",
            "DTP3",
            "PU1",
            "PU2",
            "PU3",
            "PU4",
            "ITQ1",
            "ITQ2",
            "ITQ3",
            "PAPRC1",
            "PAPRC2",
            "PAPRC3",
            "PAPRC4",
            "CON1",
            "MC1",
            "MC2",
            "PPA1",
            "PPA2",
            "PPA3",
            "PPA4",
            "PPA5",
            "PPA6",
        ]

        random.shuffle(state_items)

        player.participant.vars["StateItemsRandom"] = state_items

        state_items_rest = ["PR1", "PR2", "PR3", "PR4"]
        random.shuffle(state_items_rest)

        player.participant.vars["StateItemsRestRandom"] = state_items_rest

        # 8 items per page
        player.participant.vars["StateItemsPage1"] = player.participant.vars[
            "StateItemsRandom"
        ][0:8]
        player.participant.vars["StateItemsPage2"] = player.participant.vars[
            "StateItemsRandom"
        ][8:16]
        player.participant.vars["StateItemsPage3"] = player.participant.vars[
            "StateItemsRandom"
        ][16:24]
        player.participant.vars["StateItemsPage4"] = player.participant.vars[
            "StateItemsRandom"
        ][24:32]
        player.participant.vars["StateItemsPage5"] = player.participant.vars[
            "StateItemsRandom"
        ][32:35]

        player.session_variables = str(player.participant.vars)


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

    # Manipulation Check
    MAN_PA = make_field_7point(
        "The decission about my bonus was the result of human rationale."
    )
    MAN_RETURN = make_field_7point("My bonus was relatively high.")

    # State
    PR1 = make_field_7point(
        "… Aufzeichnungen über das Verhalten am Arbeitsplatz an Dritte weitergegeben werden?"
    )
    PR2 = make_field_7point("… personenbezogene Daten missbraucht werden?")
    PR3 = make_field_7point(
        "… personenbezogene Daten ohne das Wissen der Beschäftigten an andere Personen oder Firmen weitergegeben werden?"
    )
    PR4 = make_field_7point(
        "… personenbezogene Daten an staatliche Behörden weitergegeben werden könnte?"
    )
    TRS1 = make_field_7point(
        "Das System ist eine sichere Umgebung für die Nutzung am Arbeitsplatz."
    )
    TRS2 = make_field_7point("Das System ist eine zuverlässige Umgebung zum Arbeiten.")
    TRS3 = make_field_7point(
        "Das System geht kompetent mit den personebezogen Daten der Beschäftigten um."
    )
    TRO1 = make_field_7point(
        "Ich glaube, dass diese*r Arbeitgeber*in eine hohe Integrität besitzt."
    )
    TRO2 = make_field_7point(
        "Ich kann davon ausgehen, dass diese*r Arbeitgber*in mich konsistent und vorhersehbar behandelt."
    )
    TRO3 = make_field_7point(
        "Diese*r Arbeitgeber*in ist nicht immer aufrichtig und ehrlich."
    )
    TRO4 = make_field_7point(
        "Grundsätzlich glaube ich, dass diese*r Arbeitgeber*in gute Absichten und Motive hat."
    )
    TRO5 = make_field_7point(
        "Ich glaube nicht, dass mich diese*r Arbeitgeber*in fair behandelt."
    )
    TRO6 = make_field_7point("Diese*r Arbeitgeber*in ist offen und ehrlich mit mir.")
    TRO7 = make_field_7point(
        "Ich bin mir nicht sicher, ob ich diese*r Arbeitgeber*in komplett vertraue."
    )
    DTP1 = make_field_7point(
        "Im Vergleich zu anderen bin ich vorsichtiger was den Umgang mit meinen persönlichen Daten angeht."
    )
    DTP2 = make_field_7point(
        "Im Vergleich zu anderen finde ich es wichtiger, persönliche Daten privat zu halten."
    )
    DTP3 = make_field_7point(
        "Im Vergleich zu anderen habe ich weniger Bedenken bzgl. potentieller Gefahren für meine Privatsphäre."
    )
    PU1 = make_field_7point("Ich würde das System bei meiner Arbeit nützlich finden.")
    PU2 = make_field_7point(
        "Die Nutzung des Systems würde mir helfen, Aufgaben schneller zu erledigen."
    )
    PU3 = make_field_7point(
        "Die Nutzung des Systems würde mir dabei helfen, meine Produktivität zu steigern."
    )
    PU4 = make_field_7point(
        "Wenn ich das System nutzen würde, erhöhe ich meine Chancen auf eine Gehaltserhöhung."
    )
    ITQ1 = make_field_7point(
        "Angesichts dieser Situation ist es wahrscheinlich, dass ich im nächsten Jahr aktiv nach einer neuen Stelle suchen werde."
    )
    ITQ2 = make_field_7point("In dieser Situation werde ich oft ans Kündigen denken.")
    ITQ3 = make_field_7point(
        "In dieser Situation werde ich mich wahrscheinlich im nächsten Jahr nach einer neuen Stelle umsehen."
    )
    PPA1 = make_field_7point(
        "Das System kann menschliches Denken in den Hintergrund drängen und die Kompetenz von Führungskräften untergraben."
    )
    PPA2 = make_field_7point(
        "Das System kann die Autonomie der Beschäftigten beeinträchtigen."
    )
    PPA3 = make_field_7point(
        "Das System kann Pfadabhängigkeiten fördern. Das bedeutet, sich auf Maßnahmen zu konzentrieren, die sich in der Vergangenheit als erfolgreich erwiesen haben, während neue Muster und Parameter ignoriert werden."
    )
    PPA4 = make_field_7point(
        "Bei Führungskräften kann das System zu Reduktionismus und einer Illusion von Kontrolle führen."
    )
    PPA5 = make_field_7point(
        "Die vom System erstellten Analysen können zu selbsterfüllenden Prophezeiungen führen. Ob die Vorhersage korrekt war oder lediglich durch die Reaktion auf die Analyse wahrgeworden ist, kann nicht festgestellt werden."
    )

    PPA6 = make_field_7point(
        "Das System kann Transparenz und Verantwortlichkeit beeinträchtigen."
    )
    PAPRC1 = make_field_7point(
        "Ich bin besorgt, dass die von mir an das System übermittelten Informationen missbraucht werden könnten."
    )
    PAPRC2 = make_field_7point(
        "Ich bin besorgt, dass eine Person private Informationen über mich im System finden könnte."
    )
    PAPRC3 = make_field_7point(
        "Ich habe Bedenken, Informationen an das System zu übermitteln, weil ich nicht weiß, was andere damit anfangen können."
    )
    PAPRC4 = make_field_7point(
        "Ich habe Bedenken, Informationen an das System zu übermitteln, weil sie auf eine Weise verwendet werden könnten, die ich nicht vorhergesehen habe."
    )
    CON1 = make_field_7point("Wählen Sie hier den zweiten Kreis von rechts (++) an.")
    MC1 = make_field_7point(
        "Das System stellt direkte Prognosen und Vorhersagen über zukünftige Entwicklungen bereit."
    )
    MC2 = make_field_7point(
        "Das System stellt direkte Handlungsempfehlungen für die Optimierung einzelner Faktoren bereit."
    )


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
class State1(Page):
    form_model = "player"
    template_name = "survey/Survey.html"

    @staticmethod
    def get_form_fields(player):
        fields = player.participant.vars["StateItemsPage1"]
        return fields

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.player_qualityfail_url = get_player_qualityfail_url(
            player.participant.label
        )
        player.player_complete_url = get_player_complete_url(player.participant.label)


class State2(Page):
    form_model = "player"
    template_name = "survey/Survey.html"

    @staticmethod
    def get_form_fields(player):
        fields = player.participant.vars["StateItemsPage2"]
        return fields


class State3(Page):
    form_model = "player"
    template_name = "survey/Survey.html"

    @staticmethod
    def get_form_fields(player):
        fields = player.participant.vars["StateItemsPage3"]
        return fields


class State4(Page):
    form_model = "player"
    template_name = "survey/Survey.html"

    @staticmethod
    def get_form_fields(player):
        fields = player.participant.vars["StateItemsPage4"]
        return fields


class State5(Page):
    form_model = "player"
    template_name = "survey/Survey.html"

    @staticmethod
    def get_form_fields(player):
        fields = player.participant.vars["StateItemsPage5"]
        return fields


class StateRest(Page):
    form_model = "player"
    template_name = "survey/SurveyRest.html"

    @staticmethod
    def get_form_fields(player):
        fields = player.participant.vars["StateItemsRestRandom"]
        return fields

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.failed_quality_check = check_if_player_failed_quality_check(player)


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


page_sequence = [
    ManCheck,
    State1,
    State2,
    State3,
    State4,
    State5,
    StateRest,
    QualityFail,
    Experience,
    Feedback,
    End,
]
