""" 
Введение в PostgreSQL. Создание баз данных и таблиц.
"""

# Примеры СУБД (система управления базами данных): MySQL, Firestore, MongoDB, MarinaDB, SQLite, PostgreSQL


# PostgreSQL - система управления БД (это комплекс программ, позволяющий создавать БД и манипулировать ими (администрирование БД))

# База данных - организованная структура для хранения/изменения взаимосвязанных данных (больших объемов)

# SQL (Structured Query Language) - декларативный язык структурированных запросов - язык запросов, используемый для сохранения, изменения, удаления и извлечения данных из БД

# 1. sudo -i -u postgres - переход в учетную запись postgres
    # psql - переход к командной строке

# 2. sudo -u postgres psql - переход к командной строке (под юзером postgres и подключении к БД postgres)

# 3. psql - переход к командной строке (под вашим юзером и подключение к вашей БД) (для работы этой команды должен существовать юзер и БД как в терминале)


# \l - список БД
# \du - список пользователей
# \c <db_name> - подключение БД db_name
# \dt or \d - список всех таблиц в БД
# \d <table_name> - просмотр подробной информации о таблице table_name
# \q - выход


# SQL запросы

# 1. CREATE DATABASE <db_name>; - создание БД

# 2. CREATE TABLE <table_name (column_name type, ...)>; - создание таблицы

# 3. CREATE USER <username>;
    # CREATE USER <username> WITH PASSWORD 'your_password'; - создание пользователя

# 4. ALTER ROLE <username> WITH <PRIVILEGE>; - предоставление прав пользователю


