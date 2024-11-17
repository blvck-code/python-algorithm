f = open('data.txt', 'w')
f.write('Hello\n')
f.close()

choice = 'ham'

if choice == 'spam':
    print(1.25)
elif choice == 'hams':
    print(1.99)
else:
    print('Bad choice!')


branch = {
    'spam': 1.25,
    'ham': 1.98,
    'eggs': 2.3
}

print(branch.get('spam', 'Bad choice!'))




