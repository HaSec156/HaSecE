#Hacker

import os
import sys
##############
red = "\033[31;1m"
green="\033[32;1m"
yello = "\033[33;1m"
cyan = "\033[46;1m"
def banner():
	print("")
	print red+("        Hello Iam Mehdi !!")
	os.system("figlet -f small '		   A77x'")
	print green+("""
    #######################
    #			  #
    #    Mehdi Boullouf   #
    #	   @HaSec156      #
    #			  #
    #######################
""")
	o = raw_input("    Press EnTer TO continue")
banner()
def head():
	title = raw_input("EnTer Title : ")
	index = raw_input("Enter Name OF index without .html : ")
	l = open(index+".html","a")
	l.writelines("""
	<head>
	<title>"""+title+"""</title>
	<head>
	""")
	bgcolor = raw_input("EnTer Background Color : ")
	bglink = raw_input("EnTer COlor OF Links : ")
	bfont = raw_input("EnTer THe Font OF Text : ")
	ntext = raw_input("EnTer 1st Text : ")
	ncolor = raw_input("EnTer The Color OF Text 1 : ")
	ima = raw_input("EnTer THe Source OF image : ")
	wima = raw_input("EnTer THe Width OF image : ")
	hima = raw_input("EnTer The Height IF Image : ")
	mtext = raw_input("EnTer Second Text : ")
	mcolor = raw_input("The Color : ")
	ltext = raw_input("Third Text : ")
	lcolor = raw_input("THe Color : ")
	lik = raw_input("EnTer Any Link Your Facebook,Youtube,... : ")
	mlik = raw_input("ENTer The Name Of Link : ")
	l.write("<body><body bgcolor='"+bgcolor+"'><body link='"+bglink+"'><font face='"+bfont+"'><div align=center><font color='"+ncolor+"'><h1>"+ntext+"</h1></font><img src='"+ima+"' width='"+wima+"' height='"+hima+"'></img><div align=center><hr><font color='"+mcolor+"'><h2>"+mtext+"</h2></font><font color='"+lcolor+"'><h3>"+ltext+"</h3></font><a href ='"+lik+"'>"+mlik+"</a>")
	l.close()
	print("Saved To "+index+".html Good Luck !")
head()
	

