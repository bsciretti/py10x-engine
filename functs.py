#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math, sys, re
A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
b = 0
c = 0
d = 0
e = 0
f = 0
M = 0
R = 0
temp = 0
debugis = 0
comment = 0
elabvar = 1
line = 0
y = 0
memload = 0
lngt = 0
globalized = ["K0"]
delal = 0
commenti = []
while delal < 100:
	pota = "K"+str(delal)
	globalized.append(pota)
	delal = delal+1
for res in globalized:
	helb = "%s = 0"%res
	exec(helb,globals())

def reset():
	global A,B,C,D,E,F,M,R, b, c, d, e, f, temp, line, y, memload, lngt, globalized
	for uj in globalized:
		helb = "global %s"%uj
		exec(helb)
	for res in globalized:
		helb = "%s = 0"%res
		exec(helb,globals())
	A=B=C=D=E=F=M=Rb=c=d=e=f=temp=line=y=memload=lngt = 0
	p101()

try:
	aj = sys.argv[1]
	if aj == "debug":
		debugis = 1
	if aj == "comment":
		comment = 1
except:
	print ""

#parser del registro
def regpars(dent):
	global A,B,C,D,E,F,M,R, b, c, d, e, f, temp
	for uj in globalized:
		helb = "global %s"%uj
		exec(helb)
	if "A" in dent:
		return "A"
	if "K" in dent:
		m = re.findall("\d+\.*\d*", str(dent))
		n = m[0]
		if int(n) >-1 and int(n) < 100:
			jald = "K"+n
			return jald
	if "B/" in dent:
		return "b"
	if "C/" in dent:
		return "c"
	if "D/" in dent:
		return "d"
	if "E/" in dent:
		return "e"
	if "F/" in dent:
		return "f"
	if "B" in dent:
		return "B"
	if "C" in dent:
		return "C"
	if "D" in dent:
		return "D"
	if "E" in dent:
		return "E"
	if "F" in dent:
		return "F"
	if "M" in dent:
		return "M"
	if "R" in dent:
		return "R"
	if "/#" in dent:
		return "irl"
	if "Vs" in dent: #incondizionato
		index = re.findall("\d+\.*\d*", str(dent))
		index = str(index[0])
		jump(0,index)
	if "Ws" in dent:  #condizionato
		index = re.findall("\d+\.*\d*", str(dent))
		index = str(index[0])
		jump(1,index)

def jump(tipo, index):
	global A,B,C,D,E,F,M,R, b, c, d, e, f, temp, elabvar, line, y
	if tipo == 0:
		tem1 = "V%s\n"%index
		ind = line.index(tem1)
		y = ind
	if tipo == 1:
		if A > 0:
			tem1 = "W%s\n"%index
			ind = line.index(tem1)
			y = ind
		else:
			print ""
def ops(dent):
	global A,B,C,D,E,F,M,R, b, c, d, e, f, temp, globalized
	for uj in globalized:
		helb = "global %s"%uj
		exec(helb)
	if "/+" in dent:
		return "inc"
	if "/-" in dent:
		return "dec"
	if "+" in dent:
		return "+"
	if "-" in dent:
		return "-"
	if "x" in dent:
		return "x"
	if ":" in dent:
		return ":"
	if "#" in dent:
		return "#"
	if "sqrt" in dent:
		return "v"
	if "^" in dent:
		if "/^" in dent:
			return "nodec"
		else:
			return "^"
	if "!" in dent:
		return "!"
	if "><" in dent:
		if "/><" in dent:
			return "decpart"
		else:
			return "><"
	if "*" in dent:
		return "*"
	if "pi" in dent or "π" in dent:
		return "pi"
	if "sin" in dent:
		return "SIN"
	if "cos" in dent:
		return "COS"
	if "tan" in dent:
		return "TAN"
	if "cst" in dent:
		return "cst"
	if "cnst" in dent:
		return "cnst"
	if "arc" in dent:
		return "ARC"
	if "/x" in dent:
		return "%"
def parse(reg,oper):
	global A,B,C,D,E,F,M,R, b, c, d, e, f, temp, elabvar, line, y, globalized
	for uj in globalized:
		helb = "global %s"%uj
		exec(helb)
	if oper == "+":
		A = A + eval(reg)
		M = eval(reg)
	if oper == "-":
		A = A - eval(reg)
		M = eval(reg)
	if oper == "x":
		A = A*eval(reg)
		M = eval(reg)
	if oper == "inc":
		opx = "%s = %s + 1"%(reg,reg)
		exec(opx,globals())
	if oper == "dec":
		opx = "%s = %s - 1"%(reg,reg)
		exec(opx,globals())
	if oper == "pi":
		opx = "%s = math.pi"%(reg)
		exec(opx,globals())		
	if oper == "%":
		temp = M
		A = (A/100)*M
		M = temp
	if oper == ":":
		opx = "A = A/%s"%reg
		exec(opx,globals())	
		opx = "R = int(A)&int(%s)"%reg
		exec(opx,globals())	
		opx = "M = %s"%reg
		exec(opx,globals())	
	if oper == "#":
		print eval(reg)
	if oper == "nodec":
		M = A
		A = int(A)
	if oper == "v":
		A = math.sqrt(abs(eval(reg)))
		M = A*2
	if oper == "cst":
		ll = raw_input("Insert constant:")
		opx = "%s = %s"%(reg,ll)
		exec(opx,globals())
	if oper == "cnst":
		gl = re.findall("\d+\.*\d*", str(elabvar))
		gh = gl[0]
		opx = "%s = %s"%(reg,gh)
		exec(opx,globals())	
	if oper == "^":
		opx = "A = %s"%reg
		exec(opx,globals())	
	if oper == "!":
		opx = str("%s=M"%reg)
		exec(opx,globals())
	if oper == "><":
		if reg == "A":
			A = abs(A)
		else:
			opx = "temp = %s"%reg
			exec(opx,globals())
			#print "Temp:",temp
			opx = "%s = A"%reg
			exec(opx,globals())
			#print "M: ",eval(reg)
			A = temp
	if oper == "decpart":
		temp = int(A)
		M = A - int(A)
	if oper == "*":
		opx = "%s = 0"%reg
		exec(opx,globals())
	if oper == "SIN":
		A = math.sin(eval(reg))
	if oper == "COS":
		A = math.cos(eval(reg))
	if oper == "ARC":
		A = math.arc(eval(reg))
	if oper == "TAN":
		A = math.tan(eval(reg))

def p101():
	#jumps
	regis = ["V","W","Y","Z"]
	orig = ["M","C","D","R"]
	corig = {}
	dest = ["A", "B", "E", "F"]
	cordg = {}
	indis = 0
	indes = 0
	for x in regis:
		indis = 0
		for ga in orig:
			helab = ga+x
			ilab = str("Vs"+str(indes+1))
			corig[helab] = ilab 		 
			helab = dest[indis] + x
			ilab = str("V"+str(indes+1))
			cordg[helab] = ilab 
			indis = indis +1	
			indes = indes + 1	
	orig = ["M/","C/","D/","R/"]
	incorig = {}
	dest = ["A/", "B/", "E/", "F/"]
	incordg = {}
	indis = 0
	indes = 0
	for x in regis:
		indis = 0
		for a in orig:
			helab = ga+x
			ilab = str("Ws"+str(indes+1))
			incorig[helab] = ilab 		 
			helab = dest[indis] + x
			ilab = str("W"+str(indes+1))
			incordg[helab] = ilab 
			indis = indis +1
			indes = indes +1
	dent = raw_input("")
	global A,B,C,D,E,F,M,R, b, c, d, e, f, temp, debugis, elabvar, commenti, line, y, memload, lngt
	if debugis == 1:
		print "%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d"%(A,B,C,D,E,F,M,R)
		print "A\tB\tC\tD\tE\tF\tM\tR"
		print "Splitted"
		print "%d\t%d\t%d\t%d\t%d"%(b,c,d,e,f)
		print "b\tc\td\te\tf"
	if "EXIT" in dent:
		exit()
	if "RESET" in dent:
		reset()
	if "PRINT" in dent and memload == 1:
		for mel in line:
			print mel.rstrip()
	if "S" in dent:
		M = input(">")
	if "memload" in dent:
		a = raw_input("Insert file name: ")
		memload = 1
		with open(a) as fp:  
			line = fp.readlines()
			lngt = len(line)
			for kla in line:
				if "cnst" in kla:
					x = kla.rstrip()
					reg = regpars(x)
					oper = ops(x)
					parse(reg,oper)		
			k = 0
			while k < lngt:
				ba = line[k].rstrip()
				if ba in corig:
					o = corig[ba]
					o = o+"\n"
					line[k] = o	
				if ba in cordg:
					o = cordg[ba]
					o = o+"\n"
					line[k] = o	
				k = k +1
			k = 0
			while k < lngt:
				try:
					load = line[y]
					h = load.split("|")
					line[y] = h[0]+"\n"
					commenti.append(h[1])
					k = k +1
				except (IndexError):
					commenti.append("")
					k = k +1
			k = 0
			while k < lngt:
				ba = line[k].rstrip()
				if ba in incorig:
					o = incorig[ba]
					o = o+"\n"
					line[k] = o	
				if ba in incordg:
					o = incordg[ba]
					o = o+"\n"
					line[k] = o	
				k = k +1
	if "V" in dent and memload == 1:
		y = 0
		index = re.findall("\d+\.*\d*", str(dent))
		index = str(index[0])
		jump(0,index)
		while y < lngt:
			Mp = 0
			load = line[y]
			h = load.split("|")
			x = h[0]
			if debugis == 1:
				print "---------- \n Operation:", x
				print "%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d"%(A,B,C,D,E,F,M,R)
				print "A\tB\tC\tD\tE\tF\tM\tR"
				print "Splitted"
				print "%d\t%d\t%d\t%d\t%d"%(b,c,d,e,f)
				print "b\tc\td\te\tf"
				try:
					print "Comment: " + commenti[y]
				except:
					print "" 
			if comment == 1:
				try:
					print "Comment: " + commenti[y]
				except:
					print "" 
			if "S" in x:
				hel = raw_input(">")
				if hel == "RESET":
					reset()
				elif "V" in hel and memload == 1:
					y = 0
					index = re.findall("\d+\.*\d*", str(dent))
					index = str(index[0])
					jump(0,index)
				elif "PRINT" in hel:
					for mel in line:
						print mel.rstrip()
				else:
					M = eval(hel)
			if "Vs" in dent and memload == 1:
				index = re.findall("\d+\.*\d*", str(dent))
				index = str(index[0])
				print index
				jump(0,index)		
			if "Ws" in dent and memload == 1:
				index = re.findall("\d+\.*\d*", str(dent))
				index = str(index[0])
				print index
				jump(1,index)
			elabvar = x
			x = x.rstrip()
			reg = regpars(x)
			oper = ops(x)
			parse(reg,oper)
			y = y+1
			if y == lngt:
				y = 0
				p101()
	if "open" in dent:
		a = raw_input("Insert file name: ")
		with open(a) as fp:  
			line = fp.readlines()
			g = len(line)
			while y < g:
				x = line[y]
				if debugis == 1:
					print "---------- \n Operation:", x
					print "%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d"%(A,B,C,D,E,F,M,R)
					print "A\tB\tC\tD\tE\tF\tM\tR"
				if "S" in x:
					Mp = raw_input(">")
					if Mp == "RESET":
						reset()
					else:
						M = eval(Mp)
				elabvar = x
				x = x.rstrip()
				reg = regpars(x)
				oper = ops(x)
				parse(reg,oper)
				y = y+1
				if y == g:
					y = 0
					p101()

	if "oldopen" in dent:
		a = raw_input("Inserire nome file: ")
		with open(a) as fp:  
			line = fp.readlines()
			for x in line:
				if "S" in x:
					M = input(">")
				elabvar = x
				x = x.rstrip()
				reg = regpars(x)
				oper = ops(x)
				parse(reg,oper)
	reg = regpars(dent)
	#print reg
	oper = ops(dent)
	#print oper	
	parse(reg,oper)
	p101()
	
p101()
