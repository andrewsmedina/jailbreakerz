import cocos


class Game(cocos.layer.Layer):

	def __init__(self):
		super(Game, self).__init__()
		self.load_sprites()

	def load_sprites(self):
		self.prison = cocos.sprite.Sprite('media/imgs/prison.png')
		self.prison.position = 100,170
		self.add(self.prison)

		self.fuu = cocos.sprite.Sprite('media/imgs/tall_thief.png')
		self.fuu.position = 200,240
		self.add(self.fuu)

		action = cocos.actions.interval_actions.JumpBy((200,0), height=100, jumps=5, duration=6)
		self.fuu.do(action)

