def total_salary(path):
    try:
        with open (path, "r", encoding="utf-8" ) as file:        
            total = 0
            count = 0
            for line in file:
                line = line.strip()
                if not line:
                    continue
                total += float(line.split(",")[1])
                count += 1
            return f"Загальна сума заробітної плати: {total:.2f}, Середня заробітна плата: {total / count:.2f}"
    except FileNotFoundError:
        print("File not found")
        return 0, 0
    except ZeroDivisionError:
        print("No data")
        return 0, 0
    
    if count == 0:
        return 0, 0

    return total, total / count