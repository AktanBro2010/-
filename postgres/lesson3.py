""" 
ALTER TABLE 
"""

# Виды связей

# один к одному - one to one (создается через дополнительную колонку с ограничением  UNIQUE)
# один человек - один ID паспорт

# один ко многим - one to many (создается через дополнительную колонку)
# один блогер - много постов
# один куратор - много студентов

# Многие ко многим - many to many (создается через третью таблицу)
# один ментор - много студентов, один студент - много менторов
# один разработчик - много проектов, один проект - много разработчиков


# Import/Export баз данных

# write file to db  База Данных должна существовать!!!
# psql <database_name> < <file_name.sql>
# psql -U <username> -d <database_name> -f <file_name.sql>

# write from db to file
# pg_dump database_name > file.sql
# pg_dump -U username database_name > file.sql


""" 
Агрегационные функции sum(), avg(), count(), min(), max() 
"""

# CASE - if else

# SELECT <column> CASE WHEN <column> = 1 THEN 'OK' WHEN <column> = 2 THEN 'GOOD' END FROM <table_name>;
