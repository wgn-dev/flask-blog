lib = './core/bin'
import sys
sys.path.append(lib)

import FreeCAD as App
import FreeCADGui as Gui
class Console:
	def __init__(self, path):
		self.doc = path

	def OpenDoc(self):
		ram = []
		sin = App.openDocument(self.doc)
		for i in App.listDocuments():
			ram.append(i)
		cos = [App.ActiveDocument.Name]
		
		return ram

	def OpenObj(self):
		doc = self.OpenDoc()
		ram = []
		data = App.getDocument(doc[0])
		for i in data.Objects:
			ram.append(i.Name)
		return ram