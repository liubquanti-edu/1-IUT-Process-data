import csv

def extract_professors(csv_file):
    professors = set()  # Використовуємо множину для уникнення дублікатів
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            prof = row.get('Prof', '').strip()
            if prof and prof != 'Intervenant à préciser':  # Пропускаємо порожні значення або "Intervenant à préciser"
                professors.add(prof)
    return sorted(professors)  # Сортуємо імена в алфавітному порядку

def main():
    csv_file = 'data/ADECal-mod-2.csv'  # Вкажіть шлях до вашого CSV-файлу
    professors = extract_professors(csv_file)
    print("Список викладачів:")
    for prof in professors:
        print(prof)

if __name__ == '__main__':
    main()