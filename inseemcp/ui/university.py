from fastmcp import FastMCPApp
from prefab_ui.actions import SetState
from prefab_ui.app import PrefabApp
from prefab_ui.components import (
    Card,
    CardContent,
    Column,
    DataTable,
    DataTableColumn,
    Grid,
)
from prefab_ui.components.charts import BarChart, ChartSeries
from prefab_ui.rx import Rx

from backend.base import UniversityRequest

ui_app = FastMCPApp("Notes")


@ui_app.ui
async def team_directory() -> PrefabApp:
    instance = UniversityRequest()
    await instance()

    with PrefabApp() as app, Column(gap=4, css_class="p-6"), Grid(columns=[1, 2], gap=4):
        df = instance.dataframe[:10]
        df2 = df[['code_postal_uai', 'inscrits_2021']].groupby('code_postal_uai').sum()

        with  Card(), CardContent():
            BarChart(
                data=df2.to_dict(orient="records"),
                series=[
                    ChartSeries(dataKey="code_postal_uai", label="Code Postal UAI"),
                    ChartSeries(dataKey="inscrits_2021", label="Inscrits 2021"),
                ],
                x_axis="code_postal_uai",
                show_legend=True,
            )

        columns: list[DataTableColumn] = []
        for colum in instance.dataframe.columns:
            columns.append(DataTableColumn(key=colum, header=colum, sortable=True))

        with  Card(), CardContent():
            DataTable(
                columns=columns,
                rows=df.to_dict(orient="records"), # pyright: ignore[reportArgumentType]
                search=True,
                onRowClick=SetState("selected", Rx("$event")),
                paginated=True
            )
    return app
