import pandas as pd


# 1️⃣ Frequency Table
def frequency_table(df):
    manufacturer_counts = df['manufacturer'].value_counts().reset_index()
    manufacturer_counts.columns = ['Manufacturer', 'Count']

    return manufacturer_counts.to_html(
        classes="table table-hover table-striped table-bordered align-middle text-center",
        index=False
    )


# 2️⃣ Full Dataset
def full_dataset_table(df):
    return df.to_html(
        classes="table table-hover table-striped table-bordered align-middle",
        index=False
    )


# 3️⃣ Describe Table
def describe_table(df):
    description = df.describe(include='all')

    return description.to_html(
        classes="table table-hover table-striped table-bordered align-middle text-center",
        float_format="%.2f"
    )


# 4️⃣ Group By Selling Price
def group_by_selling_price(df):
    new_df = df.copy()
    new_df['profit'] = new_df['selling_price'] - new_df['wholesale_price'] 
    new_df['profit or loss'] = new_df['profit'].apply(lambda x: 'Profit' if x > 0 else ('Loss' if x < 0 else 'Break-even'))
    grouped = new_df.groupby(["manufacturer","fuel_type","transmission"]).agg({
        "selling_price": ["count","sum"],
        "wholesale_price": ["sum"],
        "profit":["sum"],
        "profit or loss": lambda x: x.value_counts().idxmax()
    }).rename(columns={"selling_price": "Vehicle Count"}).reset_index()

    return grouped.to_html(
        classes="table table-hover table-striped table-bordered align-middle text-center",
        index=False
    )


# 5️⃣ Pivot Table
def pivot_table_analysis(df):
    pivot = pd.pivot_table(
        df,
        values="selling_price",
        index="manufacturer",
        columns="fuel",
        aggfunc="mean"
    ).round(2)

    return pivot.to_html(
        classes="table table-hover table-striped table-bordered align-middle text-center"
    )


# 6️⃣ Cross Tabulation
def crosstab_analysis(df):
    cross_tab = pd.crosstab(
        df["manufacturer"],
        df["fuel"]
    )

    return cross_tab.to_html(
        classes="table table-hover table-striped table-bordered align-middle text-center"
    )
