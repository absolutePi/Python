secret_word="gay"
guess=""
guess_cnt=0
guess_limit=5
out_of_guess=False
while guess!=secret_word and not(out_of_guess):
    if guess_cnt<guess_limit:
        guess=input("Enter your guess: ")
        guess_cnt+=1
    else: 
        out_of_guess=True
if out_of_guess:
    print("Yo dumb ass lose lmao")
else:
    print("Nice one,u win")