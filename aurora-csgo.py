import config
from nanoleaf import Aurora
from server import GSIServer
from effects import bar_effect, flash_effect, fire_effect, flash

nanoleafs = Aurora(config.AURORA_IP, config.AUTH_TOKEN)
nanoleafs.effect = 'moonlight'

server = GSIServer((config.GSI_IP, config.GSI_PORT), config.GSI_TOKEN)


def on_bomb_state_changed(value):
    if value == 'exploded':
        nanoleafs.effect_set_raw(flash_effect(nanoleafs))
        nanoleafs.effect = 'moonlight'
        nanoleafs.effect_set_raw(fire_effect())


server.gamestate.round.register(on_bomb_state_changed)
server.start_server()
