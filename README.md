# Петри.py
`Петри.py` - скрипт для анализа покрывающих деревьев сетей Петри. Python3<br>Сама сеть Петри задаётся как словарь t. Ключ - имя перехода; Значение - два массива, первый это входные позиции, а второй это выходные позиции. Повторения допускаются.<br>Программа использует обход в ширину и генерирует таким образом все возможные вариации переходов от одного состояния к другому.<br>Программа определяет, было ли такое состояние получено до этого. Если такое случается, то программа выводит символ '*' перед состоянием.
После каждого вывода состояния на экран, программа просит ввод с клавиатуры. Просто нажмите Enter, если хотите продолжить, либо введите exit, чтобы программа завершилась. В программе используется [пример №7](http://1802.ru/edu/SetiPetri.pdf).

# WiFi files
Два простых скрипта на языке `Python`, которые играют роль клиента и сервера для передачи каких либо файлов по Wi-Fi либо сети Интернет.
