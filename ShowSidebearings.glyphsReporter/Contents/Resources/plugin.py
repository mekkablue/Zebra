# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################


from GlyphsApp.plugins import *

class ShowSidebearings(ReporterPlugin):

	def settings(self):
		self.menuName = 'Sidebearings'

	def foreground(self, layer):
		NSColor.redColor().set()
		rectToBeFilled = NSMakeRect(10, 10, 20, 20)
		NSBezierPath.fillRect_(rectToBeFilled)
