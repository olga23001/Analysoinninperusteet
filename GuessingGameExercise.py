print("Please, guess my name.")  # Kysytään käyttäjää arvamaan nimi

number_of_guesses = 0

while number_of_guesses < 5:
    guess = input("")
    number_of_guesses += 1

    #Jos vastaus on erisuuri
    if guess != "Tommi":    
        print("Incorrect guess.")

    # Jos vastaus on oikein, looppi katkeaa
    else:
        print("Congratulations! Guesses:", number_of_guesses)
        break

    #Kysytään, haluaako käyttäjä lopettaa
    quit_option = input("Do you want to quit (y/n)? ")
    
    if quit_option.lower() == "y":
        print("Quitting the game.")
        break