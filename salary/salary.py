def total_salary(path):
    try:
        with open (path, "r", encoding="utf-8" ) as file:        
            total = 0
            count = 0
            for line in file:
                line = line.strip()
                if not line:
                    continue
                total += int(line.split(",")[1])
                count += 1
            return f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {total / count}"
    except FileNotFoundError:
        return "File not found"
    except ZeroDivisionError:
        return "No data"