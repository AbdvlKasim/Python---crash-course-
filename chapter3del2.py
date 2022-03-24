#ORGANISERE EN LISTE: for å sortere en liste permanent i for eks. alfabetisk rekkefølge, gjør man det slik:
Biler = ['Bmw', 'Audi','Mercedes', 'Volvo','Toyota']
Biler.sort()
print(Biler)
#Skal du printe dem i motsatt rekkefølge permanent, blir det slik#
Biler = ['Bmw', 'Audi','Mercedes','Volvo','Toyota']
Biler.sort(reverse=True)
print(Biler)
#Skal du printe det midlertidig i en alfabetisk rekkfølge og fortsatt beholde den gamle lista gjør du det slik:
print("\nHer er den originale lista mi:")
print(Biler)
print("\nher er den sorterte lista mi:")
print(sorted(Biler))
print("\nHer er den originale lista mi igjen:")
print(Biler)
#Hvis du skal printe ut meldingen i motsatt ordre altså ikke alfabetsik men motsatt av det du har nå gjør du slik:
#da bruker du REVERSE syntaxen
Biler.reverse()
print(Biler)
#Skal du finne ut hvor stor listen din er så bruker du syntaxern: len
#Først må du alltid huske å skrive print siden du skal printe noe deretter så skriver du len
print(len(Biler))
#Det vil være fornuftig å kunne syntaxen len når du skal finne ut hvor mange spillere det er igjen i et spill eller
#finne ut hvor mange brukere det er registrert inne på en nettside osv.

#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.

Favorite_places = ['New York', 'Japan', 'Maldives', 'Mecca', 'Los Angeles']

print(sorted(Favorite_places))

print("\nOriginal order:")
print(Favorite_places)

print("\nReverse aplphabetical:")
print (sorted(Favorite_places, reverse=True))

print("\nReversed:")
Favorite_places.reverse()
print (Favorite_places)

print("\nOriginal order:")
Favorite_places.reverse()
print (Favorite_places)

print("\nAlfabetisk")
Favorite_places.sort()
print(Favorite_places)

print("\nReverse Alfabetisk")
Favorite_places.sort(reverse=True)
print(Favorite_places)

#3-9. Dinner Guests: Use len to print a message indicating the number of people you are inviting to dinner#
Gjester = ['Sebastian', 'Mago', 'Berat', 'Yusef', 'Memo']
Antall_gjester = len(Gjester)

print(Gjester)
print(f"\nJeg inviterer {Antall_gjester} gjester på middag hos meg idag.")

#Every function: Think of something you could store in a list. for ex. mountains, rivers. Write a program that creates
# a list containing these items and then uses each function introduced in this chapter at least once.#

Språk = ['Arabisk', 'Urdu', 'Norsk', 'Punjabi']
print("\nOriginal list")
print(Språk)

print("\nUse Append method")
Språk.append('Tyrkisk')
print(Språk)

print("\nuse insertion")
Språk[0] = 'Albansk'
print(Språk)

print("\nuse insert() method")
Språk.insert(2, 'Russisk')
print(Språk)

print("\nUse Del function")
del Språk [2]
print(Språk)

print("\n Use Pop method()")
Språk.pop(4)
print(Språk)

print("\n Use pop method to use it another place")
popped_språk = Språk.pop(0)
print(popped_språk)

print("\nUse remove method")
Språk.remove('Punjabi')
print(Språk)
#Skal du ha med text kan du gjøre følgende:
fjern_språk = 'Punjabi'
print(f" \nJeg måtte fjerne {fjern_språk}, Fra lista mi igår")
Språk.append('Somalisk')
Språk.append('Persisk')
print("\n organise with sort and revers method:")
print(sorted(Språk))
print(sorted(Språk, reverse=True))

print("\n use reverse twice")
Språk.reverse()
print(Språk)
Språk.reverse()
print(Språk)
print("\n use sort method twice")
Språk.sort()
print(Språk)
Språk.sort(reverse=True)
print(Språk)

print("\n find the lenght or size of the list")
Antall_Språk = len(Språk)
print(f" Det er antall {Antall_Språk} Språk i lista mi.")

#En veldig vanlig index error i Python er denne:
Dyr = ['Tiger', 'Løve', 'Hai']
print(Dyr[3])
#Denne erroren er vanlig siden man tror det tredje elementet i lista er 3 men i python teller den fra 0, derfor så vil
# hai være 2 i dette tilfelle.





