import object_data as ojd

def restart():
    ojd.player_rect.center = (400,300)
    ojd.enemy_rect.center = (0,0)
    ojd.pixel_rect.center = (400,300)
    ojd.start_game = 0
    ojd.start_time = 0
    ojd.pass_time = 0
    ojd.summary = 0
    ojd.save_time_score = 0
    ojd.sum_time = 0
    ojd.sum_score = 0
    ojd.restart = 0

    ojd.enemy_speed = 1
    ojd.fram_animation = 0

    ojd.count = 0

    ojd.bullet_delay_time = 0
