import wx
import wikipedia 
import wolframalpha

class MyFrame(wx.Frame): 

	def OnEnter(self, event): 
		input = self.txt.GetValue() 
		input = input.lower() 

		try: 
			app_id = "UX8XJX-373G2XJ8QH" 
			client = wolframalpha.Client(app_id)

			res = client.query(intrebare) 
			answer = next(res.results).text 

			print(answer)

		except:  
			randuri = input("Cate randuri doriti?")
			wikipedia.set_lang("ro") 
			print(wikipedia.summary(intrebare, senteces = randuri)) 
		

	def __init__(self): 
		wx.Frame.__init__(self, None, pos = wx.DefaultPosition, size = wx.Size(450, 100), style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx. VLIP_CHILDREN, title = "Ravis") 
		panel = wx.Panel (self) 
		my_sizer = wx.BoxSizer(wx.VERTICAL) 
		lbl = wx.StaticText(panel, label = "Buna, sunt Ravis, cu ce te pot ajuta?") 
		my_sizer.Add(lbl, 0, wx.ALL, 5) 
		self.txt = wx.TextCTRl(panel, style = wx.TE_PROCESS_ENTER,size = (400, 30)) 
		self.txt.SetFocus() 
		self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter) 
		my_sizer.Add(self.txt, 0, wx.ALL, 5) 
		panel.SetSizer(my_sizer) 
		self.Show() 



if __name__ == "__main__": 
	app = wx.App(True) 
	frame = MyFrame() 
	app.MainLoop() 
