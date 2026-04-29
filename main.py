def on_overlap_tile(sprite, location):
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player, sprites.builtin.coral0, on_overlap_tile)

myCorg = corgio.create(SpriteKind.player)
myCorg.horizontal_movement()
myCorg.vertical_movement()
myCorg.update_sprite()
tiles.set_tilemap(tilemap("""
    level_0
    """))
myCorg.camera_follow()