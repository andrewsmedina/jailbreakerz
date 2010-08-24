import cocos


class Background(cocos.layer.Layer):

	def __init__(self):
		super( Background, self ).__init__()
		self.load_sprites()

	def load_sprites(self):
		self.prison = cocos.sprite.Sprite( 'imgs/prison.png' )
		self.prison.position = 200,160
		self.add( self.prison )

		self.fuu = cocos.sprite.Sprite( 'imgs/boneco.png' )
		self.fuu.position = 200,240
		self.add( self.fuu )

		action = cocos.actions.interval_actions.JumpBy( (200,0), height=100, jumps=5, duration=6 )
		self.fuu.do( action )
		
if __name__ == "__main__":
	cocos.director.director.init()
	background = Background()
	main_scene = cocos.scene.Scene( background )
	cocos.director.director.run( main_scene)
