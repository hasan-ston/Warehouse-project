def main():
  print(f"Welcome!")
  userid=input("Enter your id: ")
  authenticate(userid) #do we need this
  while not authenticate(userid):
    userid=input("Enter your id: ")
    autheticate(userid)  

  while not lookup_products(scan_barcode()):
    lookup_products(scan_barcode())
    
    

  pack_products(lookup_products(scan_barcode()))

  
    
    
    
  
  
    
    
  
  print(scan(barcode))
  print


