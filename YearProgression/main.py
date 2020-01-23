from datetime import date, datetime , timedelta
import re
import json
import time
import os
import sys
import random
import urllib.request
import math, itertools
from aliniari_geocentrice import Planete


class Procentaj:
	def __init__(self):
		self.current_year
		self.today
		self.thisMonth
		self.EarthResult
		self.todayFull
		self.MoonResult
		self.MoonPerihelion
		self.NewMoonperihelion
		self.MercuryResult
		self.MercuryPerihelion
		self.NewMercuryPerihelion
		self.earth
		self.BarrEarth
		self.moon
		self.barrMoon
		self.mercury
		self.barrMercury
		self.motdResult
		self.Venus
		self.barrVenus
		self.VenusPerihelion
		self.NewVenusPerihelion
		self.MarsResult
		self.MarsPerihelion
		self.NewMarsPerihelion
		self.JupiterResult
		self.JupiterPerihelion
		self.NewSaturnPerihelion
		self.UranusResult
		self.UranusPerihelion
		self.NewUranusPerhelion
		self.NeptuneResult
		self.NeptunePerihelion
		self.NewNeptunePerihelion
		self.PlutoResult
		self.PlutoPerihelion
		self.NewPlutoPerihelion
		self.Pluto
		self.barrPluto
		self.HalleyResult
		self.HalleyPerihelion
		self.NewHalleyPerihelion
		self.Haley
		self.barrHalley
		self.TeslaResult
		self.barrTesla
		self.TeslaPerihelion
		self.NewTeslaPeihelion
		self.CeresResult
		self.CeresPerihelion
		self.NewCeresperihelion
		self.Ceres
		self.barrCeres
		self.HaumeaResult
		self.HaumeaPerihelion
		self.NewHaumeaPerihelion
		self.Haumea
		self.barrHaumea
		self.Makemakeresult
		self.MakemakePerihelion
		self.NewMakemakePerihelion
		self.Makemake
		self.barrMakemake
		self.ErisResult
		self.ErisPerihelion
		self.NewErisPerihelion
		self.Eris
		self.barrEris
		self.motdReuslt2
		self.motdResult
		self.VenusResult
		self.NewJupiterPerihelion
		self.JupiterResult
		self.ISS
		self.ISSResult
		self.BarreISS
		self.ora
		self.minut
		self.secunda
		self.SaturnPerihelion
		self.SaturnResult


Procentaj.current_year = date.today().year
Procentaj.today = int(datetime.today().strftime("%d"))
Procentaj.thisMonth = int(datetime.today().strftime("%m"))
Procentaj.ora = int(datetime.today().strftime("%H"))
Procentaj.minut = int(datetime.today().strftime("%M"))
Procentaj.secunda = int(datetime.today().strftime("%S"))

def motd():

	from time import sleep
	from bara_progres import ProgressBar

	steps = 100

	bara_progres3 = ProgressBar(steps)
	bara_progres3.prefix_text = '------>Progres:'

	for i in range(1, steps + 1):
		sleep(0.4)
		bara_progres3.show(i)

	bara_progres3.complete()
	Procentaj.motdResult = (
		("\n")
		+ str("\n")
		+ str(" __     __               _   __")
		+ str("\n")
		+ str(" \ \   / /              (_) / /")
		+ str("\n")
		+ str("  \ \_/ /__  __ _ _ __     / / ")
		+ str("\n")
		+ str("   \   / _ \/ _` | '__|   / /  ")
		+ str("\n")
		+ str("    | |  __/ (_| | |     / / _ ")
		+ str("\n")
		+ str("    |_|\___|\__,_|_|    /_/ (_)")
		+ str("\n\n")
		)
	print(Procentaj.motdResult)
	text = "Facut si gandit de GAL1LEO"

	for x in text:
		print(x, end = '')
		sys.stdout.flush()
		time.sleep(0.01)
	print("\n")
	time.sleep(1)


def Pamant():
	d0 = date(Procentaj.current_year, 1, 1)

	d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
	d1 = d1 + timedelta(days = 1)

	d2 = date(Procentaj.current_year, 12, 31)

	d3 = d2 - d0
	d3 = str(d3)
	#print(d3)
	d3 = d3.split()
	d3 = int(d3[0])
	d3 = d3 + 1

	ValuePercent = d3 / 100
	delta = d1 - d0
	delta = str(delta)
	delta = delta[:6]
	new = re.sub("[^0-9]", "", str(delta))
	new = str(new)
	new = new[:6]
	new = int(new)
	Procentaj.EarthResult = new / ValuePercent
	Procentaj.EarthResult = round(Procentaj.EarthResult, 2)

	Procentaj.earth = (
		("<Planeta> : </Pamant>")
		+ str("\n")
		+ str(("Ziua din an: ") + str("ziua ") + str(new) + str("\n"))
		+ str(("Progresul planetei Pamantului pana la completarea orbitei:") + str(Procentaj.EarthResult) + str("%") + str("\n"))
	)

	print(Procentaj.earth)
	procentaj = Procentaj.EarthResult
	barre = (
		"["
		+ "#" * int((50 / 100) * procentaj)
		+ "_" * int((50 / 100) * (100 - procentaj))
		+ "]"
	)

	Procentaj.BarrEarth = "Procentajul acestui an:" + (barre) + str("\n")
	print(Procentaj.BarrEarth)
	#print("------Datele d0, d1, d2, d3, new, delta, ValuePercent------")
	#print("d0:" + str(d0))
	#print("d1:" + str(d1))
	#print("d2:" + str(d2))
	#print("d3:" + str(d3))
	#print("New:" + str(new))
	#print("Delta:" + str(delta))
	#print("ValuePercent:" + str(ValuePercent))

#main_cerc.functie()
def Luna():
	years_ago_full = datetime.now() - timedelta(days = 1 * 365)
	years_ago_full = str(years_ago_full)
	years_ago = years_ago_full[:4]
	years_ago = int(years_ago)

	years_after_full = datetime.now() + timedelta(days = 1 * 365)
	years_after_full = str(years_after_full)
	years_after = years_after_full[:4]
	years_after = int(years_after)

	with open("/var/www/html/Orbit.json", "r") as O:
		orbit = json.load(O)
		thisYear = orbit["Moon"]

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days = 1)
			if(d0 >= d1 - timedelta(days = 27) and d0 <= d1):
				Procentaj.MoonPerihelion = d0

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days = 1)
			if (d0 <= d1 + timedelta(days = 27) and d0 >= d1):
				Procentaj.NewMoonperihelion = d0
				d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
				d3 = Procentaj.NewMoonperihelion - Procentaj.MoonPerihelion
				d3 = str(d3)
				d3 = d3.split()
				d3 = int(d3[0])
				d3 = d3 + 1
				ValuePercent = d3 / 100
				delta = d1 - Procentaj.MoonPerihelion
				delta = str(delta)
				delta = delta.split()
				delta = delta[0]
				new = re.sub("[^0-9]", "", str(delta))
				new = str(new)
				new = new[:6]
				new = int(new)
				Procentaj.MoonResult = new / ValuePercent
				Procentaj.MoonResult = round(Procentaj.MoonResult, 2)
				print("<Satelit> : </Luna>")
				print(("Ziua din an: ") + str("ziua ") + str(new))
				print(("Progresul satelitului Luna pana la completarea orbitei:") + str(Procentaj.MoonResult) + str("%"))

				procentaj = Procentaj.MoonResult
				barre = (
					"["
					+ "#" * int((50 / 100) * procentaj)
					+ "-" * int((50 / 100) * (100 - procentaj))
					+ "]"
				)
				print("Procentajul anului:" + (barre))
				print("\n")
				#print("years_after_full,years_ago, years_after,d0Year, d0Month, d0Day, d0, d1, d3, new, ValuePercent")
				#print("years_after_full:" + str(years_after_full))
				#print("years_ago:" + str(years_ago))
				#print("years_after:" + str(years_after))
				#print("d0Year" + str(d0Year))
				#print("d0Month" + str(d0Month))
				#print("d0Day" + str(d0Day))
				#print("d0:" + str(d0))
				#print("d1:" + str(d3))
				#print("d3:" + str(d3))
				#print("new:" + str(new))
				#print("ValuePercent" + str(ValuePercent)) '''';
def ISS2():

	d0 = datetime(Procentaj.current_year, 1 , 1,  hour = 0, minute = 0, second = 0)
	#print(d0)
	d1 = datetime(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today, Procentaj.ora, Procentaj.minut, Procentaj.secunda)
	#print(d1)
	d1 = d1 + timedelta(hours = 1, minutes = 32)
	#print(d1)

	d2 = datetime(Procentaj.current_year, 12, 31, 23, 59, 0)

	d3 = d2 - d0
	#print(d3)
	d3 = str(d3)
	d3 = d3.split()
	d3 = int(d3[0])
	d3 = d3 + 1

	ValuePercent = d3 / 100
	delta = d1 - d0
	delta = str(delta)
	delta = delta[:6]
	new = re.sub("[^0-9]", "", str(delta))
	#print(new)
	new = str(new)
	new = new[:6]
	new = int(new)
	Procentaj.ISSResult = new / ValuePercent
	Procentaj.ISSResult = round(Procentaj.ISSResult, 2)

	print("<Satelit> : <ISS>")
	print(("Ziua: ") + str("ziua ") + str(new))
	print(("Progresul satelitului ISS pana la completarea orbitei: ") + str(Procentaj.ISSResult) + str("%"))
	#print(Procentaj.ISS)
	procentaj = Procentaj.ISSResult
	barre = (
		"["
		+ "#" * int((50 / 100) * procentaj)
		+ "_" * int((50 / 100) * (100 - procentaj))
		+ "]"
	)

	Procentaj.BarreISS = "Procentajul acestui an:" + (barre) + str("\n")
	print(Procentaj.BarreISS)
	#print("------Datele d0, d1, d2, d3, new, delta, ValuePercent------")
	#print("d0:" + str(d0))
	#print("d1:" + str(d1))
	#print("d2:" + str(d2))
	#print("d3:" + str(d3))
	#print("New:" + str(new))
	#print("Delta:" + str(delta))
	#print("ValuePercent:" + str(ValuePercent))


def Haumea():
	years_ago_full = datetime.now() - timedelta(days=1 * 365)
	years_ago_full = str(years_ago_full)
	years_ago = years_ago_full[:4]
	years_ago = int(years_ago)

	years_after_full = datetime.now() + timedelta(days=1 * 365)
	years_after_full = str(years_after_full)
	years_after = years_after_full[:4]
	years_after = int(years_after)  # result

	with open("/var/www/html/Orbit.json", "r") as O:
			orbit = json.load(O)
			thisYear = orbit["Haumea"]
			for i in thisYear:
				d0Year = i[:4]
				d0Year = int(d0Year)
				d0Month = i[5:7]
				d0Month = int(d0Month)
				d0Day = i[8:10]
				d0Day = int(d0Day)
				d0 = date(d0Year, d0Month, d0Day)
				d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
				d1 = d1 + timedelta(days=1)
				if (d0 >= d1 - timedelta(days=103728) and d0 <= d1):
					Procentaj.HaumeaPerihelion = d0

			for i in thisYear:
				d0Year = i[:4]
				d0Year = int(d0Year)
				d0Month = i[5:7]
				d0Month = int(d0Month)
				d0Day = i[8:10]
				d0Day = int(d0Day)
				d0 = date(d0Year, d0Month, d0Day)
				d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
				d1 = d1 + timedelta(days=1)
				if (d0 <= d1 + timedelta(days=103774) and d0 >= d1):
					Procentaj.NewHaumeaPerihelion = d0
					d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
					d3 = Procentaj.NewHaumeaPerihelion - Procentaj.HaumeaPerihelion
					d3 = str(d3)
					d3 = d3.split()
					d3 = int(d3[0])
					d3 = d3 + 1
					ValuePercent = d3 / 100
					delta = d1 - Procentaj.HaumeaPerihelion
					delta = str(delta)
					delta = delta.split()
					delta = delta[0]
					new = re.sub("[^0-9]", "", str(delta))
					new = str(new)
					new = new[:6]
					new = int(new)
					Procentaj.HaumeaResult = new / ValuePercent
					Procentaj.HaumeaResult = round(Procentaj.HaumeaResult, 2)

					print("<Planeta pitica>: </Haumea>")
					print(("Ziua din an: ") + str("ziua ") + str(new))
					print(("Progresul planetei Haumea pana la completarea orbitei: ") + str(Procentaj.HaumeaResult) + str("%"))

					percent = Procentaj.HaumeaResult
					barre = (
					"["
					+ "#" * int((50 / 100) * percent)
					+ "-" * int((50 / 100) * (100 - percent))
					+ "]"
					)
					print("Procentajul anului(pana la finalizare): " + (barre))
					print("\n")
					#print("years_after_full:" + str(years_after_full))
					#print("years_ago:" + str(years_ago))
					#print("years_after:" + str(years_after))
					#print("d0Year" + str(d0Year))
					#print("d0Month" + str(d0Month))
					#print("d0Day" + str(d0Day))
					#print("d0:" + str(d0))
					#print("d1:" + str(d3))
					#print("d3:" + str(d3))
					#print("new:" + str(new))
					#print("ValuePercent" + str(ValuePercent))

def Marte():
	years_ago_full = datetime.now() - timedelta(days = 1 * 365)
	years_ago_full = str(years_ago_full)
	years_ago = years_ago_full[:4]
	years_ago = int(years_ago)

	years_after_full = datetime.now() + timedelta(days = 1* 365)
	years_after_full = str(years_after_full)
	years_after = years_after_full[:4]
	years_after = int(years_after)

	with open("/var/www/html/Orbit.json", "r") as O:
		orbit = json.load(O)
		thisYear = orbit["Mars"]

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days = 1)
			if (d0 >= d1 - timedelta(days = 687) and d0 <= d1):
				Procentaj.MarsPerihelion = d0

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days = 1)
			if(d0 <= d1 + timedelta(days = 687) and d0 >= d1):
				Procentaj.NewMarsPerihelion = d0
				d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
				d3 = Procentaj.NewMarsPerihelion - Procentaj.MarsPerihelion
				d3 = str(d3)
				d3 = d3.split()
				d3 = int(d3[0])
				d3 = d3 + 1
				ValuePercent = d3 / 100
				delta = d1 - Procentaj.MarsPerihelion
				delta = str(delta)
				delta = delta.split()
				delta = delta[0]
				new = re.sub("[^0-9]", "", str(delta))
				new = str(new)
				new = new[:6]
				new = int(new)
				Procentaj.MarsResult = new / ValuePercent
				Procentaj.MarsResult = round(Procentaj.MarsResult, 2)
				print("<Planeta> : </Marte>")
				print(("Ziua din an: ") + str("ziua ") + str(new))
				print(("Progresul planetei Marte pana la completarea orbitei:") + str(Procentaj.MarsResult) + str("%"))
				procentaj = Procentaj.MarsResult
				barre = (
					"["
					+ "#" * int((50 / 100) * procentaj)
					+ "-" * int((50 /100) * (100 - procentaj))
					+"]"
				)
				print("Procentaj anului:" + (barre))
				print('\n')
				#print("years_after_full:" + str(years_after_full))
				#print("years_ago:" + str(years_ago))
				#print("years_after:" + str(years_after))
				#print("d0Year" + str(d0Year))
				#print("d0Month" + str(d0Month))
				#print("d0Day" + str(d0Day))
				#print("d0:" + str(d0))
				#print("d1:" + str(d3))
				#print("d3:" + str(d3))
				#print("new:" + str(new))
				#print("ValuePercent" + str(ValuePercent))

def Neptun():
	years_ago_full = datetime.now() - timedelta(days = 1 * 365)
	years_ago_full = str(years_ago_full)
	years_ago = years_ago_full[:4]
	years_ago = int(years_ago)

	years_after_full = datetime.now() + timedelta(days = 1 * 365)
	years_after_full = str(years_after_full)
	years_after = years_after_full[:4]
	years_after = int(years_after)

	with open("/var/www/html/Orbit.json", "r") as O:
		orbit = json.load(O)
		thisYear = orbit["Neptune"]

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days = 1)
			if(d0 >= d1 - timedelta(days = 60265) and d0 <= d1):
				Procentaj.NeptunePerihelion = d0

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days = 1)
			if (d0 <= d1 + timedelta(days = 60265) and d0 >= d1):
				Procentaj.NewNeptunePerihelion = d0
				d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
				d3 = Procentaj.NewNeptunePerihelion - Procentaj.NeptunePerihelion
				d3 = str(d3)
				d3 = d3.split()
				d3 = int(d3[0])
				d3 = d3 + 1
				ValuePercent = d3 / 100
				delta = d1 - Procentaj.NeptunePerihelion
				delta = str(delta)
				delta = delta.split()
				delta = delta[0]
				new = re.sub("[^0-9]", "", str(delta))
				new = str(new)
				new = new[:6]
				new = int(new)
				Procentaj.NeptuneResult = new / ValuePercent
				Procentaj.NeptuneResult = round(Procentaj.NeptuneResult, 2)
				print("<Planeta> : </Neptun>")
				print(("Ziua din an: ") + str("ziua ") + str(new))
				print(("Progresul planetei Neptun pana la completarea orbitei:") + str(Procentaj.NeptuneResult) + str("%"))

				procentaj = Procentaj.NeptuneResult
				barre = (
					"["
					+ "#" * int((50 / 100) * procentaj)
					+ "-" * int((50 / 100) * (100 - procentaj))
					+ "]"
				)
				print("Procentajul anului:" + (barre))
				print("\n")

				#print("years_after_full:" + str(years_after_full))
				#print("years_ago:" + str(years_ago))
				#print("years_after:" + str(years_after))
				#print("d0Year" + str(d0Year))
				#print("d0Month" + str(d0Month))
				#print("d0Day" + str(d0Day))
				#print("d0:" + str(d0))
				#print("d1:" + str(d3))
				#print("d3:" + str(d3))
				#print("new:" + str(new))
				#print("ValuePercent" + str(ValuePercent))

def Mercur():
	years_ago_full = datetime.now() - timedelta(days = 1 * 365)
	years_ago_full = str(years_ago_full)
	years_ago = years_ago_full[:4]
	years_ago = int(years_ago)

	years_after_full = datetime.now() + timedelta(days = 1 * 365)
	years_after_full = str(years_after_full)
	years_after = years_after_full[:4]
	years_after = int(years_after)

	with open("/var/www/html/Orbit.json", "r") as O:
		orbit = json.load(O)
		thisYear = orbit["Mercury"]

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days = 1)
			if (d0 >= d1 - timedelta(days = 88) and d0 <= d1):
				Procentaj.MercuryPerihelion = d0

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days = 1)
			if (d0 <= d1 + timedelta(88) and d0 >= d1):
				Procentaj.NewMercuryPerihelion = d0
				d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
				d3 = Procentaj.NewMercuryPerihelion - Procentaj.MercuryPerihelion
				d3 = str(d3)
				d3 = d3.split()
				d3 = int(d3[0])
				d3 = d3 + 1
				ValuePercent = d3 / 100
				delta = d1 - Procentaj.MercuryPerihelion
				delta = str(delta)
				delta = delta.split()
				delta = delta[0]
				new = re.sub("[^0-9]", "", str(delta))
				new = str(new)
				new = new[:6]
				new = int(new)
				Procentaj.MercuryResult = new / ValuePercent
				Procentaj.MercuryResult = round(Procentaj.MercuryResult, 2)
				print("<Planeta> : </Mercur>")
				print(("Ziua din an: ") + str("ziua ") + str(new))
				print(("Progresul planetei Mercur pana la completarea orbitei: ") + str(Procentaj.MercuryResult) + str("%"))
				procentaj = Procentaj.MercuryResult
				barre = (
					"["
					+ "#" * int((50 / 100) * procentaj)
					+ "-" * int((50 / 100) * (100 - procentaj))
					+ "]"
				)

				print("Procentajul anului:" + (barre))
				print("\n")

				#print("years_after_full:" + str(years_after_full))
				#print("years_ago:" + str(years_ago))
				#print("years_after:" + str(years_after))
				#print("d0Year" + str(d0Year))
				#print("d0Month" + str(d0Month))
				#print("d0Day" + str(d0Day))
				#print("d0:" + str(d0))
				#print("d1:" + str(d3))
				#print("d3:" + str(d3))
				#print("new:" + str(new))
				#print("ValuePercent" + str(ValuePercent))
def Venus():
	years_ago_full = datetime.now() - timedelta(days = 1 * 365)
	years_ago_full = str(years_ago_full)
	years_ago = years_ago_full[:4]
	years_ago = int(years_ago)

	years_after_full = datetime.now() + timedelta(days = 1 * 365)
	years_after_full = str(years_after_full)
	years_after = years_after_full[:4]
	years_after = int(years_after)

	with open("/var/www/html/Orbit.json","r") as O:
		orbit = json.load(O)
		thisYear = orbit["Venus"]

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days = 1)
			if ( d0 >= d1 - timedelta(days = 225) and d0 <= d1):
				Procentaj.VenusPerihelion = d0

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days = 1)
			if (d0 <= d1 + timedelta(days = 225) and d0 >= d1):
				Procentaj.NewVenusPerihelion = d0
				d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
				d3 = Procentaj.NewVenusPerihelion - Procentaj.VenusPerihelion
				d3 = str(d3)
				d3 = d3.split()
				d3 = int(d3[0])
				d3 = d3 +1
				ValuePercent = d3 / 100
				delta = d1 - Procentaj.VenusPerihelion
				delta = str(delta)
				delta = delta.split()
				delta = delta[0]
				new = re.sub("[^0-9]", "", str(delta))
				new = str(new)
				new = new[:6]
				new = int(new)
				Procentaj.VenusResult = new / ValuePercent
				Procentaj.VenusResult = round(Procentaj.VenusResult, 2)
				print("<Planeta> : </Venus>")
				print(("Ziua din an: ") + str("ziua ") + str(new))
				print(("Progresul planetei Venus pana la completarea orbitei:") + str(Procentaj.VenusResult) + str("%"))

				procentaj = Procentaj.VenusResult
				barre = (
					"["
					+ "#" * int((50 / 100) * procentaj)
					+ "-" * int((50 / 100) * (100 - procentaj))
					+ "]"
				)

				print("Procentajul anului:" + (barre))
				print("\n")
				#print("years_after_full:" + str(years_after_full))
				#print("years_ago:" + str(years_ago))
				#print("years_after:" + str(years_after))
				#print("d0Year" + str(d0Year))
				#print("d0Month" + str(d0Month))
				#print("d0Day" + str(d0Day))
				#print("d0:" + str(d0))
				#print("d1:" + str(d3))
				#print("d3:" + str(d3))
				#print("new:" + str(new))
				#print("ValuePercent" + str(ValuePercent))
def Jupiter():
	years_ago_full = datetime.now() - timedelta(days=1 * 365)
	years_ago_full = str(years_ago_full)
	years_ago = years_ago_full[:4]
	years_ago = int(years_ago)

	years_after_full = datetime.now() + timedelta(days=1 * 365)
	years_after_full = str(years_after_full)
	years_after = years_after_full[:4]
	years_after = int(years_after)

	with open("/var/www/html/Orbit.json", "r") as O:
		orbit = json.load(O)
		thisYear = orbit["Jupiter"]
		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days = 1)
			if(d0 >= d1 - timedelta(days = 4382) and d0 <= d1):
				Procentaj.JupiterPerihelion = d0

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days = 1)
			if (d0 <= d1 + timedelta(days = 4382) and d0 >= d1):
				Procentaj.NewJupiterPerihelion = d0
				d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
				d3 = Procentaj.NewJupiterPerihelion - Procentaj.JupiterPerihelion
				d3 = str(d3)
				d3 = d3.split()
				d3 = int(d3[0])
				d3 = d3 + 1
				ValuePercent = d3 / 100
				delta = d1 - Procentaj.JupiterPerihelion
				delta = str(delta)
				delta = delta.split()
				delta = delta[0]
				new = re.sub("[^0-9]", "", str(delta))
				new = str(new)
				new = new[:6]
				new = int(new)
				Procentaj.JupiterResult = new / ValuePercent
				Procentaj.JupiterResult = round(Procentaj.JupiterResult, 2)

				print("<Planeta> : </Jupiter>")
				print(("Ziua: ") + str("ziua ") + str(new))
				print(("Progresul planetei Jupiter pana la completarea orbitei:") + str(Procentaj.JupiterResult) + str("%"))
				procentaj = Procentaj.JupiterResult
				barre = (
					"["
					+ "#" * int((50 / 100) * procentaj)
					+ "-" * int((50 / 100) * (100 - procentaj))
					+ "]"
				)
				print("Procentul anului:" + (barre))
				print("\n")

				#print("years_after_full:" + str(years_after_full))
				#print("years_ago:" + str(years_ago))
				#print("years_after:" + str(years_after))
				#print("d0Year" + str(d0Year))
				#print("d0Month" + str(d0Month))
				#print("d0Day" + str(d0Day))
				#print("d0:" + str(d0))
				#print("d1:" + str(d3))
				#print("d3:" + str(d3))
				#print("new:" + str(new))
				#print("ValuePercent" + str(ValuePercent))


def Tesla():
	years_ago_full = datetime.now() - timedelta(days=1 * 365)  # adapt to the number of years
	years_ago_full = str(years_ago_full)
	years_ago = years_ago_full[:4]
	years_ago = int(years_ago)  # result

	# Next rotation year
	years_after_full = datetime.now() + timedelta(days=1 * 365)  # adapt to the number of years
	years_after_full = str(years_after_full)
	years_after = years_after_full[:4]
	years_after = int(years_after)  # result

	with open("/var/www/html/Orbit.json", "r") as O:
		orbit = json.load(O)
		thisYear = orbit["Tesla"]  # This year
		# years_ago = orbit["Tesla"][str(years_ago)][-1]
		# years_after = orbit["Tesla"][str(years_after)][0]
		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days=1)
			if (d0 >= d1 - timedelta(days=568) and d0 <= d1):
				Procentaj.TeslaPerihelion = d0

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days=1)
			if (d0 <= d1 + timedelta(days=568) and d0 >= d1):
				Procentaj.NewTeslaPerihelion = d0
				d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
				d3 = Procentaj.NewTeslaPerihelion - Procentaj.TeslaPerihelion
				d3 = str(d3)
				d3 = d3.split()
				d3 = int(d3[0])
				d3 = d3 + 1
				ValuePercent = d3 / 100
				delta = d1 - Procentaj.TeslaPerihelion
				delta = str(delta)
				delta = delta.split()
				delta = delta[0]
				new = re.sub("[^0-9]", "", str(delta))
				new = str(new)
				new = new[:6]#:4
				new = int(new)
				Procentaj.TeslaResult = new / ValuePercent
				Procentaj.TeslaResult = round(Procentaj.TeslaResult, 2)

				# Add graph progress #####

				print("<Statie>: </Starman>")
				print(("Ziua: ") + str("ziua ") + str(new))
				print(("Progresul statiei Starman pana la completarea orbitei: ") + str(Procentaj.TeslaResult) + str("%"))

				percent = Procentaj.TeslaResult
				barre = (
				    "["
				    + "#" * int((50 / 100) * percent)
				    + "-" * int((50 / 100) * (100 - percent))
				    + "]"
				)
				print("Procentajul anului : " + (barre))
				print("\n")

				#print("years_after_full:" + str(years_after_full))
				#print("years_ago:" + str(years_ago))
				#print("years_after:" + str(years_after))
				#print("d0Year" + str(d0Year))
				#print("d0Month" + str(d0Month))
				#print("d0Day" + str(d0Day))
				#print("d0:" + str(d0))
				#print("d1:" + str(d3))
				#print("d3:" + str(d3))
				#print("new:" + str(new))
				#print("ValuePercent" + str(ValuePercent))



def Saturn():
	years_ago_full = datetime.now() - timedelta(days = 1 * 365)
	years_ago_full = str(years_ago_full)

	years_ago = years_ago_full[:4]
	yeas_ago = int(years_ago)

	years_after_full = datetime.now() + timedelta(days = 1* 365)
	years_after_full = str(years_after_full)

	years_after = years_after_full[:4]
	years_after = int(years_after)

	with open("/var/www/html/Orbit.json", "r") as O:
		orbit = json.load(O)
		thisYear = orbit["Saturn"]

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days = 1)
			if (d0 >= d1 - timedelta(days = 10585) and d0 <= d1):
				Procentaj.SaturnPerihelion = d0

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d1 = d1 + timedelta(days = 1)
			if(d0 <= d1 + timedelta(days = 10585) and d0 >= d1):
				Procentaj.NewSaturnPerihelion = d0
				d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
				d3 = Procentaj.NewSaturnPerihelion - Procentaj.SaturnPerihelion
				d3 = str(d3)
				d3 = d3.split()
				d3 = int(d3[0])
				d3 = d3 + 1
				ValuePercent = d3 / 100
				delta = d1 - Procentaj.SaturnPerihelion
				delta = str(delta)
				delta = delta.split()
				delta = delta[0]
				new = re.sub("[^0-9]", "", str(delta))
				new = str(new)
				new = new[:6]
				new = int(new)
				Procentaj.SaturnResult = new / ValuePercent
				Procentaj.SaturnResult = round(Procentaj.SaturnResult, 2)

	print("<Planeta> : </Saturn>")
	print(("Ziua din an:") + str("ziua ") + str(new))
	print(("Progresul planetei Saturn pana la completarea orbitei:") + str(Procentaj.SaturnResult) + str("%"))

	procentaj = Procentaj.SaturnResult
	barre = (
		"["
		+ "#" * int((50 / 100) * procentaj)
		+ "-" * int((50 / 100) * (100 - procentaj))
		+ "]"
	)
	print("Procentajul anului: " + (barre))
	print("\n")

	#print("years_after_full:" + str(years_after_full))
	#print("years_ago:" + str(years_ago))
	#print("years_after:" + str(years_after))
	#print("d0Year" + str(d0Year))
	#print("d0Month" + str(d0Month))
	#print("d0Day" + str(d0Day))
	#print("d0:" + str(d0))
	#print("d1:" + str(d3))
	#print("d3:" + str(d3))
	#print("new:" + str(new))
	#print("ValuePercent" + str(ValuePercent))
def Uranus():
	years_ago_full = datetime.now() - timedelta(days = 1 * 365)
	years_ago_full = str(years_ago_full)

	years_ago = years_ago_full[:4]
	years_ago = int(years_ago)

	years_after_full = datetime.now() + timedelta(days =  1* 365)
	years_after_full = str(years_after_full)
	years_after = years_after_full[:4]
	years_after = int(years_after)

	with open("/var/www/html/Orbit.json", "r") as O:
		orbit = json.load(O)
		thisYear = orbit["Uranus"]

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days = 1)
			if (d0 >= d1 - timedelta(days = 30680) and d0 <= d1):
				Procentaj.UranusPerihelion = d0

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
			d1 = d1 + timedelta(days = 1)
			if (d0 <= d1 + timedelta(days = 30680) and d0 >= d1):
				Procentaj.NewUranusPerihelion = d0
				d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
				d3 = Procentaj.NewUranusPerihelion - Procentaj.UranusPerihelion
				d3 = str(d3)
				d3 = d3.split()
				d3 = int(d3[0])
				d3 = d3 + 1
				ValuePercent = d3 / 100
				delta = d1 - Procentaj.UranusPerihelion
				delta = str(delta)
				delta = delta.split()
				delta = delta[0]
				new = re.sub("[^0-9]", "", str(delta))
				new = str(new)
				new = new[:6]
				new = int(new)
				Procentaj.UranusResult = new / ValuePercent
				Procentaj.UranusResult = round(Procentaj.UranusResult, 2)
				print("<Planeta> : </Uranus>")
				print(("Ziua din an: ") + str("ziua ") + str(new))
				print(("Progresul planetei Uranus pana la completarea orbitei:") + str(Procentaj.UranusResult) + str("%"))

				procentaj = Procentaj.UranusResult
				barre = (
					"["
					+ "#" * int((50 / 100) * procentaj)
					+ "-" * int((50 / 100) * (100 - procentaj))
					+ "]"
				)

				print("Procentajul anului:" + (barre))
				print("\n")
				#print("years_after_full:" + str(years_after_full))
				#print("years_ago:" + str(years_ago))
				#print("years_after:" + str(years_after))
				#print("d0Year" + str(d0Year))
				#print("d0Month" + str(d0Month))
				#print("d0Day" + str(d0Day))
				#print("d0:" + str(d0))
				#print("d1:" + str(d3))
				#print("d3:" + str(d3))
				#print("new:" + str(new))
				#print("ValuePercent" + str(ValuePercent))
def Pluto():  # d0 = first perihelion , d1 = today , d2 = next perihelion

	years_ago_full = datetime.now() - timedelta(days=1 * 365)  # adapt to the number of years
	years_ago_full = str(years_ago_full)
	years_ago = years_ago_full[:4]
	years_ago = int(years_ago)  # result

	years_after_full = datetime.now() + timedelta(days=1 * 365)  # adapt to the number of years
	years_after_full = str(years_after_full)
	years_after = years_after_full[:4]
	years_after = int(years_after)  # result

	with open("/var/www/html/Orbit.json", "r") as O:
		orbit = json.load(O)
		thisYear = orbit["Pluto"]
		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
			d1 = d1 + timedelta(days=1)
			if (d0 >= d1 - timedelta(days=90580) and d0 <= d1):  # i is bigger or equal today - 30 days and smaller or equal today : First day of rotation
				Percentage.PlutoPerihelion = d0

		for i in thisYear:
			d0Year = i[:4]
			d0Year = int(d0Year)
			d0Month = i[5:7]
			d0Month = int(d0Month)
			d0Day = i[8:10]
			d0Day = int(d0Day)
			d0 = date(d0Year, d0Month, d0Day)
			d1 = date(Percentage.current_year, Percentage.thisMonth, Percentage.today)
			d1 = d1 + timedelta(days=1)
			if (d0 <= d1 + timedelta(days=90580) and d0 >= d1):  # i is smaller or equal today + 30 days and bigger or equalt today : Next Perihelion
				Percentage.NewPlutoPerihelion = d0
				d1 = date(Procentaj.current_year, Procentaj.thisMonth, Procentaj.today)
				d3 = Procentaj.NewPlutoPerihelion - Procentaj.PlutoPerihelion
				d3 = str(d3)
				d3 = d3.split()
				d3 = int(d3[0])
				d3 = d3 + 1
				ValuePercent = d3 / 100
				delta = d1 - Procentaj.PlutoPerihelion
				delta = str(delta)
				delta = delta.split()
				delta = delta[0]
				new = re.sub("[^0-9]", "", str(delta))
				new = str(new)
				new = new[:6]#:4
				new = int(new)
				Procentaj.PlutoResult = new / ValuePercent
				Procentaj.PlutoResult = round(Procentaj.PlutoResult, 2)


				print("<Planeta> : </Pluto>")
				print(("Ziua :") + str("ziua") + str(new))
				print(("Progresul planetei Uranus pana la completarea orbitei: : ") + str(Procentaj.PlutoResult) + str("%"))

				percent = Procentaj.PlutoResult
				barre = (
				    "["
				    + "#" * int((50 / 100) * percent)
				    + "-" * int((50 / 100) * (100 - percent))
				    + "]"
				)
				print("Procentajul anului: " + (barre))
				print("\n")


#motd()
def timp_pamant(year, month, day, hour):
	return 367 * year- 7 * (year + (month + 9)/ 12) / 4 + 275 * month / 9 + day - 730530 + float(hour)/float(24)

timp = datetime.utcnow()
d = timp_pamant(timp.year, timp.month, timp.day, timp.hour)
def get_planet(nume, d):

	if nume == "Soare":
		return {
			'N': math.radians(0.0),#N - longitudinea nodului ascendent
			'i' : math.radians(0.0),#i - Înclinarea către ecliptică (planul orbitei Pământului)
			'w' : math.radians(282.9404 + 4.70935E-05 * d),#w - argumentul periheliu
			'a' : 1.000000,#a - semi-majore axă, sau distanța medie de la soare
			'e' : 0.016709 - 1.151E-9 * d, #e - excentricitate (0 = cerc, 0-1 = elipsă, 1 = parabola)
			'M' : math.radians(356.0470 + 0.9856002585 * d)#M - anomalie normala
	}
	elif nume == 'Mercur':
		return {
			'N': math.radians(48.3313 + 3.24587E-5 * d),
			'i' :  math.radians(7.0047 + 5.00E-8 * d),
			'w' : math.radians(29.1241 + 1.01444E-5 * d),
			'a' : 0.387098,
			'e' : 0.205635 + 5.59E-10 * d,
			'M' : math.radians(168.6562 + 4.0923344368 * d)
	}
	elif nume == 'Venus':
		return {
			'N' : math.radians(76.6799 + 2.46590E-5 * d),
			'i' : math.radians(3.3946 + 2.75E-8 * d),
			'w' : math.radians(54.8910 + 1.38374E-5 * d),
			'a' : 0.723330,
			'e' : 0.006773 - 1.302E-9 * d,
			'M' : math.radians(48.0052 + 1.6021302244 * d)
	}
	elif nume == 'Marte':
		return {
			'N': math.radians(49.5574 + 2.11081E-5 * d),
			'i' : math.radians(1.8497 - 1.78E-8 * d),
			'w' : math.radians(286.5016 + 2.92961E-5 * d),
			'a' : 1.523688,
			'e' : 0.093405 + 2.516E-9 * d,
			'M' : math.radians(18.6021 + 0.5240207766 * d)
		}
	elif nume == 'Jupiter':
		return {
			'N': math.radians(100.4542 + 2.76854E-5 * d),
			'i' : math.radians(1.3030 - 1.557E-7 * d),
			'w' : math.radians(273.8777 + 1.64505E-5 * d),
			'a' : 5.20256,
			'e' : 0.048498 + 4.469E-9 * d,
			'M' : math.radians(19.8950 + 0.0830853001 * d)
		}

	elif nume == 'Saturn':
		return {
			'N': math.radians(113.6634 + 2.38980E-5 * d),
			'i' : math.radians(2.4886 - 1.081E-7 * d),
			'w' : math.radians(339.3939 + 2.97661E-5 * d),
			'a' : 9.55475,
			'e' : 0.055546 - 9.499E-9 * d,
			'M' : math.radians(316.9670 + 0.0334442282 * d)
		}
	elif nume == 'Uranus':
		return {
			'N': math.radians(74.0005 + 1.3978E-5 * d),
			'i' : math.radians( 0.7733 + 1.9E-8 * d),
			'w' : math.radians(96.6612 + 3.0565E-5 * d),
			'a' : 19.18171 - 1.55E-8 * d,
			'e' : 0.047318 + 7.45E-9 * d,
			'M' : math.radians(142.5905 + 0.011725806 * d)
		}
	elif nume == 'Neptun':
		return {
			'N': math.radians(131.7806 + 3.0173E-5 * d),
			'i' : math.radians(1.7700 - 2.55E-7 * d),
			'w' : math.radians(272.8461 - 6.027E-6 * d),
			'a' : 30.05826 + 3.313E-8 * d,
			'e' : 0.008606 + 2.15E-9 * d,
			'M' : math.radians(260.2471 + 0.005995147 * d)
		}

	elif nume == 'Luna':
		return {
			'N' : math.radians(384400 * d),
			'i' : math.radians(5.16),
			'w' : math.radians(318.15 * d),
			'a' : (60.2666),
			'e' : (0.054900),
			'M' : math.radians(135.27)
			}



def elemente_orbitale(nume_planeta, d):

	planet = get_planet(nume_planeta, d)

	N = planet.get('N')
	i = planet.get('i')
	w = planet.get('w')
	a = planet.get('a')
	e = planet.get('e')
	M = planet.get('M')

	E = M + e* math.sin(M) * ( 1.0 + e * math.cos(M) )

	xv =  a * ( math.cos(E) - e )#}Distanța de la soare și adevărata sa anomalie v
	yv =  a * ( math.sqrt(1.0 - e*e) * math.sin(E) )

	v = math.atan2( yv, xv )
	r = math.sqrt( xv*xv + yv*yv )

	xh = r * ( math.cos(N) * math.cos(v+w) - math.sin(N) * math.sin(v+w) * math.cos(i) )#Pozitia planetelor in spatiul cu 3 dimensiuni
	yh = r * ( math.sin(N) * math.cos(v+w) + math.cos(N) * math.sin(v+w) * math.cos(i) )
	zh = r * ( math.sin(v+w) * math.sin(i) )

	lonecl = math.atan2( yh, xh ) #longitudinea ecliptică și latitudinea eliptica
	latecl = math.atan2( zh, math.sqrt(xh*xh+yh*yh) )

	return {
		'r' : r,
		'v' : v,
		'xh' : xh,
		'yh' : yh,
		'w'  :w,
		'lonecl' : lonecl,
		'latecl ': latecl
	}

def alinieri_geocentrice(nume_planeta, d):
	soare = elemente_orbitale('Soare', d)
	planeta = elemente_orbitale(nume_planeta, d)

	lon_soare = soare.get('v') + soare.get('w')

	xs = soare.get('r') * math.cos(lon_soare)
	ys = soare.get('r') * math.sin(lon_soare)

	xh = planeta.get('xh')
	yh = planeta.get('yh')

	xg = xh + xs
	yg = yh + ys

	grade_heliocentrice = math.degrees(math.atan2(xh, yh))
	grade_geocentrice = math.degrees(math.atan2(xg, yg))

	#print(grade_heliocentrice)
	#print(grade_geocentrice)

	grade_heliocentrice = 90 - grade_heliocentrice
	grade_geocentrice = 90 - grade_geocentrice

	if grade_heliocentrice < 0:
		grade_heliocentrice = grade_heliocentrice + 360

	if grade_geocentrice < 0:
		grade_geocentrice = grade_geocentrice + 360

	return grade_geocentrice

def Neptun_planeta():
	print("Neptun:" + str(float(alinieri_geocentrice('Neptun', d))))

def Soare_stea():
	print("Soare:" + str(float(alinieri_geocentrice('Soare', d))))

def Uranus_planeta():
	print("Uranus:" + str(float(alinieri_geocentrice('Uranus', d))))

def Saturn_planeta():
	print("Saturn:" + str(float(alinieri_geocentrice('Saturn', d))))

def Jupiter_planeta():
	print("Jupiter:" + str(float(alinieri_geocentrice('Jupiter', d))))

def Marte_planeta():
	print("Marte:" + str(float(alinieri_geocentrice('Marte', d))))

def Venus_planea():
	print("Venus:" + str(float(alinieri_geocentrice('Venus', d))))

def Mercur_planeta():
	print("Mercur:" + str(float(alinieri_geocentrice('Mercur', d))))

def Luna_satelit():
	print("Luna:" + str(float(alinieri_geocentrice('Luna', d)) - 7))

text = "Salut si bine te-am gasit in aventura noastra spatiala,eu sunt Edmo si am sa iti ofer informatii despre Calea Lactee" + "\n"
for x in text:
	print(x, end = '')
	sys.stdout.flush()
	time.sleep(0.1)

text = "Inainte de toate, pot sa iti ofer un 'Stiati ca?' al zilei sau vrei sa afli informatii despre planetele din sistemul solar?" + "\n"
for x in text:
	print(x, end = '')
	sys.stdout.flush()
	time.sleep(0.1)
raspuns = str(input("DA/NU:"))

if (raspuns == "DA"):
	stiati_ca_serie = ['Pamantul are nevoie nu de 365 de zile pentru a face o rotatie completa in jurul soarelui, ci de 365 de zile si 6 ore, deci nu sarbatorim mai bine Anul Nou la ora 6 dimineata de 1 ianuarie?', 'Planeta Marte are o masa de 6.39 * 10 la puterea 23 de kg, nici cat greutatea Planetei Pamant, dar ea are mai multi sateliti naturali, in numar de doi , numindu-se Phobos si Deimos?', 'Planeta Saturn este a sasea planeta de la Soare si una dintre cele 5 planete pe care le poti vedea cu ochiul liber, noaptea?']
	elementul_ales = random.choice(stiati_ca_serie)
	text = "Stiati ca:" + str(elementul_ales) + "\n"
	for x in text:
		print(x, end = '')
		sys.stdout.flush()
		time.sleep(0.1)

	text = "Acum vom trece la informatii!"
	for x in text:
		print(x, end = '')
		sys.stdout.flush()
		time.sleep(0.1)
	text = "Iti voi oferi optiuni, tu le vei selecta cu ajutorul numerelor de la 1 la 10 si eu ti-oi oferi cat ai spune Saturn" + "\n"
	for x in text:
		print(x, end = '')
		sys.stdout.flush()
		time.sleep(0.1)

	text = "Esti gata pentru excursia noastra spatiala?"
	for x in text:
		print(x, end = '')
		sys.stdout.flush()
		time.sleep(0.1)
	raspuns = str(input("DA/NU"))
	while raspuns == "DA":
		print("1) Pamant si Luna")
		print("2) Marte")
		print("3) Saturn")
		print("4) Venus")
		print("5) Uranus")
		print("6) Pluto(Planeta pitica)")
		print("7) Haumea(Planeta pitica)")
		print("8) Jupiter")
		print("9) Naveta Starman(Tesla)")
		print("10) Mercur")
		print("11) Neptun")
		print("12) Statia Spatiala Internationala")

		raspuns2 = int(input("Despre ce planeta doresti sa afli informatii?Selecteaza optiunile dorite cu ajutorul numerelor indicate:"))
		print("Ai ales varianta:" + str(raspuns2))

		def unu():
			text = "[INFO]:Pamantul este a treia planeta de la Soare"
			for x in text:
				print(x, end = '')
				sys.stdout.flush()
				time.sleep(0.1)
			Pamant()

			text = "Iti voi prezenta acum informatii despre Luna, satelitul nostru natural"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)
			Luna()
			Luna_satelit()

		def doi():
			text = "[INFO]:Marte este a patra planeta de la Soare"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Marte()

			text = "Fiecare planeta are o aliniere geocentrica, chiar si Marte\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Marte_planeta()

		def trei():
			text = "[INFO]:Saturn este a sasea planeta de la Soare\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Saturn()

			text = "Fiecare planeta are o aliniere geocentrica, chiar si Saturn\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Saturn_planeta()


		def patru():
			text = "[INFO]:Venus, este a patra planeta de la Soare\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Venus()

			text = "Fiecare planeta are o aliniere geocentrica, chiar si Venus\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Venus_planea()

		def cinci():
			text = "[INFO]:Uranus e a saptea planeta de la Soare\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Uranus()

			text = "Fiecare planeta are o aliniere geometrica, chiar si Uranus\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Uranus_planeta()

		def sase():
			text = "Pluto este a 10-a planeta de la Soare\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Pluto()
			'''
			text = "Fiecare planeta are o aliniere geometrica, chiar si Pluto"
			for x in text:
				print("\033[1;30;", x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Planete.Marte_planeta()
			'''

		def sapte():
			text = "Haumae este a 11-a planeta, si a 3-a planeta pitica din sistemul nostru solar\n"
			for x in text:
				print("\033[1;30;", x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Haumae()
			'''
			text = "Fiecare planeta are o aliniere geometrica, chiar si Haumea"
			for x in text:
				print("\033[1;30;", x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Planete.Marte_planeta()
			'''

		def opt():
			text = "Jupiter este a cincea planeta din sistemul nostru solar\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Jupiter()

			text = "Fiecare planeta are o aliniere geometrica, chiar si Jupiter\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Jupiter_planeta()
		def noua():
			text = "Starman, statia lansata de SpaceX in februarie 2018\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Tesla()

		def zece():
			text = "Mercur este prima planeta de la Soare\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Mercury()

			text = "Fiecare planeta are o aliniere geometrica, chiar si Mercur \n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Mercur_planeta()

		def unspe():
			text = "Neptun este ultima pplaneta de la Soare \n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Neptun()

			text = "Fiecare planeta are o aliniere geometrica, chiar si Marte \n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Neptun_planeta()

		def doisprezece():
			text = "SSI , Statia Spatiala Internationala a fost lansata in 1992 de catre NASA si pusa in functiune in 2000 \n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			ISS2()

			text = "Iti voi arata din punct de vedere latitudinal si longitudinal, pozitia ISS-ului:"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
			response = urllib.request.urlopen(req)

			obj = json.loads(response.read())
			print(obj['timestamp'])
			print(obj['iss_position']['latitude'], obj['iss_position']['longitude'])


		if raspuns2 == 1:
			unu()
		if raspuns2 == 2:
			doi()
		if raspuns2 == 3:
			trei()
		if raspuns2 == 4:
			patru()
		if raspuns2 == 5:
			cinci()
		if raspuns2 == 6:
			sase()
		if raspuns2 == 7:
			sapte()
		if raspuns2 == 8:
			opt()
		if raspuns2 == 9:
			noua()
		if raspuns2 == 10:
			zece()
		if raspuns2 == 11:
			unspe()
		if raspuns2 == 12:
			doisprezece()


		text = "Mai vrei sa afli informatii despre sistemul solar?"
		for x in text:
			print(x, end = '')
			sys.stdout.flush()
			time.sleep(0.1)
		raspuns = str(input("DA/NU"))

else:
	text = "Am inteles, iti voi oferi optiuni, tu le vei selecta cu ajutorul numerelor de la 1 la 10 si eu ti-oi oferi cat ai spune Saturn \n"
	for x in text:
		print(x, end = '')
		sys.stdout.flush()
		time.sleep(0.1)

	print("1) Pamant si Luna")
	print("2) Marte")
	print("3) Saturn")
	print("4) Venus")
	print("5) Uranus")
	print("6) Pluto(Planeta pitica)")
	print("7) Haumea(Planeta pitica)")
	print("8) Jupiter")
	print("9) Naveta Starman(Tesla)")
	print("10) Mercur")
	print("11) Neptun")
	print("12) Statia Spatiala Internationala")

	raspuns2 = int(input("Despre ce planeta doresti sa afli informatii?Selecteaza optiunile dorite cu ajutorul numerelor indicate."))
	print("Ai ales varianta:" + str(raspuns2))
	text = "Esti gata pentru excursia noastra spatiala?"
	for x in text:
		print(x, end = '')
		sys.stdout.flush()
		time.sleep(0.1)
	raspuns = str(input("DA/NU"))
	while raspuns == "DA":
		print("1) Pamant si Luna")
		print("2) Marte")
		print("3) Saturn")
		print("4) Venus")
		print("5) Uranus")
		print("6) Pluto(Planeta pitica)")
		print("7) Haumea(Planeta pitica)")
		print("8) Jupiter")
		print("9) Naveta Starman(Tesla)")
		print("10) Mercur")
		print("11) Neptun")
		print("12) Statia Spatiala Internationala")

		raspuns2 = int(input("Despre ce planeta doresti sa afli informatii?Selecteaza optiunile dorite cu ajutorul numerelor indicate:"))
		print("Ai ales varianta:" + str(raspuns2))

		def unu():
			text = "[INFO]:Pamantul este a treia planeta de la Soare"
			for x in text:
				print(x, end = '')
				sys.stdout.flush()
				time.sleep(0.1)
			Pamant()

			text = "Iti voi prezenta acum informatii despre Luna, satelitul nostru natural"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)
			Luna()
			Luna_satelit()

		def doi():
			text = "[INFO]:Marte este a patra planeta de la Soare"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Marte()

			text = "Fiecare planeta are o aliniere geocentrica, chiar si Marte\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Marte_planeta()

		def trei():
			text = "[INFO]:Saturn este a sasea planeta de la Soare\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Saturn()

			text = "Fiecare planeta are o aliniere geocentrica, chiar si Saturn\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Saturn_planeta()


		def patru():
			text = "[INFO]:Venus, este a patra planeta de la Soare\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Venus()

			text = "Fiecare planeta are o aliniere geocentrica, chiar si Venus\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Venus_planea()

		def cinci():
			text = "[INFO]:Uranus e a saptea planeta de la Soare\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Uranus()

			text = "Fiecare planeta are o aliniere geometrica, chiar si Uranus\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Uranus_planeta()

		def sase():
			text = "Pluto este a 10-a planeta de la Soare\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Pluto()
			'''
			text = "Fiecare planeta are o aliniere geometrica, chiar si Pluto"
			for x in text:
				print("\033[1;30;", x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Planete.Marte_planeta()
			'''

		def sapte():
			text = "Haumae este a 11-a planeta, si a 3-a planeta pitica din sistemul nostru solar\n"
			for x in text:
				print("\033[1;30;", x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Haumae()
			'''
			text = "Fiecare planeta are o aliniere geometrica, chiar si Haumea"
			for x in text:
				print("\033[1;30;", x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Planete.Marte_planeta()
			'''

		def opt():
			text = "Jupiter este a cincea planeta din sistemul nostru solar\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Jupiter()

			text = "Fiecare planeta are o aliniere geometrica, chiar si Jupiter\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Jupiter_planeta()
		def noua():
			text = "Starman, statia lansata de SpaceX in februarie 2018\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Tesla()

		def zece():
			text = "Mercur este prima planeta de la Soare\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Mercury()

			text = "Fiecare planeta are o aliniere geometrica, chiar si Mercur \n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Mercur_planeta()

		def unspe():
			text = "Neptun este ultima pplaneta de la Soare \n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Neptun()

			text = "Fiecare planeta are o aliniere geometrica, chiar si Marte \n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			Neptun_planeta()

		def doisprezece():
			text = "SSI , Statia Spatiala Internationala a fost lansata in 1992 de catre NASA si pusa in functiune in 2000 \n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			ISS2()

			text = "Iti voi arata din punct de vedere latitudinal si longitudinal, pozitia ISS-ului:\n"
			for x in text:
				print(x , end = '')
				sys.stdout.flush()
				time.sleep(0.1)

			req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
			response = urllib.request.urlopen(req)

			obj = json.loads(response.read())
			print(obj['timestamp'])
			print(obj['iss_position']['latitude'], obj['iss_position']['longitude'])

if raspuns2 == "NU":
	text = "Atunci ne vom revedea intr-o alta excursie planetara\n"
	for x in text:
		print(x ,end='')
		sys = stdout.flush()
		time.sleep(0.1)


if raspuns2 == 1:
	unu()
if raspuns2 == 2:
	doi()
if raspuns2 == 3:
	trei()
if raspuns2 == 4:
	patru()
if raspuns2 == 5:
	cinci()
if raspuns2 == 6:
	sase()
if raspuns2 == 7:
	sapte()
if raspuns2 == 8:
	opt()
if raspuns2 == 9:
	noua()
if raspuns2 == 10:
	zece()
if raspuns2 == 11:
	unspe()
if raspuns2 == 12:
	doisprezece()
