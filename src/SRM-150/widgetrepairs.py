class WidgetRepairs:
	def days(self, arrivals, numPerDay):
		in_shop = 0
		days = 0
		for widget in arrivals:
			in_shop = in_shop + widget

			if(in_shop > 0):
				days += 1

			in_shop = in_shop - numPerDay
			if(in_shop < 0):
				in_shop = 0
		while(in_shop > 0):
			in_shop -= numPerDay
			days += 1
		return days