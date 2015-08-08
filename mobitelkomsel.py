import requests
import bs4
import re

class mobi(object):
	def __init__(self):
		super(mobi, self)
		self.url = requests.get('http://mobi.telkomsel.com/profil/profileinternet/profileinternet')

	def getNumber(self):
		soup = bs4.BeautifulSoup(self.url.text)
		a = soup.find_all('span', 'usermsidn')
		b = re.split("<|>", str(a[0]))[-3]
		return b

	def telkomsel(self):
		number = self.getNumber()
		if self.url.ok:
			soup = bs4.BeautifulSoup(self.url.text)
			a1 = []
			a2 = []
			for i in soup.find_all('table'):
				a = str(i.text).split("\n")
				for j in a:
					if str(j).strip() != '':
						a2.append(str(j).strip())
				a1.append(a2)
				a2 = []
			for i in range(len(a1)):
				if i != len(a1) - 1:
					if a1[i][1:] == a1[i+1]:
						print "\n"
						print "Number",(' '*(34 - len("number"))), "=", number
						print a1[i][0],":"
						print "\t",a1[i][1],(' '*(26 - len(a1[i][1]))), "=", a1[i][1+1]
						print "\t",a1[i][3],(' '*(26 - len(a1[i][3]))), "=", a1[i][3+1]
						print "*"*64
		else:
			print "can't connect !"

if __name__ == '__main__':
	c = mobi()
	c.telkomsel()
	# c.getNumber()