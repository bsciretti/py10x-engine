import math, sys, re
A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
M = 0
R = 0
#p652
K = 0
N = 0
temp = 0
debugis = 0
elabvar = 1
line = 0
y = 0
memload = 0
lngt = 0

def reset():
	global A,B,C,D,E,F,M,R,temp, K, N, line, y, memload, lngt
	A=B=C=D=E=F=M=R=temp=K=N=line=y=memload=lngt = 0
	p101()

try:
	aj = sys.argv[1]
	if aj == "debug":
		debugis = 1
except:
	print ""

#parser del registro
def regpars(dent):
	global A,B,C,D,E,F,M,R,temp, K, N
	if "A" in dent:
		return "A"
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
	if "K" in dent:
		return "K"
	if "N" in dent:
		return "N"
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
	global A,B,C,D,E,F,M,R,temp, K, N, elabvar, line, y
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
	global A,B,C,D,E,F,M,R,temp, K, N
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
	if "v" in dent:
		return "v"
	if "^" in dent:
		return "^"
	if "!" in dent:
		return "!"
	if "><" in dent:
		return "><"
	if "*" in dent:
		return "*"
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
	if "/><" in dent:
		return "decpart"
def parse(reg,oper):
	global A,B,C,D,E,F,M,R,temp, K, N, elabvar, line, y
	if oper == "+":
		A = A + eval(reg)
		M = eval(reg)
	if oper == "-":
		A = A - eval(reg)
		M = eval(reg)
	if oper == "x":
		A = A*eval(reg)
		M = eval(reg)
	if oper == ":":
		A = A/eval(reg)
		R = A%eval(reg)
		M = eval(reg)
	if oper == "#":
		print eval(reg)
	if oper == "v":
		A = math.sqrt(eval(reg))
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
		A = eval(reg)
	if oper == "!":
		if "A" in reg:
			A = abs(A)
		else:
			opx = str("%s=M"%reg)
			exec(opx,globals())
	if oper == "><":
		temp = eval(reg)
		opx = "%s = A"%reg
		exec(opx,globals())
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
	dent = raw_input("")
	global A,B,C,D,E,F,M,R,temp, K, N, debugis, elabvar, line, y, memload, lngt
	if debugis == 1:
		print "%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d"%(A,B,C,D,E,F,M,R)
		print "A\tB\tC\tD\tE\tF\tM\tR"
	if "S" in dent:
		M = input(">")
	if "EXIT" in dent:
		exit()
	if "RESET" in dent:
		reset()
	if "memload" in dent:
		a = raw_input("Insert file name: ")
		memload = 1
		with open(a) as fp:  
			line = fp.readlines()
			lngt = len(line)
	if "V" in dent and memload == 1:
		y = 0
		index = re.findall("\d+\.*\d*", str(dent))
		index = str(index[0])
		jump(0,index)
		while y < lngt:
			x = line[y]
			if debugis == 1:
				print "Operation:", x
				print A,B,C,D,E,F,M,R
				print "A,B,C,D,E,F,M,R"
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
					print "Operation:", x
					print A,B,C,D,E,F,M,R
					print "A,B,C,D,E,F,M,R"
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
	oper = ops(dent)
	parse(reg,oper)
	p101()
	
p101()
	
