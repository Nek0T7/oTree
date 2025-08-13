from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    # 一人のときは"None"と記述する
    NUM_ROUNDS = 1
    # 質問は1度だけ



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q_gender = models.CharField(initial=None,
                                choices=['男性', '女性', 'その他'],
                                verbose_name = 'あなたの性別を教えてください',
                                widget=widgets.RadioSelect)
    # ラジオボタンを使うときはwidget = widgets.RadioSelectを記述する

    q_age = models.IntegerField(initial=None,
                                 verbose_name='あなたの年齢を教えてください',
                                 choices=range(0, 120)
                                 # 年齢は0から120までの整数
                                )
    q_area = models.CharField(initial=None,
                               choices=['北海道', '東北', '関東', '中部', '関西', '中国', '四国', '九州', '沖縄'],
                               verbose_name='あなたの居住地を教えてください',
                               widget=widgets.RadioSelect)
    # ラジオボタンを使うときはwidget = widgets.RadioSelectを記述する

# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
