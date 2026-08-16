def positive(Price):
   while True:
      if Price>0:
         break
      Price=float(input('Please enter a positive value : '));
   return Price;

def results(Dif,Return):
   if Dif > 0:
       print('Profit:',f'{Dif:.2f}','$')
       print('Return:',f'{Return:.2f}','%')
   elif Dif<0:
       print('Loss:',f'{Dif:.2f}','$')
       print('Return:',f'{Return:.2f}','%')
   else:
       print('There is no profit or loss')
       print('The percentage return is: 0%')
   
Stock=input('Give me the stock tag:');
InitialPrice=float(input('Enter initial price : '));
InitialPrice=positive(InitialPrice);
FinalPrice=float(input('Enter final price : '));
FinalPrice=positive(FinalPrice);
Dif=FinalPrice-InitialPrice
Return=(Dif/InitialPrice)*100;
print('Stock : ',Stock)
print('Initial price :$',f'{InitialPrice:.2f}')
print('Final price :$', f'{FinalPrice:.2f}')
results(Dif,Return);


  
  


