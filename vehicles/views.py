import pandas as pd
from django.shortcuts import render
from .dashboard import (
    frequency_table,
    full_dataset_table,
    describe_table,
    group_by_selling_price,
    pivot_table_analysis,
    crosstab_analysis
)


def dashboard_view(request):
    df = pd.read_csv("dummy_data/vehicles_data_1000.csv")

    return render(request, "vehicles/index.html", {
        "frequency_table": frequency_table(df),
        "describe_table": describe_table(df),
        "full_dataset": full_dataset_table(df),
        "grouped_selling_price": group_by_selling_price(df),
        "pivot_table": pivot_table_analysis(df),
        "crosstab_table": crosstab_analysis(df)
    })
