#!/usr/bin/env python
#-*-coding: utf-8-*-
# Liturgia Diária versão 0.2
# Autor: Isac C.
from subprocess import Popen, PIPE
import os
import sys
import time

class cores:
	lilas = '\033[95m'
	azul = '\033[94m'
	verd = '\033[92m'
	amar = '\033[93m'
	verm = '\033[91m'
	negr = '\033[1m'
	subl = '\033[4m'
	fim =  '\033[0m'

cmd = "curl catolicoorante.com.br/liturgia_diaria.php 2> /dev/null"
processo = Popen([cmd], stdout=PIPE, shell=True)
saida, erro = processo.communicate()

html = saida.split('</form>')[1].split("Reflexão sobre o Evangelho")[0]

tags = ['<br />', '</center>', '<p>', '</p>', '<center>']
html = html.replace('<br>', '\n')
for t in tags:
    if t in html:
        html = html.replace(t, '')

dicionario = {"<b>":cores.negr, "<strong>":cores.negr, "</b>":cores.fim,\
"</strong>":cores.fim, "<em>":cores.subl, "<i>":cores.subl, "</em>":cores.fim, "</i>":cores.fim}

for x in dicionario:
    if x in html:
        html = html.replace(x, dicionario[x])

html = cores.verd + "Liturgia Diária versão 0.2 \n\n" + cores.fim + html + cores.fim

a = open("/tmp/liturgia.txt", "w")
a.write(html)
a.close()
os.system("more /tmp/liturgia.txt")
os.system("rm /tmp/liturgia.txt")
