import requests
from bs4 import BeautifulSoup
from random import randint


base_url = "http://quotes.toscrape.com"
page_url = "/page/1"
all_quotes = []

while page_url:

	url = base_url + page_url
	response = requests.get(url)
	soup = BeautifulSoup(response.text,"html.parser")
	class_quote = soup.select(".quote")	

	for el in class_quote:
		text = el.find(class_="text").get_text()
		name = el.find(class_="author").get_text()
		href = el.a['href']

		all_quotes.append({
			"text" : text,
			"name" : name,
			"bio-link" : href
			})

	class_next = soup.find(class_ = "next")
	if(class_next):
		page_url = class_next.find("a")['href']
	else:
		page_url = []


#GAME LOGIC



def get_quote(value):
	return value['text']

def user_ans():
	user_ans = input("Enter your answer: ")
	return user_ans

def check_ans(rand_quote,user_ans):
	if(user_ans == rand_quote['name']):
		return 1
	else:
		return 0

def hint2(rand_quote,base_url):
	url = base_url + rand_quote['bio-link']
	response = requests.get(url)
	soup = BeautifulSoup(response.text,"html.parser")
	date = soup.find(class_='author-born-date').get_text()
	loc = soup.find(class_='author-born-location').get_text()
	print(f"Author born on {date} at {loc}")



def hint1(rand_quote):
	letters = [i for i in rand_quote['name']]
	print("Author's name starts with "+letters[0]+" and ends with "+letters[-1])

guess = 3
def game(guess):
	rand_quote = all_quotes[randint(1,len(all_quotes))]
	print(get_quote(rand_quote))
	while (guess>0):
		if(check_ans(rand_quote,user_ans()) == 1):
			print("Congratulations! You Won")
			break
		else:
			if(guess==3):
				hint1(rand_quote)
			elif(guess==2):
				hint2(rand_quote,base_url)
		guess-=1
	if (guess==0):
		print("You Lost")


if __name__ == '__main__':
	game(guess)
	play = input("Want to play again (y/n)? ")
	if(play=='y'):
		game(guess)




	
	


	




	



	




