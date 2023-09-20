import pandas as pd
from sqlalchemy import create_engine


def data_loading(file_path):
    try:
        # Чтение данных из файла xlsx
        data_file = pd.read_excel(file_path)

        # Удаление пустых строк
        data_file.dropna(inplace=True)

        # Исключение ошибок типов данных
        data_file = data_file.convert_dtypes()

        # Подключение к БД
        engine = create_engine('sqlite:///historical_data.db', echo=False)

        # Запись в БД
        data_file.to_sql('historical_data', con=engine, if_exists='append', index=False)

        print(f"Статус - OK. Данные из файла {file_path} загружены в БД")
    except Exception as e:
        print(f"Статус - Ошибка при загрузке данных из файла {file_path}: {str(e)}")


if __name__ == '__main__':
    files = ['data_file_1.xlsx', 'data_file_2.xlsx', 'data_file_3.xlsx']  # Список файлов для загрузки

    for file in files:
        data_loading(file)
