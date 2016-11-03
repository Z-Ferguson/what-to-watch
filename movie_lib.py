with open('u.item', encoding='latin_1') as f:
    reader = csv.DictReader(f, fieldnames=['movie_id', 'movie_title', '', '', 'something_else'], delimiter='|')
    for row in reader:
        print(row)
