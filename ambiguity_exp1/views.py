from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Decide(Page):
    form_model = models.Player
    form_fields = ['decision']


# class ResultsWaitPage(WaitPage):
#
#     def after_all_players_arrive(self):
#         pass


class Results(Page):
    pass


page_sequence = [
    Decide,
    #ResultsWaitPage,
    Results
]
