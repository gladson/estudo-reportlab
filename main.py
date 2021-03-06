from reportlab.lib import colors
from reportlab.platypus import Table
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.platypus.tables import TableStyle

table_header = [
    ["NAME1", "NAME2"],
]

table_obj = []

LIST_STYLE = TableStyle(
    [
        ('LINEABOVE', (0,0), (-1,0), 2, colors.green),
        ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 2, colors.green),
        ('ALIGN', (1,1), (-1,-1), 'RIGHT')
    ]
)

for x in range(2):
    for x in range(6):
        table_header.append(["id", "value"])
    table_obj.append(Table(data=table_header, style=LIST_STYLE))

doc = table_obj

documento = SimpleDocTemplate("export/example1.pdf", pagesize=A4, showBoundary=0)

documento.build(doc)