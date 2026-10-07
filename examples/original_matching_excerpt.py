# Original selected matching statements with a new in-memory wrapper.
import pandas as pd
from original_name_formatting import remove_numbers_in_parentheses, parse_full_name

def selected_name_matching(df1, df2):
    """Historical name-only prototype; not verified identity resolution."""
    df2.columns = df2.columns.str.strip()
    df2["Normalized Author Names"] = df2["Author full names"].apply(remove_numbers_in_parentheses)
    df2["Normalized Author Names"] = df2["Normalized Author Names"].str.split(";")
    df2 = df2.explode("Normalized Author Names")
    df2["Normalized Author Names"] = df2["Normalized Author Names"].apply(parse_full_name)
    df1.columns = df1.columns.str.strip()
    titles_to_remove = [
        "Profesor", "Docent", "Ogreti̇m Gorevli̇si̇", "Arastirma Gorevli̇si̇", "Doktor Ogreti̇m Uyesi"
    ]
    pattern = "|".join(titles_to_remove)
    df1["Name and Surname"] = df1["Title, Name and Surname"].str.replace(pattern, "", regex=True).str.strip()
    matched_df = pd.merge(
        df1,
        df2,
        left_on="Name and Surname",  # 1. dosyadaki "Name and Surname" sütunu
        right_on="Normalized Author Names",  # 2. dosyadaki "Normalized Author Names" sütunu
        how="inner"  # Sadece eşleşenleri al
    )
    matched_df = matched_df[["Name and Surname"]]
    final_matched_df = matched_df.drop_duplicates(subset=["Name and Surname"])
    return final_matched_df
