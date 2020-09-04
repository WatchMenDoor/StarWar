class GameStats():
    #跟踪游戏的统计信息
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        #游戏刚启动时处于非活动状态
        self.game_active = False
        #在任何情况下都不应重置最高得分
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
