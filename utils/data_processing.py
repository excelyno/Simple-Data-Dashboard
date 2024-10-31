import pandas as pd

def load_data(filepath):
    """Memuat data dari file CSV dan melakukan preprocessing yang diperlukan."""
    df = pd.read_csv(filepath, encoding='ISO-8859-1')
    
    # Mengonversi kolom tanggal menjadi tipe datetime
    df['Hire Date'] = pd.to_datetime(df['Hire Date'], errors='coerce')
    df['Exit Date'] = pd.to_datetime(df['Exit Date'], errors='coerce')
    
    # Mengonversi kolom gaji dan bonus menjadi angka
    df['Annual Salary'] = df['Annual Salary'].replace('[\$,]', '', regex=True).astype(float)
    df['Bonus %'] = df['Bonus %'].replace('%', '', regex=True).astype(float)
    
    return df

def get_summary_statistics(df, column):
    stats = {
        'mean': df[column].mean(),
        'median': df[column].median(),
        'max': df[column].max(),
        'min': df[column].min(),
    }
    return stats
