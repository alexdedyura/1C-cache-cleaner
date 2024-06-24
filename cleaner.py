import os
import shutil
import psutil

print("Очистка кэша 1С | Alex Dedyura")

user = os.getlogin()
print("Текущий пользователь: ", user)

# Получение среды APPDATA текущего пользователя
APPDATA = os.getenv('APPDATA')
# Получение среды LOCALAPPDATA текущего пользователя
LOCALAPPDATA = os.getenv('LOCALAPPDATA')

if not APPDATA or not LOCALAPPDATA:
    print("Не удалось получить значения переменных среды APPDATA или LOCALAPPDATA.")
    exit(1)

# Получение пути 1С в AppData\Local
APPDATA_1C = os.path.join(APPDATA, '1C', '1cv8')
# Получение пути 1С в AppData\Roaming
LOCALAPPDATA_1C = os.path.join(LOCALAPPDATA, '1C', '1cv8')

# Исключение файлов и папок для удаления
APPDATA_EX = ['1cv8.pfl', '1cv8c.pfl', '1cv8strt.pfl', '1cv8u.pfl', 'ExtCompT']
LOCALAPPDATA_EX = ['1cv8u.pfl', 'dumps']

RES_EX = [os.path.join(APPDATA_1C, ex) for ex in APPDATA_EX] + [os.path.join(LOCALAPPDATA_1C, ex) for ex in LOCALAPPDATA_EX]

def clear_cache(path_to_cache):
    if not os.path.exists(path_to_cache):
        print(f"Путь {path_to_cache} не существует.")
        return

    for i in os.listdir(path_to_cache):
        full_path = os.path.join(path_to_cache, i)
        if full_path not in RES_EX:
            try:
                if os.path.isdir(full_path):
                    shutil.rmtree(full_path)
                    print(f"Удалена папка: {full_path}")
                else:
                    os.remove(full_path)
                    print(f"Удален файл: {full_path}")
            except Exception as e:
                print(f"Ошибка при удалении {full_path}: {e}")

def close_1c_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] in ['1cv8.exe', '1cv8c.exe', '1cv8s.exe']:
                print(f"Закрытие процесса {proc.info['name']} с PID {proc.info['pid']}")
                proc.terminate()
                proc.wait(timeout=5)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired) as e:
            print(f"Не удалось завершить процесс {proc.info['name']} с PID {proc.info['pid']}: {e}")

# Закрытие процессов 1С перед очисткой кэша
close_1c_processes()

# Очистка кэша 1С
clear_cache(APPDATA_1C)
clear_cache(LOCALAPPDATA_1C)

print("Кэш 1С очищен успешно!")
input("Нажмите Enter для завершения программы...")
