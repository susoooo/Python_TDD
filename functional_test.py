from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		#self.browser = webdriver.Safari()
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()
	
	def test_can_start_a_list_and_retrieve_it_later(self):

		#Pilar has heard about a new cool to-do lists app, so she goes to the app
		#website to check-it out. 
		time.sleep(1)
		self.browser.get('http://localhost:8000')

		#She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title) 
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header.text)		

		#She is invited to enter a to-do item stright away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)		

		#She types "Buy peacock feather" into a text box. (Pilar's hobby is to tie
		# fly-fishing lures)
		inputbox.send_keys('Buy peacock feathers')	

		#When she hits Enter, the page updates, and now the page lists:
		# "1: Buy peacock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows)
		)


		#There is still a text box inviting her to add another item. She enters
		# "Use peacock feathers to make a fly" (Pilar is very methodical)
		self.fail('Finish the test!')

		#The page updates again and now shows both items in the list

		#Pilar wonders if the site will remenber her list. Then she sees that the 
		# site has generates an unique URL for her. -- There is some explanatory
		# to that text.

		#She visites that URL - The to-do list is still there

		#Satisfied, she goes back to sleep

if __name__ == '__main__':
	unittest.main(warnings='ignore')
