import pandas as pd


def get_sheet(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df


def get_rows(file_path, sheet_name):
    df = get_sheet(file_path, sheet_name)
    rows = df.shape[0]
    return rows


def get_data(file_path, sheet_name, row_number, column_name):
    df = get_sheet(file_path, sheet_name)
    value = df.loc[row_number, column_name]
    return value


def write_to_excel(file_path, sheet_name, row_number, column_name, value_to_write):
    df = get_sheet(file_path, sheet_name)
    df.loc[row_number, column_name] = value_to_write
    writer = pd.ExcelWriter(file_path)
    df.to_excel(writer,sheet_name)
    writer.save()
