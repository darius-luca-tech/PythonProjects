#coding=utf-8

import math, itertools, sys, datetime 
__autor__ = 'GAL1LE0'


def timp_pamant(year, month, day, hour): 
	return 367 * year- 7 * (year + (month + 9)/ 12) / 4 + 275 * month / 9 + day - 730530 + float(hour)/float(24) 

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
			'N' : math.radians(125.1228 - 0.05295338083 *d), 
			'i' : math.radians(5.1453), 
			'w' : math.radians(318.0634 + 0.1643573223 * d), 
			'a' : (60.2666),
			'e' : (0.054900), 
			'M' : math.radians(115.3654 + 13.0649929509 * d)  
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

def verificare(aliniari): 
	timp = datetime.datetime.utcnow()  
	d = timp_pamant(timp.year, timp.month, timp.day, timp.hour) 
	for unghi, grup in itertools.groupby(aliniari, lambda x: x[1]): 
		planete = list(map(lambda x: x[0], grup))  
		
		if len(planete) > 0: 
			print("Asezarea geocentrica a planetelor(valori de tip float):\n" )
			print("Neptun:" + str(float(alinieri_geocentrice('Neptun', d)))) 
			print("Soare:" + str(float(alinieri_geocentrice('Soare', d)))) 
			print("Uranus:" + str(float(alinieri_geocentrice('Uranus', d)))) 
			print("Saturn:" + str(float(alinieri_geocentrice('Saturn', d)))) 
			print("Jupiter:" + str(float(alinieri_geocentrice('Jupiter', d)))) 
			print("Marte:" + str(float(alinieri_geocentrice('Marte', d)))) 
			print("Venus:" + str(float(alinieri_geocentrice('Venus', d)))) 
			print("Mercur:" + str(float(alinieri_geocentrice('Mercur', d))))  
			print("Luna" + str(float(alinieri_geocentrice('Luna' , d))))
			print("Asezarea geocentrica a planetelor(valori rotunjite):\n" )
			print("Neptun:" + str(round(alinieri_geocentrice('Neptun', d)))) 
			print("Soare:" + str(round(alinieri_geocentrice('Soare', d)))) 
			print("Uranus:" + str(round(alinieri_geocentrice('Uranus', d)))) 
			print("Saturn:" + str(round(alinieri_geocentrice('Saturn', d)))) 
			print("Jupiter:" + str(round(alinieri_geocentrice('Jupiter', d)))) 
			print("Marte:" + str(round(alinieri_geocentrice('Marte', d)))) 
			print("Venus:" + str(round(alinieri_geocentrice('Venus', d)))) 
			print("Mercur:" + str(round(alinieri_geocentrice('Mercur', d)))) 
			sys.exit(1) 

def main(): 
	timp = datetime.datetime.utcnow()  
	d = timp_pamant(timp.year, timp.month, timp.day, timp.hour) 

	sir_planete = ['Soare', 'Mercur', 'Venus', 'Marte', 'Jupiter', 'Saturn', 'Uranus', 'Neptun'] 

	aliniari = list(map(lambda x: [x, round(alinieri_geocentrice(x, d))], sir_planete)) 
	aliniari.sort(key = lambda x: x[1]) 

	verificare(aliniari) 

main()
