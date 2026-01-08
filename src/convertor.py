import os
from colorama import Fore, Style
from script.modified import Convert2CSV
import keyboard

def find_ics_files(directory):
    ics_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".ics"):
                ics_files.append(os.path.join(root, file))
    return ics_files

def display_ics_menu(ics_files):
    selected_index = 0
    base_directory = os.getcwd()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.BLUE}Sélectionnez un fichier .ics à convertir:\n{Style.RESET_ALL}")
        for i, file in enumerate(ics_files):
            relative_path = os.path.relpath(file, base_directory)
            if i == selected_index:
                print(f"{Fore.CYAN}> {relative_path}{Style.RESET_ALL}")
            else:
                print(f"{Fore.BLUE}  {relative_path}{Style.RESET_ALL}")

        event = keyboard.read_event(suppress=True)
        if event.event_type == "down":
            if event.name == "down":
                selected_index = (selected_index + 1) % len(ics_files)
            elif event.name == "up":
                selected_index = (selected_index - 1) % len(ics_files)
            elif event.name == "enter":
                return ics_files[selected_index]

def convert_ics_to_csv():
    current_directory = os.getcwd()
    ics_files = find_ics_files(current_directory)

    if not ics_files:
        print(f"{Fore.RED}Aucun fichier .ics trouvé dans le répertoire actuel.{Style.RESET_ALL}\n")
        input(f"{Fore.CYAN}> Revenir au menu{Style.RESET_ALL}")
        return

    selected_file = display_ics_menu(ics_files)
    try:
        csv_file = os.path.splitext(selected_file)[0] + ".csv"
        relative_path = os.path.relpath(selected_file, current_directory)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.YELLOW}Conversion de {relative_path} en {csv_file}{Style.RESET_ALL}\n")

        converter = Convert2CSV()
        converter.read_ical(selected_file)
        converter.make_csv()
        converter.process_summary_column()
        converter.split_column(3, ':')  
        converter.process_description_column()
        converter.save_csv(csv_file)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.GREEN}Fichier converti avec succès: {csv_file}{Style.RESET_ALL}\n")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.RED}Erreur lors de la conversion de {relative_path}: {e}{Style.RESET_ALL}\n")

    input(f"{Fore.CYAN}> Revenir au menu{Style.RESET_ALL}")