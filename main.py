from fpdf import FPDF
import pandas as pd

# Create a pdf object
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# Read data from csv file
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Add an empty page
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)

    # Create a gap between the header and the footer
    pdf.ln(265)

    # Set the footer
    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        # Add an empty page
        pdf.add_page()

        # Create a gap for the footer
        pdf.ln(277)

        # Set the footer
        pdf.set_font(family="Times", style="B", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

# Output the pdf object to file
pdf.output("output.pdf")