import sys
from collections import Counter

def parse_log_line(line: str) -> dict:
    date, time, error_level, *message_list = line.split(' ')    
    return {'date': date, 'time': time, 'error_level': error_level, 'message': ' '.join(message_list).strip()}

def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]: 
    return [log for log in logs if log['error_level'] == level]

def count_logs_by_level(logs: list) -> dict:
    return Counter(log['error_level'] for log in logs)

def display_log_counts(counts: dict):
    headers = ['Рівень логування', 'Кількість']
    col_width = [20, 10]
    
    # Print headers
    print(f'{headers[0]:<{col_width[0]}}|{headers[1]:^{col_width[1]}}')
    print('-' * col_width[0] + '|' + '-' * col_width[1])
    
    # Print data
    for level, count in counts.items():
        print(f'{level:<{col_width[0]}}|{str(count):^{col_width[1]}}')

def load_logs(file_path: str) -> list[dict]:
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                logs.append(parse_log_line(line))
            except ValueError:
                print(f'Помилка при парсингу рядка: {line}')
    return logs

if __name__ == '__main__':
    if 2 > len(sys.argv) >= 3:
        print('Usage: python logs.py <file_path> <level>')
        sys.exit(1)
    logs = load_logs(sys.argv[1])
    
    counts = count_logs_by_level(logs)
    display_log_counts(counts)
    
    if len(sys.argv) == 3:
        print('')
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)
        
        if len(filtered_logs) == 0:
            print(f'Не знайдено логів для рівня: {level}')
        else: 
            print(f"Деталі логів для рівня '{level}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
