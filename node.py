import random
from OpenGL.GL import glCallList, glColor3f, glMaterialfv, glMultMatrixf, glPopMatrix, glPushMatrix, \
                      GL_EMISSION, GL_FRONT
import numpy
import color
from primitive import G_OBJ_SPHERE
from transformation import scaling, translation


class Node(object):
	def __init__(self):
		self.color_index = random.randint(color.MIN_COLOR, color.MAX_COLOR)
		self.translation_matrix = numpy.identity(4)
		self.scaling_matrix = numpy.identity(4)

	def render(self):
		""" Render node. """
		glPushMatrix()
		glMultMatrixf(numpy.transpose(self.translation_matrix))
		glMultMatrixf(self.scaling_matrix)
		cur_color = color.COLORS[self.color_index]
		glColor3f(cur_color[0], cur_color[1], cur_color[2])
		self.render_self()
		glPopMatrix()

	def render_self(self):
		raise NotImplementedError("The Abstract Node Class doesn't define 'render_self'")

	def translate(self, x, y, z):
		self.scaling_matrix = numpy.dot(self.translation_matrix, translation([x, y, z]))

	def scale(self, s):
		self.scaling_matrix = numpy.dot(self.scaling_matrix, scaling([s, s, s]))

class Primitive(Node):
	def __init__(self):
		super(Primitive, self).__init__()
		self.call_list = None

	def render_self(self):
		glCallList(self.call_list)

class Sphere(Primitive):
	def __init__(self):
		super(Sphere, self).__init__()
		self.call_list = G_OBJ_SPHERE