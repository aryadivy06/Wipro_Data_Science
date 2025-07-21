def is_palindrome(str6):
   sta=0
   end=len(str6)-1
   while sta<end:
      if str6[sta]!=str6[end]:
         return False
      sta=sta+1
      end=end-1
   return True
