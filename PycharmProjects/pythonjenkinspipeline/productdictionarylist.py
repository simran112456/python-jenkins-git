products ={
    "productId" : "A1234",
    "ProductName": "OnePlusPro",
    "price": 50000.0,
    "vendors" :
      [
          {"name":"Amazon", "email": "abcdef@amazon.com"},
          {"name":"flipcart", "email": "aeedef@flipcart.com"},
          {"name":"tatacliq", "email": "abddcdef@tatacliq.com"}
      ]
}

#for product in products["vendors"]:
  #  print(type(product))
   # print(product["email"])

for product in products.get("vendors"):
    print(type(product))
    print(product.get("email"))