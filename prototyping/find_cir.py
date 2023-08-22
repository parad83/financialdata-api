
def find_cir(string):
    matches = []
    with open("cik-lookup-data.txt", 'r') as file:
        for line in file:
            if string.lower() in line.strip().lower():             
                name = ' '.join(line.split(' ')[:-1])
                code = line.split(' ')[-1].split(':')[-2]               
                matches.append({name: code})
    return matches
print(find_cir("tesla"))