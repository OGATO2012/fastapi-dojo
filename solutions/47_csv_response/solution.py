from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()


@app.get("/export/csv")
def export_csv():
    csv_data = "id,name,price\n1,Apple,1.50\n2,Banana,0.75\n3,Cherry,3.00\n"
    return Response(
        content=csv_data,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=items.csv"},
    )
