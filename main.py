from salary.salary import total_salary
from cats.catsInfo import get_cats_info
from bot.bot import main as run_bot
from pathlib import Path

salary_path = Path("./salary.txt")
cats_path = Path("./text.txt")

def main():
    print(total_salary(salary_path))
    print(get_cats_info(cats_path))
    run_bot()

if __name__ == "__main__":
    main()