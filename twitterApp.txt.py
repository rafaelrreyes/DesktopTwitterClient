import wx

class twitterGui(wx.Frame):
	
	#main constructor function to build main frame
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'Twitter Interace', size=(600,800))
		panel=wx.Panel(self)
		tweetButton=wx.Button(panel,label='Tweet',pos=(300,300),size=(50,50))
		clearButton=wx.Button(panel,label='Clear',pos=(300,400),size=(50,50))
		
		#bind event handling to components such as buttons
		self.Bind(wx.EVT_BUTTON, self.tweetButtonMethod, tweetButton)
		self.Bind(wx.EVT_CLOSE, self.closeWindow)
		self.Bind(wx.EVT_BUTTON, self.clearButtonMethod, clearButton)

	def tweetButtonMethod(self,event):
		#tweet code here
		self.Close(True)

	def clearButtonMethod(self,event):
		self.Close(True)

	#When window is closed, print on console a message
	def closeWindow(self,event):
		print('The user has terminated the program')
		self.Destroy()

if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=twitterGui(parent=None,id=-1)
	frame.Show()
	app.MainLoop()
	
