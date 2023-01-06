secret_number =3
guess_count =0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('guess:'))
    guess_count += 1
    if guess == secret_number:
        print('YOU WON ')
        break
else : 
    print ('Sorry you fliled')