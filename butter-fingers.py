from random import randint
import random
text = "hello this is a test message"

probOfTypo = 0.1
keyboard = "querty"
keyApprox = {}

if keyboard == "querty":
	keyApprox['q'] = "qwasedzx"
	keyApprox['w'] = "wqesadrfcx"
	keyApprox['e'] = "ewrsfdqazxcvgt"
	keyApprox['r'] = "retdgfwsxcvgt"
	keyApprox['t'] = "tryfhgedcvbnju"
	keyApprox['y'] = "ytugjhrfvbnji"
	keyApprox['u'] = "uyihkjtgbnmlo"
	keyApprox['i'] = "iuojlkyhnmlp"
	keyApprox['o'] = "oipklujm"
	keyApprox['p'] = "plo['ik"

	keyApprox['a'] = "aqszwxwdce"
	keyApprox['s'] = "swxadrfv"
	keyApprox['d'] = "decsfaqgbv"
	keyApprox['f'] = "fdgrvwsxyhn"
	keyApprox['g'] = "gtbfhedcyjn"
	keyApprox['h'] = "hyngjfrvkim"
	keyApprox['j'] = "jhknugtblom"
	keyApprox['k'] = "kjlinyhn"
	keyApprox['l'] = "lokmpujn"

	keyApprox['z'] = "zaxsvde"
	keyApprox['x'] = "xzcsdbvfrewq"
	keyApprox['c'] = "cxvdfzswergb"
	keyApprox['v'] = "vcfbgxdertyn"
	keyApprox['b'] = "bvnghcftyun"
	keyApprox['n'] = "nbmhjvgtuik"
	keyApprox['m'] = "mnkjloik"
	keyApprox[' '] = " "
else:
	print "Keyboard not supported."

probOfTypoArray = []
probOfTypo = int(probOfTypo * 100)


for letter in text:
    if random.choice(range(0, 100)) <= probOfTypo:
        print(random.choice(keyApprox[letter]), end="")
    else:
        print(letter, end="")

