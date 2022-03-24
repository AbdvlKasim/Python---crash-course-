#når du kjører denne koden så vil ikke de forskjellige bicyucles komme med en vanlig output#
#den vil være nøyaktig samme som du har skrevet den ned som under:#
bicyles = ['trek', 'cannondale', 'redline', 'specialized']
print (bicyles)

#for å velge en spesifikk item i en liste og få svaret til å komme uten parantesene i output gjør man følgende:#
bicyles = ['trek', 'cannondale', 'redline', 'specialized']
print (bicyles[0])

#for å velge den siste item i en liste hvor vi ikke vet hvor lang listen er, så skriver man inn -1, for eks#
bicyles = ['trek', 'cannondale', 'redline', 'specialized']
print (bicyles[-1])

#for å velge en ting fra liste og gi kommentar på det#
bicyles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My favorite bike was {bicyles[3].title()}"
print(message)

#Try it yourself kapittel 3
#3-1. Names: Store the names of a few of your friends in a list called names and
#print each person’s name by accessing each element in the list, one at a time
Names = ['Mehmet', 'Berat', 'Ømer', 'Iskender']

print(f"Hey my friend {Names[0]}")
print(f"Hey my friend {Names[1]}")
print(f"Hey my friend {Names[2]}")
print(f"Hey my friend {Names[3]}")

#Dette er en annen måte man kan gjøre det på#
Gjester = ['shpend', 'Sebo', 'berat']

name = Gjester[0].title()
print(f"{name}, please come to dinner")

name2 = Gjester[1]
print(f"{name2}, do not come to dinner")

name3  = Gjester[2]
print(f"Hey, {name3.title()}, please come to dinner")

#3-3. Your Own List: Think of your favorite mode of transportation, such as a
#motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements
# about these items, such as “I would like to own a Honda motorcycle.
List_of_cars = ['Bmw','Mercedes','toyota','Tesla','Lamborghini']
message = f"I would like to own a {List_of_cars[0]} someday"
message_2 = f"not everybody can afford a {List_of_cars[4]}, but everyone can buy a {List_of_cars[2]}."
print(message)
print(message_2)

#Under ser du hvordan du kan endre en verdi i en liste, for eks. gjøre en Bmw om til en bugatti#
Cars = ['bmw','mercedes','Audi','Tesla']
print (Cars)
Cars[0] = 'Bugatti'
print (Cars)

#For å legge til en ny item i en liste, gjør man følgende:#
Cars.append('Jaguar')
print(Cars)

#Har man en tom liste og vil legge til data bruker man append#
Animals = []
Animals.append('Tiger')
Animals.append('Lion')
Animals.append('Cheetah')
print (Animals)

#Skal man legge til en ny verdi og velge hvor den skal plasseres, bruker man insert syntax#
Animals.insert(2,'Jaguar')
print(Animals)

#For å slette noe fra en liste bruker man syntaxen del#
del Animals[3]
print (Animals)

#Hvis vi skal fjerne noe fra en liste men fremdeles trenger den verdien i en annen liste, kan man bruke POP syntaxen#
Motorcycles = ['Honda','Yamaha','suzuki']
print(Motorcycles)
popped_Motorcycles = Motorcycles.pop()
print (popped_Motorcycles)

#Et eksempel på hvor vi kan bruke POP er hvis for eks motorcycles er en liste over alle motorsykler vi har hatt, så skal popped motorcyle være den siste man har eid#
Motorcycles = ['Honda','Yamaha','suzuki']
Last_owned = Motorcycles.pop()
print(f"den siste motorsykkelen jeg hadde var {Last_owned.title()}")

#Skal du velge en spesifikk item i en liste med bruk av pop, gjør du følgende#
First_owned = Motorcycles.pop(0)
print (f"My first ever motorcycle was a {First_owned}")

#Det er ikke alltid du vet verdien på item du skal fjerne så da kan man heller bruke remove syntax#
Flyselskap = ['SAS','Ryanair','Norwegian','QatarAirways']
Flyselskap.remove('QatarAirways')
print(Flyselskap)

#Man kan også bruke remove syntax og begrunne hvorfor du sletta det#
PC = ['mac','Lenovo', 'Acer','Asus']
Altfor_dyrt = 'mac'
PC.remove(Altfor_dyrt)
print(f"\n En {Altfor_dyrt.strip()} ble altfor dyr for meg")

#Try it yourself chapter 3#
#3-4 Guest list#
venner = ['Berat','Mehmet','Sebastian']

Venn1 = venner[0]
print(f"\n{Venn1}, Du er invitert på middag!")

Venn2 = venner[1]
print(f"{Venn2}, Du er invitert på middag!")

Venn3 = venner[2]
print(f"{Venn3}, Du er invitert på middag!")

print(f"\n{Venn3}, beklager jeg får ikke kommet alikevel!")

#3-5. Changing Guest List:You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

#Skal du slette noen fra liste og erstatte de med noen andre, gjør man følgende:
#la oss si Sebastian ikke kan komme, så vi inviterer Gurol heller#
del(venner[2])
venner.insert(2,'Gurol')
#Deretter printer du invitasjonene på nytt#
Venn1 = venner[0]
print(f"{Venn1}, Du er invitert på middag!")

Venn2 = venner[1]
print(f"{Venn2}, Du er invitert på middag!")

Venn3 = venner[2]
print(f"{Venn3}, Du er invitert på middag siden Sebastian ikke kunne!")

#En annen løsning er:#
venner.remove('Gurol')
venner.append('Suleyman')
print(venner)

Venn1 = venner[0]
print(f"{Venn1}, Du er invitert på middag!")

Venn2 = venner[1]
print(f"{Venn2}, Du er invitert på middag!")

Venn3 = venner[2]
print(f"{Venn3}, Du er invitert på middag siden Gurol ikke kunne!")

#3-6 More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner#
venner.insert(0,'Yusef')
venner.insert(2,'Simer')
venner.append('Iskender')
venner.remove('Suleyman')

Venn1=venner[0]
Venn2=venner[1]
Venn3=venner[2]
Venn4=venner[3]
Venn5=venner[4]


print(f"\n{Venn1}, Du er invitert på middag hos meg")
print(f"{Venn2}, Du er invitert på middag hos meg")
print(f"{Venn3}, Du er invitert på middag hos meg")
print(f"{Venn4}, Du er invitert på middag hos meg")
print(f"{Venn5}, Du er invitert på middag hos meg")

#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#For å fjerne de aller fleste og kun ha 2 igjen med bruk av pop, gjør man følgende#
print("\nJeg kan desverre bare invitert 2 gjester siden jeg ikke får henta det nye middagsbordet")
venner.pop()
print(f"{Venn5}, beklager for at du ikke får kommet")
venner.pop()
print(f"{Venn4}, beklager for at du ikke får kommet")
venner.pop()
print(f"{Venn3}, beklager for at du ikke får kommet")

print(f"\n{Venn1}, Du er fortsatt invitert")
print(f"{Venn2}, Du er også fortsatt invitert")

del (venner[0])
del (Venner[1])
print(venner)










