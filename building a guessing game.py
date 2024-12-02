secret_word = "giraffe"
guess = ""
while guess != secret_word:
   guess = input("enter guess:") 
print("you win!")  




secret_word = "giraffe"
guess = ""
guess_count= 0
guess_limits= 3
out_of_guess= False

while guess != secret_word and not(out_of_guess):
   if guess_count < guess_limits:
    guess = input("enter guess:")
    guess_count += 1
   else:
    out_of_guess=True 
if out_of_guess:
   print("out of guesses, you loss!")  
else:   
  print("you win!")  