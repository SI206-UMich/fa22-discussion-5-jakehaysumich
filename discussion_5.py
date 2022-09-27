import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in sentence:
		if i == 'a' or i == "A":
			total += 1
	return total

# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)
		pass

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		max_item = None
		max_stock = 0
		for item in self.items:
			if max_item == None:
				max_item = item.name
				max_stock = item.stock
			elif max_stock<item.stock:
				max_item = item.name
				max_stock = item.stock
		return max_item

		pass
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		max_item = None
		max_price = 0
		for item in self.items:
			if max_item == None:
				max_item = item.name
				max_price = item.price
			elif max_price<item.price:
				max_item = item.name
		return max_item
		pass	



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("peter piper picked a peck of pickled peppers"),1,'tested count a with item 1')
		pass


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		warehouse1 = Warehouse()
		self.assertEqual(len(warehouse1.items),0)
		list_items = [self.item1, self.item2]
		warehouse2 = Warehouse(list_items)
		self.assertEqual(len(warehouse2.items),2)
		warehouse1.add_item(self.item3)
		self.assertEqual(len(warehouse1.items),1)
		self.assertEqual(warehouse1.items[0], self.item3)
		pass


	# ## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		warehouse1 = Warehouse()
		self.assertEqual(warehouse1.get_max_stock(),None)
		warehouse2 = Warehouse([self.item1, self.item2])
		self.assertEqual(warehouse2.get_max_stock(),"Cider")

		pass


	# # Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		warehouse1 = Warehouse()
		self.assertEqual(warehouse1.get_max_price(),None)
		warehouse2 = Warehouse([self.item1, self.item2])
		self.assertEqual(warehouse2.get_max_price(),"Beer")
		pass
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()