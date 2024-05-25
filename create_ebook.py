from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Children\'s Book', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_image(self, image_path):
        self.image(image_path, x=10, y=None, w=190)
        self.ln(10)

def create_ebook(text_files, image_files, output_path):
    pdf = PDF()
    pdf.add_page()

    for text_file, image_file in zip(text_files, image_files):
        with open(text_file, 'r') as file:
            text = file.read()
            pdf.chapter_body(text)
        pdf.add_image(image_file)

    pdf.output(output_path)

if __name__ == "__main__":
    text_files = ["texts/text1.txt", "texts/text2.txt"]
    image_files = ["images/image1.png", "images/image2.png"]
    output_path = "output/ebook.pdf"

    create_ebook(text_files, image_files, output_path)
    print(f"Ebook created and saved to {output_path}")
