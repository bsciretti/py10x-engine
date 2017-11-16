import math
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
	if "cos" in dent:
		return "SIN"
	if "cos" in dent:
		return "COS"
	if "tan" in dent:
		return "TAN"
	if "arc" in dent:
		return "ARC"
	if "/><" in dent:
		return "decpart"
def parse(reg,oper):
	global A,B,C,D,E,F,M,R,temp, K, N
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
		A = A + eval(reg)
		R = A%eval(reg)
		M = eval(reg)
	if oper == "#":
		print eval(reg)
	if oper == "v":
		A = math.sqrt(eval(reg))
		M = A*2
	if oper == "^":
		A = eval(reg)
	if oper == "!":
		if "A" in reg:
			A = abs(A)
		else:
			opx = "%s = M"%reg
			exec(opx)
	if oper == "><":
		temp = eval(reg)
		opx = "%s = A"%reg
		exec(opx)
		A = temp
	if oper == "decpart":
		temp = int(A)
		M = A - int(A)
	if oper == "*":
		opx = "%s = 0"%reg
		exec(opx)
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
	global M
	if "help" in dent:
		print """
SIMULATORE DI OLIVETTI PROGRAMMA.
Comandi:
X viene usato come sinonimo di registro, eistono B,C,D,E,F per i dati, A per l'elaborazione,
M riceve le immissioni e R per il calcolo.
X+ -> A = A + X (addizione)
X- -> A = A - X (sottrazione)
Xx -> A = A * X (moltiplicazione)
X: -> A = A : X (divisione)
Xv -> A = radice di X, M = doppio della radice di X
X^ -> Mette il contenuto del registro X in A
X! -> Mette il conteniuto del registro M in X
X>< -> Scambia il contenuto di A e di X
X* -> Azzera il registro X
Supporto COS, SIN, ARC e TAN
"""
	if "S" in dent:
		M = input(">")
	
	if "open" in dent:
		#non funziona
		a = raw_input("Inserire nome file: ")
		with open(a) as f:
			lines = f.readlines()
		for x in lines:
			reg = regpars(dent)
			oper = ops(dent)
			parse(reg,oper) 
		
	reg = regpars(dent)
	oper = ops(dent)
	parse(reg,oper)
	p101()
	
p101()
	
