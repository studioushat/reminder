from datetime import datetime
import time

class Assignment():

	def __init__(self, title, desc, importance, month, day, hour, minute, countdown):

		self.importance = importance
		self.month = month
		self.day = day
		self.hour = hour
		self.minute = minute
		self.title = title
		self.desc = desc
		self.countdown = countdown
		self.strng = (str(importance)+" "+str(title)+" - "+ str(month)+" "+str(day)+" • "+str(hour)+":"+str(minute)+"\n"+str(desc)+"\n"+str(countdown))
		
		
		#today = datetime.date.today()
		#year = today.year

		currentyear = time.strftime("%y")

		if len(hour) == 1:

			newhour = hour
			newhour = "0" + eventhour

		else:

			newhour = hour

		eventTime=str(currentyear+" "+month + " " + day + ":" + newhour + ":" + minute)

		CurrentTime = time.strftime("%m:%d:%H:%M")
		
		self.datetime = datetime.strptime(eventTime, "%y %B %d:%H:%M")

		#delta = self.datetime - CurrentTime
		
		#self.second = delta.total_seconds()