import os
import shutil

print("Очистка кэша 1С | Alex Dedyura")

user = os.getlogin()
print("Текущий пользователь: ",user)

# Получение среды APPDATA текущего пользователя
APPDATA = os.getenv('APPDATA')
# Получение среды LOCALAPPDATA текущего пользователя
LOCALAPPDATA = os.getenv('LOCALAPPDATA')
# Получение пути 1С в AppData\Local
APPDATA_1C = os.path.join(APPDATA, '1C\\1cv8')
# Получение пути 1С в AppData\Roaming
LOCALAPPDATA_1C = os.path.join(LOCALAPPDATA, '1C\\1cv8')

# Исключение файлов и папок для удаления
APPDATA_EX = ['1cv8.pfl', '1cv8c.pfl', '1cv8strt.pfl', '1cv8u.pfl', 'ExtCompT']
LOCALAPPDATA_EX = ['1cv8u.pfl', 'dumps']
#
RES_EX = APPDATA_EX + LOCALAPPDATA_EX


def clear_cache(path_to_cache):
    for i in os.listdir(path_to_cache):
        if i not in RES_EX:
            #print(os.path.join(path_to_cache, i))
            shutil.rmtree(os.path.join(path_to_cache, i))


clear_cache(APPDATA_1C)
clear_cache(LOCALAPPDATA_1C)
print("Кэш 1С очищен успешно!")
input("Нажмите Enter для завершения программы...")
