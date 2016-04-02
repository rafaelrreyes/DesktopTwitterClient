import wx
from twitter import *

class twitterGui(wx.Frame):
	
	t = 0
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

		#create access token/consumer key
		access_token = '65962166-2yYXHTmH7X0vXy5sh1hDp2RlXfbcu959VhdHnjGWh'
		access_token_secret = 'QI9zsM0vRwtvTq455k4xkEbbcH2cvpHlalOj187kNN4wo'
		consumer_key = 'DkPQfFHhPadZyNqvvqyoXSV1p'
		consumer_secret = 'QPDDdc6fCP0ApGVPdtl7UOxfIxIbcLQSjiObX2gvsEmtv5d6i8'
		global t
		t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

	def tweetButtonMethod(self,event):
		#tweet code here
		t.statuses.update(status="---- python app posted tweet success ----")

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
	
