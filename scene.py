class Scene(object):
	PLACE_DEPTH = 15.0

	def __init__(self):
		self.node_list = list()

	def add_node(self, node):
		self.node_list.append(node)

	def render(self):
		for node in self.node_list:
			node.render()