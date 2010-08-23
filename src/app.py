import cocos


class Background(cocos.layer.Layer):

	def __init__(self):
		super( Background, self ).__init__()
		self.load_sprites()

	def load_sprites(self):
		self.building = cocos.sprite.Sprite( 'imgs/predio.png' )
		self.building.position = 120,200
		self.add( self.building)

		
if __name__ == "__main__":
	cocos.director.director.init()
	background = Background()
	main_scene = cocos.scene.Scene( background )
	cocos.director.director.run( main_scene)
