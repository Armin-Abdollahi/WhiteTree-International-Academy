import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from PIL import Image
from matplotlib.backends.backend_pdf import PdfPages
from PyPDF2 import PdfReader, PdfWriter
from matplotlib.font_manager import FontProperties

def plot_maker(df, output_pdf='report.pdf', name="Armin Abdollahi", age=25, date="2025-01-31"):
    front_cover_path = 'D:\WhiteTree\CogniFit_Report\data\Front_Cover.pdf'
    back_cover_path = 'D:\WhiteTree\CogniFit_Report\data\Back_Cover.pdf'

    # Create a PDF object
    pdf = PdfPages(output_pdf)

    # Create a figure with subplots of size A4
    fig = plt.figure(figsize=(8.27, 11.69))  # A4 size in inches

    # ----------------------------------------------- Page 2 -----------------------------------------------
    # Add logo and title to the top-left corner
    logo1 = Image.open('D:\WhiteTree\CogniFit_Report\images\Logo1.png')
    logo1 = logo1.resize((140, 27))  # Resize the logo to a smaller size
    fig.figimage(logo1, 50, fig.bbox.ymax - 50 - logo1.size[1])  # Position the logo at the top-left corner

    # Add personal information to the center-top of the page
    fig.text(0.5, 0.95, "Name:               Age:    Date of Evaluation:", fontsize=10, ha='center')
    fig.text(0.5, 0.93, f"{name}    {age}    {date}", fontsize=10, ha='center')

    # Add the title "CogniFit Profile" close to the figures
    fig.text(0.5, 0.85, "Cognitive Profile", fontsize=12, ha='center', weight='bold')

    # Create a table
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.axis('tight')
    ax1.axis('off')

    # Sample data for the table
    table_data = [['Visual Memory', 'Value 1'], ['Working Memory', 'Value 2'], ['Short-term Memory', 'Value 3'],
                  ['Focus Attention', 'Value 4'], ['Updating', 'Value 5'], ['Hand-Eye Coordination', 'Value 6'],
                  ['Spatial Perception', 'Value 7'], ['Reaction Time', 'Value 8'], ['Processing Speed', 'Value 9'],
                  ['Planning and Reasoning', 'Value 10']]

    # Set column widths: first column wider than the second
    col_widths = [0.69, 0.31]  # 70% for the first column, 30% for the second

    table = ax1.table(cellText=table_data,
                      colLabels=["Cognitive Ability", "Final Score"],
                      cellLoc='center',
                      loc='center',
                      colWidths=col_widths)

    # Modify the font properties of column labels
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_text_props(weight='bold', fontsize=12)

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)

    # Figure 2: Heptagon Plot with 10 parameters
    ax2 = fig.add_subplot(2, 2, 2, polar=True)

    # Use the first 10 elements from table_data for the heptagon
    labels = [row[0] for row in table_data]
    values = np.random.rand(len(labels))  # Generate random data for demonstration

    # Add the first value to the end of the lists to close the heptagon
    values = np.append(values, values[0])
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]  # Add the first angle to the end to close the heptagon

    ax2.fill(angles, values, color='blue', alpha=0.25)
    ax2.plot(angles, values, color='blue', linewidth=1)
    ax2.set_yticklabels([])
    ax2.set_xticks(angles[:-1])
    ax2.set_xticklabels(labels, fontsize=8)

    # Figure 3: Vertical bar chart (Page 2)
    ax3 = fig.add_subplot(2, 1, 2)
    y_pos = np.arange(len(labels))
    values_percent = values[:-1] * 100  # Convert to percentage
    ax3.bar(y_pos, values_percent, align='center')
    ax3.set_xticks(y_pos)
    ax3.set_xticklabels(['\n'.join(label.split()) for label in labels], fontsize=5, rotation=0, ha='center')
    for i, v in enumerate(values_percent):
        ax3.text(i, v + 1, f"{v:.1f}", color='blue', ha='center', fontsize=8)
    ax3.set_ylim(0, 100)  # Set y-axis limit from 0 to 100
    ax3.set_yticks(range(0, 101, 20))  # Set y-axis ticks from 0 to 100 with step of 20
    ax3.set_yticklabels([str(i) for i in range(0, 101, 20)])  # Remove % symbol from y-axis labels
    ax3.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines

    # Add the second logo to the bottom-right corner
    logo2 = Image.open('D:\WhiteTree\CogniFit_Report\images\WhiteTree.png')
    logo2 = logo2.resize((70, 70))  # Resize the logo to a smaller size
    fig.figimage(logo2, fig.bbox.xmax - 50 - logo2.size[0], fig.bbox.ymin + 50)  # Position the logo at the bottom-right corner

    # Save the first page
    pdf.savefig(fig)
    plt.close(fig)

    # ----------------------------------------------- Page 3 -----------------------------------------------
    fig = plt.figure(figsize=(8.27, 11.69))  # A4 size in inches

    # Add logo and title to the top-left corner
    fig.figimage(logo1, 50, fig.bbox.ymax - 50 - logo1.size[1])  # Position the logo at the top-left corner

    # Add personal information to the center-top of the page
    fig.text(0.5, 0.95, "Name:               Age:    Date of Evaluation:", fontsize=10, ha='center')
    fig.text(0.5, 0.93, f"{name}    {age}    {date}", fontsize=10, ha='center')

    # Add the title "Assessment Results" close to the figures
    fig.text(0.5, 0.85, "Assessment Results", fontsize=12, ha='center', weight='bold')

    # Add a 3-column 7-row table with size matching the bar chart
    ax4 = fig.add_subplot(2, 1, 1)
    ax4.axis('tight')
    ax4.axis('off')

    # Sample data for the table
    table_data_page2 = [['Assessment Name', 'Score', 'Description'],
                        ['Psychomotor Vigilance Test', 'Value 1.2', 'Value 1.3'],
                        ['Eye-Hand Coordination Test', 'Value 2.2', 'Value 2.3'],
                        ['Eye-Hand Coordination MUD', 'Value 3.2', 'Value 3.3'],
                        ['Maze Test', 'Value 4.2', 'Value 4.3'],
                        ['Digit Span Test', 'Value 5.2', 'Value 5.3'],
                        ['Visual Memory Test', 'Value 6.2', 'Value 6.3']]

    # Set column widths: 22% for first column, 11% for second, and the rest (67%) for the third
    col_widths = [0.22, 0.11, 0.67]

    table_page2 = ax4.table(cellText=table_data_page2,
                            cellLoc='center',
                            loc='center',
                            colWidths=col_widths)

    # Modify the font properties of column labels
    for (row, col), cell in table_page2.get_celld().items():
        if row == 0:
            cell.set_text_props(weight='bold', fontsize=12)

    table_page2.auto_set_font_size(False)
    table_page2.set_fontsize(6)
    table_page2.scale(1, 1.5)  # Scale to match bar chart size

    # Figure 4: Vertical bar chart (Page 3)
    ax5 = fig.add_subplot(2, 1, 2)
    labels_page2 = [row[0] for row in table_data_page2[1:]]  # Exclude header row
    values_page2 = np.random.rand(len(labels_page2)) * 100  # Generate random data as percentage
    y_pos_page2 = np.arange(len(labels_page2))
    ax5.bar(y_pos_page2, values_page2, align='center')
    ax5.set_xticks(y_pos_page2)
    ax5.set_xticklabels(['\n'.join(label.split()) for label in labels_page2], fontsize=5, rotation=0, ha='center')
    for i, v in enumerate(values_page2):
        ax5.text(i, v + 1, f"{v:.1f}", color='blue', ha='center', fontsize=8)
    ax5.set_ylim(0, 100)  # Set y-axis limit from 0 to 100
    ax5.set_yticks(range(0, 101, 20))  # Set y-axis ticks from 0 to 100 with step of 20
    ax5.set_yticklabels([str(i) for i in range(0, 101, 20)])  # Remove % symbol from y-axis labels
    ax5.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines

    # Add the second logo to the bottom-right corner
    fig.figimage(logo2, fig.bbox.xmax - 50 - logo2.size[0], fig.bbox.ymin + 50)  # Position the logo at the bottom-right corner

    # Save the second page
    pdf.savefig(fig)
    plt.close(fig)

    # Close the PDF file
    pdf.close()

    # Merge front cover, report, and back cover
    front_pdf = PdfReader(front_cover_path)
    report_pdf = PdfReader(output_pdf)
    back_pdf = PdfReader(back_cover_path)

    output = PdfWriter()

    # Add front cover
    output.add_page(front_pdf.pages[0])

    # Add report pages
    for page in report_pdf.pages:
        output.add_page(page)

    # Add back cover
    output.add_page(back_pdf.pages[0])

    # Save the merged PDF
    with open(output_pdf, 'wb') as f:
        output.write(f)

    # Download the merged PDF
    print(f"PDF report generated successfully: {output_pdf}")

# Example usage with a sample dataframe
data = {
    'Visual Memory': np.random.rand(100),
    'Working Memory': np.random.rand(100),
    'Short-term Memory': np.random.rand(100),
    'Focus Attention': np.random.rand(100),
    'Updating': np.random.rand(100),
    'Hand-Eye Coordination': np.random.rand(100),
    'Spatial Perception': np.random.rand(100),
    'Reaction Time': np.random.rand(100),
    'Processing Speed': np.random.rand(100),
    'Planning and Reasoning': np.random.rand(100),
    'Psychomotor Vigilance Test': np.random.rand(100),
    'Eye-Hand Coordination Test': np.random.rand(100),
    'Eye-Hand Coordination MUD': np.random.rand(100),
    'Maze Test': np.random.rand(100),
    'Digit Span Test': np.random.rand(100),
    'Visual Memory Test': np.random.rand(100),
    'Visual Working Memory Span': np.random.rand(100)
}
df = pd.DataFrame(data)
plot_maker(df)