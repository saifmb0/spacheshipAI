from docx2pdf import convert
from docxtpl import DocxTemplate

class Report():
    def __init__(self, date, time, name, model_no, desc):
        date = date
        time = time
        name = name
        model_no = model_no
        desc = desc

    def write_document(self, output_path: str, template_path: str=r"AI\SpaceShipAI_Report_Template.docx") -> None:
        # Load the template
        doc = DocxTemplate(template_path)

        # Define the context with data to replace placeholders
        context = {
            "date": self.date,
            "time": self.time,
            "name": self.name,
            "model_no": self.model_no,
            "desc": self.desc
        }

        doc.render(context)
        doc.save(output_path)
        convert(output_path, output_path.replace(".docx", ".pdf"))