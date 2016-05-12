
class Zipcode():

    def get_zip():
        while True:
            try:
                zipcode = int(input('\nPlease enter your zipcode: '))
            except:
                print("\nYou didn't enter a valid zipcode")
            else:
                zipcode = str(zipcode)
                if len(zipcode) == 5:
                    return zipcode
                else:
                    print("\nYou didn't enter a valid zipcode")
